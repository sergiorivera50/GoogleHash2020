def parseData(fileName):
    with open(fileName, "r") as f:
        lines = list(l.strip() for l in f.readlines())
        f.close()

    initData = lines[0].split()
    numBooks = int(initData[0])
    numLibraries = int(initData[1])
    days = int(initData[2])

    print(numBooks, numLibraries, days)
    
    bookScores = lines[1].split()
    print(bookScores)

    allBooks = []
    for i in range(numBooks):
        allBooks.append(Book(bookScores[i]))

    libraries = []
    libraryCount = 0
    count = 2
    for i in range(numLibraries):
        libraryData = lines[count].split()
        numBooks = int(libraryData[0])
        libraryBooksIds = lines[count+1].split() # get book ids for this library from next line
        libraryBooks = []
        for j in range(len(libraryBooksIds)):
            for book in allBooks:
                if book.id == int(libraryBooksIds[j]):
                    libraryBooks.append(book)
        libraries[libraryCount].append(Library(libraryBooks, libraryData[1], libraryData[2]))
        count += 2 # jump to the next library
        libraryCount += 1
    
    return allBooks, libraries


allBooks, libraries = parseData("a_example.txt")

"""
init_data = lines[0].split()
n_videos = int(init_data[0])
n_endpoints = int(init_data[1])
n_requests = int(init_data[2])
n_caches = int(init_data[3])
cache_capacity = int(init_data[4])
video_sizes = lines[1].split()

# [video size (megabytes)]
videos = []
for i in range(n_videos):
    videos.append(Video(i, int(video_sizes[i])))

# [cache id, cache capacity]
cache_servers = []
for i in range(n_caches):
    cache_servers.append(CacheServer(i, cache_capacity))

# [endpoint id, latency to data center, [[cache id, cache latency], ...]]
endpoints = []
line_count = 2
for i in range(n_endpoints):
    endpoint_data = lines[line_count].split()
    latency = int(endpoint_data[0])
    n_connections = int(endpoint_data[1])
    cache_connections = []
    line_count += 1
    for j in range(n_connections):
    cache_connections.append((int(lines[line_count].split()[0]), int(lines[line_count].split()[1])))
    line_count += 1
    endpoints.append(EndPoint(i, latency, cache_connections))

# [video id, endpoint id, num requests]
requests = []
for i in range(n_requests):
    request_data = lines[line_count].split()
    requests.append(Request(int(request_data[0]), int(request_data[1]), int(request_data[2])))
    line_count += 1

# video: [video size (megabytes)]
# cache: [cache id, cache capacity]
# endpoint: [endpoint id, latency to data center, [[cache id, cache latency], ...] <- cache connections] 
# request: [video id, endpoint id, num requests]

return videos, cache_servers, endpoints, requests
"""