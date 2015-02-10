from tbay import User, Bid, Item, session

wade = User(name="Wade Boggs", password="Red Sox")
don = User(name="Don Mattingly", password="Yankees")
cal = User(name="Cal Ripken", password="Orioles")

baseball = Item(name="World Series Baseball", description="Game used basedball from 1983 World Series")

baseball.owner = cal

bid1 = Bid(price=25)
bid2 = Bid(price=30)
bid3 = Bid(price=35)
bid4 = Bid(price=40)

bid1.item = baseball
bid2.item = baseball
bid3.item = baseball
bid4.item = baseball

bid1.owner = wade
bid2.owner = don
bid3.owner = wade
bid4.owner = don

session.add_all([wade, don, cal, baseball, bid1, bid2, bid3, bid4])
session.commit()

baseball_id = session.query(Item.id).filter(Item.name == "World Series Baseball").all()
baseball_id = baseball_id[0][0]
winner = session.query(Bid.price, Bid.owner_id).filter(Bid.item_id == baseball_id).order_by(Bid.price).all()
winner = winner.pop()

winner_name = session.query(User.name).filter(User.id == winner[1]).all()
print "The winner of the auction is {}".format(winner_name)