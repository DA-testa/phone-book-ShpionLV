# python3
# Artūrs Brūvers 221RDB511 DS-14

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            if cur_query.number in contacts:
                contacts[cur_query.number].name = cur_query.name
            else:
                contacts[cur_query.number] = cur_query
        elif cur_query.type == 'del':
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        else:
            if cur_query.number in contacts:
                result.append(contacts[cur_query.number].name)
            else:
                result.append('not found')
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

