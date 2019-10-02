'''
    1-start,1.1,1.3,1.2

    -> Sweep the kitchen and dust the living room.
        • Participant retrieves broom from supply closet
        • Participant retrieves dust pan and brush from closet
        • Participant retrieves duster from supply closet
'''

import re

def getActivityList(s):

    list = []
    val = re.split('\.', s)

    # region Uncued Tasks
    if s[0:2] == '1-' or val[0] == '1':
        list.append("Sweep the kitchen and dust the living room.")
        list.append("Participant retrieves broom from supply closet")
        list.append("Participant retrieves duster from supply closet")
        list.append("Participant retrieves dust pan and brush from closet")
        list.append("Participant sweeps kitchen floor")
        list.append("Participant uses dust pan and brush")
        list.append("Participant dusts living room")
        list.append("Participant dusts dining room")
        list.append("Participant returns broom to supply closet")
        list.append("Participant returns duster to supply closet")
        list.append("Participants returns dust pan and brush to supply closet")

    if s[0:2] == '2-' or val[0] == '2':
        list.append("Obtain a set of medicines and a weekly medicine dispenser, fill as per directions.") 
        list.append("Participant retrieves materials from cupboard \"A\"")
        list.append("Participant reads instructions")
        list.append("Participant fills dispenser with medication")

    if s[0:2] == '3-' or val[0] == '3':
        list.append("Write a birthday card, enclose a check and address an envelope.") 
        list.append("Participant sits at dining room table")
        list.append("Participant retrieves birthday card")
        list.append("Participant writes birthday wish inside the card: \"Happy Birthday\" Name Wish")
        list.append("Participant retrieves check")
        list.append("Participant writes check for birthday card")
        list.append("Participant puts birthday card and check in envelope")
        list.append("Participant addresses the envelope")
        list.append("Participant places envelope in the mail organizer")

    if s[0:2] == '4-' or val[0] == '4':
        list.append("Find the appropriate DVD and watch the corresponding news clip.")  
        list.append("Participant moves to the living room")
        list.append("Participant selects correct DVD")
        list.append("Participant reads instructions next to the T.V.")
        list.append("Participants uses remote to turn on TV")
        list.append("Participant selects correct channel")
        list.append("Participant watches news clip")
        list.append("Participant turns off T.V.")
        list.append("Participant returns DVD to pile")

    if s[0:2] == '5-' or val[0] == '5':
        list.append("Obtain a watering can and water all plants in the living space.")  
        list.append("Participant retrieves watering can from supply closet")
        list.append("Participant fills watering can")
        list.append("Participant waters plants (windowsill)")
        list.append("Participant waters plants (coffee table)")
        list.append("Participant empties extra water into sink")
        list.append("Participant returns watering can to supply closet")

    if s[0:2] == '6-' or val[0] == '6':
        list.append("Answer the phone and respond to questions pertaining to the video from task 4.") 
        list.append("Participant answers the phone")
        list.append("Participant answers questions over the phone")
        list.append("Participant sits down during conversation")
        list.append("Participant stands in one place")
        list.append("Participant walks around during phone call")
        list.append("Participant hangs up the phone")

    if s[0:2] == '7-' or val[0] == '7':
        list.append("Prepare a cup of soup using the microwave.")  
        list.append("Participant retrieves materials from cupboard \"A\"")
        list.append("Participant fills measuring cup with water")
        list.append("Participant boils water in microwave")
        list.append("Participant pours water into cup of noodles")
        list.append("Participant retrieves pitcher of water from refrigerator")
        list.append("Participant pours glass of water")
        list.append("Participant returns pitcher of water")
        list.append("Participant waits for water to simmer in cup of noodles")
        list.append("Participant brings all items to dining room table")

    if s[0:2] == '8-' or val[0] == '8':
        list.append("Find the appropriate DVD and watch the corresponding news clip.")  
        list.append("Participant moves to the living room")
        list.append("Participant selects correct DVD")
        list.append("Participant reads instructions next to the T.V.")
        list.append("Participants uses remote to turn on TV")
        list.append("Participant selects correct channel")
        list.append("Participant watches news clip")
        list.append("Participant turns off T.V.")
        list.append("Participant returns DVD to pile")
    #endregion

    # region Cued Tasks
    if s[0:2] == '9-' or val[0] == '9':
        list.append("Check the wattage of a desk lamp and replace the bulb.") 
        list.append("Participant checks wattage")
        list.append("Participant moves to the kitchen")
        list.append("Participant retrieves light bulbs from cabinet \"B\"")
        list.append("Participant moves to the dining room")
        list.append("Participant removes old light bulb")
        list.append("Participant throws away old light bulb")
        list.append("Participant replaces the bulb")

    if s[0:3] == '10-' or val[0] == '10':
        list.append("Wash hands with soap at the kitchen sink.") 
        list.append("Participant moves to the kitchen")
        list.append("Participant turns on water")
        list.append("Participant uses hand soap")
        list.append("Participant washes hands")
        list.append("Participant dries hands")

    if s[0:3] == '11-' or val[0] == '11':
        list.append("Wash and dry all kitchen countertop surfaces.") 
        list.append("Participant locates the sponge")
        list.append("Participant locates the dish detergent")
        list.append("Participant wets the sponge")
        list.append("Participant lathers the sponge with the detergent")
        list.append("Participant washes the countertops")
        list.append("Participant rinses out the sponge")
        list.append("Participant dries the countertops")
        list.append("Participant returns the sponge to the sponge drying dish")

    if s[0:3] == '12-' or val[0] == '12':
        list.append("Place a phone call to a recording and write down the recipe heard.") 
        list.append("Participant moves to the dining room table")
        list.append("Participant sits at dining room table")
        list.append("Participant locates the phone book")
        list.append(" Participant locates the phone number for \"Safeway Food and Drugs\"")
        list.append("Participant dials the number and listens to the recording")
        list.append("Participant records the recipe")
        list.append("Participant hangs up the phone")

    if s[0:3] == '13-' or val[0] == '13':
        list.append("Sort and fold a basketful of clothing containing men's, women's and children's articles.") 
        list.append("Participant moves to the hallway closet")
        list.append("Participant locates the laundry basket")
        list.append("Participant moves to the couch")
        list.append("Participant sorts/folds the laundry")

    if s[0:3] == '14-' or val[0] == '14':
        list.append("Prepare a bowl of oatmeal on the stovetop from the directions given in task 12.") 
        list.append("Participant moves to the kitchen")
        list.append("Participant removes materials from cupboard")
        list.append("Participant locates pot")
        list.append("Participant turns on stove")
        list.append("Participant fills pot with water")
        list.append("Participant puts oatmeal into pot")
        list.append("Participants times one minute")
        list.append("Participant stirs oatmeal")
        list.append("Participant puts oatmeal into bowl")
        list.append("Participant turns stove off")
        list.append("Participant puts sugar in oatmeal")
        list.append("Participant puts raisin in oatmeal")
        list.append("Participant throws raisin box in trashcan")

    if s[0:3] == '15-' or val[0] == '15':
        list.append("Sort and file a small collection of billing statements.") 
        list.append("Participant moves to the living room")
        list.append("Participant gathers statements from bookshelf")
        list.append("Participant moves to the dining room table")
        list.append("Participant sits down at the dining room table")
        list.append("Participant sorts pile of statements into the organizer")

    if s[0:3] == '16-' or val[0] == '16':
        list.append("Setup hands for a card game, answer the phone and describe the rules of the game.") 
        list.append("Participant moves to the kitchen")
        list.append("Participant locates deck of cards from kitchen cabinet \"B\"")
        list.append("Participant brings deck of cards to the dining room table")
        list.append("Participant sets up card game")
        list.append("Participant answers the telephone")
        list.append("Participant explains the rules of the game over the phone")
        list.append("Participant hangs up the phone")
    #endregion

    #region Intervowen Uncued Tasks

    if s[0:2] == '17':
        list.append("Examine a bus schedule; plan a trip including length of time and when to leave.") 

    if s[0:2] == '18':
        list.append("Microwave a comfort heat-pack for the bus ride.") 

    if s[0:2] == '19':
        list.append("Select a magazine to read during the trip.") 

    if s[0:2] == '20':
        list.append("Count out appropriate change for bus fare.") 

    if s[0:2] == '21':
        list.append("Take a dose of an anti-motion sickness medication.") 

    if s[0:2] == '22':
        list.append("Find a recipe book, gather ingredients cited as necessary for a picnic meal." )

    if s[0:2] == '23':
        list.append("Obtain a picnic basket from the hall closet and fill with all items for the trip.") 

    if s[0:2] == '24':
        list.append("Take the filled picnic basket toward the apartment exit, as though leaving as planned.") 
    #endregion

    return list


def getStartActivityIndex(s):
    pattern = ','
    res = re.split(pattern, s)
    indices = []

    for i in res[1:]:
        indices.append(i.split('.')[1])

    return indices

def getActivityIndex(s):
    pattern = ','
    res = re.split(pattern, s)
    indices = []

    for i in res:
        indices.append(i.split('.')[1])

    return indices
