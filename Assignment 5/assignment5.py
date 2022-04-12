import itertools, math

class Graph:
    class _Vertex:
        def __init__(self, id, name, gender, age=None, adopted=False):
            self.id = id
            self.name = name
            self.gender = 'M' if gender.lower() == 'male' or gender.lower() == 'm' else 'F'
            self.age = age
            self.adopted = adopted
            self.edge_list = []

        def __eq__(self, other):
            return self.id == other.id
        
        def __hash__(self):
            return hash(self.id)

        def __str__(self):
            return '['+str(self.id)+' | '+self.name+ ']'
        
        def get_vertex(self):
            return '[ID: '+str(self.id)+' | Name: '+self.name+' | Gender: '+self.gender+\
                ' | Age: '+str(self.age) + ' | Adopted: ' + str(self.adopted) + ']'
        
        def get_edge_list(self):
            return self.edge_list
    
    class _Edge:
        _WEIGHT = {
            1: 'married',
            2: 'parent-child',
            3: 'siblings',
            5: 'divorced',
            6: 'separated',
        }
        def __init__(self, dest, weight):
            self.dest = dest
            self.weight = weight

        def __str__(self) -> str:
            relationship = self._WEIGHT[self.weight]
            return '[' + str(self.dest) + ' - relationship: ' + relationship + ']'

        def get_dest_vertex(self):
            return self.dest

    def __init__(self):
        self._vertices = set()
        self._edges = set()

    def add_vertex(self, person: _Vertex):
        self._vertices.add(self._Vertex(person.id, person.name, person.gender))

    def get_vertices(self):
        return self._vertices

    def get_vertex_object(self, id) -> _Vertex:
        for vertex in self._vertices:
            if vertex.id == id:
                return vertex
        return None

    def get_next_id(self):
        m = max(self._vertices, key=lambda v: v.id).id
        return  m

    def edge_exists(self, origin: _Vertex, dest: _Vertex):
        for vertex in origin.get_edge_list():
            if vertex.get_dest_vertex() == dest:
                return True
        return False

    def add_edge(self, v1: _Vertex, v2: _Vertex, weight):
        origin = self.get_vertex_object(v1.id)
        dest = self.get_vertex_object(v2.id)

        if origin and dest:
            if not self.edge_exists(origin, dest) and origin is not dest:
                origin.edge_list.append(self._Edge(dest, weight))
            else:
                print('Edge already exists between ' + str(origin) + ' and ' + str(dest))
        else:
            print('Origin: '+ str(origin) +' Dest: '+str(dest))    

    def get_edges(self, vertex: _Vertex):
        return vertex.get_edge_list() 

    def update_vertex(self, old_vertex: _Vertex, new_vertex: _Vertex):
        new_edge_list = []
        for v in self._vertices:
            if v == old_vertex:
                new_edge_list = v.get_edge_list()
                self._vertices.remove(v)
                break
        new_vertex.edge_list = new_edge_list
        self._vertices.add(new_vertex)

    def update_edge(self, from_vertex: _Vertex, to_vertex: _Vertex, weight):
        if from_vertex and to_vertex and self.edge_exists(from_vertex, to_vertex):
            for vertex in self._vertices:
                if vertex.id == from_vertex.id:
                    for e in vertex.get_edge_list():
                        if e.get_dest_vertex().id == to_vertex.id:
                            e.weight = weight
                elif vertex.id == to_vertex.id: # bidirectional change
                    for e in vertex.get_edge_list():
                        if e.get_dest_vertex().id == from_vertex.id:
                            e.weight = weight
        else:
            print('No edge exists between ' + str(from_vertex) + ' and ' + str(to_vertex))
            self.add_edge(from_vertex, to_vertex, weight)

    def delete_vertex(self, vertex: _Vertex):
        for v in self._vertices:
            if v == vertex:
                for e in v.get_edge_list():
                    self.delete_edge(v, e.get_dest_vertex())
        self._vertices.remove(vertex)

    def delete_edge(self, from_vertex: _Vertex, to_vertex: _Vertex):
        if from_vertex and to_vertex and self.edge_exists(from_vertex, to_vertex):
            for vertex in self._vertices:
                if vertex.id == from_vertex.id:
                    for e in vertex.get_edge_list():
                        if e.get_dest_vertex().id == to_vertex.id:
                            vertex.edge_list.remove(e)
                elif vertex.id == to_vertex.id: # bidirectional change
                    for e in vertex.get_edge_list():
                        if e.get_dest_vertex().id == from_vertex.id:
                            vertex.edge_list.remove(e)
        else:
            print('No edge exists between ' + str(from_vertex) + ' and ' + str(to_vertex))

    def print_graph(self):
        for v in self.get_vertices():
            print(v, '--->', end=' ')
            for e in self.get_edges(v):
                print(e, end=' ')
            print()

class Person:
    def __init__(self, id, name, gender, age=None, adopted=False):
        self.id = id
        self.name = name
        self.gender = 'M' if gender.lower() == 'male' or gender.lower() == 'm' else 'F'
        self.age = age
        self.adopted = adopted
        pass

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.id == other.id or (self.name == other.name and self.gender == other.gender and self.age == other.age)
    
    def __hash__(self):
        return hash(self.id)

    def __str__(self, long=False):
        return '['+str(self.id)+' | '+self.name+ ']' if not long else \
                '[ID: '+str(self.id)+' | Name: '+self.name+' | Gender: '+self.gender+\
                ' | Age: '+str(self.age) + ' | Adopted: ' + str(self.adopted) + ']'

class FamilyTree():
    _RELATIONSHIP = {
        'married': 1,
        'parent-child': 2,
        'siblings': 3,
        'divorced': 5,
        'separated': 6,
    }

    def __init__(self, file='familytree.txt'):
        self._graph = Graph()
        self._initialize(file)

    def _initialize(self, file):
        with open(file, mode='r', encoding='utf-8-sig') as txt:
            families = list()
            tag = ''
            for line in txt:
                if line.startswith('Family'):
                    family = []
                    tag = 'p'
                elif line.strip().startswith('Relationship'):
                    family.append(line.strip())
                    relationship = line.strip()[14:]
                    if(len(family) > 1):
                        self._graph.add_edge(family[0], family[1], self._RELATIONSHIP[relationship.lower()])
                        self._graph.add_edge(family[1], family[0], self._RELATIONSHIP[relationship.lower()])
                elif line.strip().startswith('Children'):
                    family.append('Children')
                    tag = 'c'
                elif line.strip().startswith('End'):
                    families.append(family.copy())
                else: # add person as vertex, and edge if they have children
                    person = self._get_person(line)
                    family.append(person)
                    self._graph.add_vertex(person)
                    if tag == 'c':
                        self._graph.add_edge(family[0], family[-1], self._RELATIONSHIP['parent-child'])
                        if  isinstance(family[1], Person):
                            self._graph.add_edge(family[1], family[-1], self._RELATIONSHIP['parent-child'])
            # add sibling edges/relationships
            for family in families:
                children = family[family.index('Children')+1:] if 'Children' in family else []
                for siblings in itertools.combinations(children, 2):
                    self._graph.add_edge(siblings[0], siblings[1], self._RELATIONSHIP['siblings'])
                    self._graph.add_edge(siblings[1], siblings[0], self._RELATIONSHIP['siblings'])
                
    def _get_person(self, line):
        name = line.split('(')[0].strip()
        gender = line[line.find("(")+1:line.find(")")].strip()
        id = line[line.find("{")+1:line.find("}")][3:].strip()
        adopted = True if line[line.find("[")+1:line.find("]")] == "Adopted" else False
        return Person(id, name, gender, adopted=adopted)

    def add_family_member(self):
        name = input('Name: ')
        gender = input('Gender (M or F): ')
        age = int(input('Age: '))
        id = str(int(self._graph.get_next_id()) + 1).rjust(3, '0')
        
        person = Person(id, name, gender, age)
        self._graph.add_vertex(person)
        print(str(person) + ' added successfully"')
    
    def show_family_tree(self):
        print('\n----------------------------------------------------')
        print('Family Tree')
        print('----------------------------------------------------')
        self._graph.print_graph()
        print()

    def get_bool(prompt):
        while True:
            try:
                return {"true":True,"false":False}[input(prompt).lower()]
            except KeyError:
                print("Invalid input please enter True or False!")
    
    def edit_family_member(self):
        self.show_family_tree()
        prompt1 = input('index of the family member you want to edit: ')
        old_vertex = self._graph.get_vertex_object(prompt1)
        print(old_vertex.get_vertex())

        name_p = input('Name: ')
        name = name_p if name_p else old_vertex.name
        gender_p = input('Gender (M or F): ')
        gender = gender_p if gender_p else old_vertex.gender
        adopted_p = {"true":True,"false":False,"t":True,"f":False,"":False}[input('Adopted (T or F):').lower()]
        adopted = adopted_p if adopted_p else old_vertex.adopted
        age_p = input('Age: ')
        age = age_p if age_p else old_vertex.age

        new_vertex = self._graph._Vertex(old_vertex.id, name, gender, age=age, adopted=adopted)
        
        self._graph.update_vertex(old_vertex, new_vertex)
        print(str(new_vertex)+' has been updated successfuly!')


    def edit_family_tree(self):
        self.show_family_tree()
        prompt1 = input('ID of the relationships you want to edit (from): ')
        prompt2 = input('ID of the relationships you want to edit (to): ')
        print('Possible relationships')
        for k,v in self._RELATIONSHIP.items():
            print(v, k)
        prompt3 = int(input('Index: '))
        from_vertex = self._graph.get_vertex_object(prompt1)
        to_vertex = self._graph.get_vertex_object(prompt2)
        weight = prompt3
        self._graph.update_edge(from_vertex,to_vertex,weight)
        print('relationship between ' + str(from_vertex) + str(to_vertex) + ' updated successfully!')

    def remove_family_member(self):
        self.show_family_tree()
        prompt = input('index of the family member you want to delete: ')
        vertex = self._graph.get_vertex_object(prompt)
        if vertex:
            self._graph.delete_vertex(vertex)
            print(str(vertex) + ' deleted successfully!')
        else:
            print('Id not found')
    

if __name__ == '__main__':

    familyTree = FamilyTree()
    while True:
        index = int(input('\nWelcome to the Family!\n1. Show Family Tree\n2. Add Person to Family Tree\n'+
                        '3. Remove Person from Family Tree\n4. Update Family Tree (relationships)\n5. Update Family Member\n6. Exit\n:'))
        if index == 1:
            familyTree.show_family_tree()
        elif index == 2:
            familyTree.add_family_member()
        elif index == 3:
            familyTree.remove_family_member()
        elif index == 4:
            familyTree.edit_family_tree()
        elif index == 5:
            familyTree.edit_family_member()
        else:
            break