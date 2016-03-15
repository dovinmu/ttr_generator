from bs4 import BeautifulSoup
import random

def generateCards():
    with open('routes.json') as f:
        import json
        routes = json.loads(f.read())
    #load file parts: prefix & suffix
    with open('TTR_cards_all_locations.svg') as f:
        svg = f.read()
        soup = BeautifulSoup(svg, 'lxml')
        resultSet = soup.findAll('circle')[1:]

        svg = svg.split('<!--end prefix-->')
        prefix = svg[0]
        svg = svg[1].split('<!--end name-->')
        name_geom = svg[0]
        svg = svg[1].split('<!--end number-->')
        number_geom = svg[0]
        suffix = svg[1].split('<!--end destinations-->')[1]

    for i in range(len(resultSet)):
        sample = random.sample(resultSet[i+1:], int(len(resultSet[i:])/4))
        for result2 in sample:
            route = (resultSet[i], result2)
            routeNames = (route[0].text.strip(), route[1].text.strip())
            print(' ==> '.join(routeNames))
            num = findRouteLength(routeNames[0].replace(' ',''),
                routeNames[1].replace(' ',''), routes)
            if num < 3:
                continue
            num = num*2 + random.randint(0,2)
            #...card-specific information: score, name, dots
            name1 = routeNames[0]
            name2 = routeNames[1]
            if 'name' in routes[name1]:
                name1 = routes[name1]['name']
            if 'name' in routes[name2]:
                name2 = routes[name2]['name']
            if len(name1) + len(name2) > 23:
                if 'abbreviation' in routes[routeNames[0]]:
                    name1 = routes[routeNames[0]]['abbreviation']
            if len(name1) + len(name2) > 23:
                if 'abbreviation' in routes[routeNames[1]]:
                    name2 = routes[routeNames[1]]['abbreviation']
            if len(name1) + len(name2) > 23:
                print('Could not sufficiently abbreviate {}'.format(routeNames))
    #TODO: abbreviate long names
            name_output = name_geom.replace('NAME', name1 + ' - ' + name2)
            num = str(num)
            if len(num) == 1:
                num = ' ' + num
            number_output = number_geom.replace('NUMBER', str(num))
            with open('cards/' + '-'.join(routeNames) + '.svg', 'w') as f:
                f.write(prefix)
                f.write(name_output)
                f.write(number_output)
                f.write(str(route[0]))
                f.write(str(route[1]))
                f.write(suffix)



def findRouteLength(start, stop, routes):
    leaves = set(routes[start]['neigh'])
    dist = {}
    visited = {}
    distCount = 1
    for leaf in leaves:
        dist[leaf] = distCount
    while len(leaves) > 0:
        #print(leaves)
        newLeaves = set()
        for leaf in leaves:
            visited[leaf] = True
            if leaf == stop:
                return dist[leaf]
            for neigh in routes[leaf]['neigh']:
                if neigh not in visited:
                    newLeaves.add(neigh)
        leaves = newLeaves
        distCount += 1
        for leaf in leaves:
            dist[leaf] = distCount
    print(start, stop)
    return None

if __name__ == "__main__":
    generateCards()
