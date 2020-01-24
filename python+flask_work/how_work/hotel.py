class Hotel():
    def __init__(self, name, location, residents):
        self.name = name
        self.location = location
        self.residents = residents
        self.total_gust = 0

    def chek_in(self, gust,):
        self.total_gust += gust
        print('welcome to our hotel {} you are in room {} ')

            print('sorry {} we dont have empty rooms ')

    def cheke_out(self, name, room_num):
        if name in self.rooms.keys() and room_num in self.rooms.values():

            print('we hope to sea you agen in {} hotel'.format(self.name))


ameen = Hotel('DH', 'moon', 10)
ameen.chek_in('adma')
ameen.cheke_out()
