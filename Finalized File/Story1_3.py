import tkinter.scrolledtext as st
import sys
sys.path.insert(0, '/Hackathon Project/Pages')
from winconfig import *
import tkinter as tk
win = tk.Tk()
w = story1Window(win)
window = Mbar(win)
w.set()
window.nav()
win.title("Story1_3")

#------------------------------------------------------#

#Darkmode
switch = True
def DarkMode():
    global switch
    if switch == True:
        text_area.config(background = "#333333", foreground = "white")
        win.config(background = "#333333")
        switch = False
    elif switch == False:
        text_area.config(background = "white", foreground = "#333333")
        win.config(background = "white")
        switch = True

def Back():
    win.destroy()
    sys.path.insert(0, './Pages')
    import Story1

def index():
    win.destroy()
    sys.path.insert(0, './Pages')
    import index


# Title Label
tk.Label(win,
         text = "Chapter 1",
         font = ("Times New Roman", 20),
         width = 50,
         background = '#850101',
         foreground = "white").pack()

text_area = st.ScrolledText(win,
                            height = 16,
                            font = ("Times New Roman",20),
                            highlightthickness=0)

text_area.pack(pady = 10, padx = 50)

text_area.insert(INSERT,
"""
 Life is not always as we think of it I thought I knew what I always wanted and what is takes to fall in love but I was wrong i knew entering the Great Citadel Library was forbidden. But i saw that girl again. The one who had met my gaze in the Citadel gym and held it just a little too long.  
After weeks of returning to the gym, and searching every face in the crowd, I finally saw her again.  
The library was restricted to only some families , and mine was not a part of it . I scoffed at the library system enforced by the owner, designed to keep our family out of it. that day, i got more than i expected. I  slipped into the library and followed the girl through its maze-like halls. Crouched in a shadowed alcove in a large stone chamber, i witnessed some kind of ritual. The girl stood before a long wooden table. It was covered with vials of liquid, and countless containers of various herbs and sundries. she read words from a book out loud as she combined ingredients together. 
The words she spoke were foreign to me.  
A white smoke streamed out of the flask, filling the room.  It was a clear, viscous liquid with the slightest amber hue. 
The girl was visibly relieved, letting out a long sigh and wiping a bead of sweat off her brow. But as she set the flask down, the slightest drip of the clear liquid dribbled off the edge and fell to the stone floor. When the drop hit the ground, there was an impossibly bright flash. A loud clapping noise echoed through the chamber. I let out a yell of surprise before cupping my hand over my mouth.   
“Who’s there?” the girl called out. “I’ll call the guards!”I cursed under her breath.  
So I decided on the direct approach. After all, didn’t i sneak in here to find the girl? Even if i wasn’t sure what she’d do when I found her. i stepped out of the shadows and faced the girl. “Hello.” 
The girl stepped back with a slight smile and a look of recognition. “You.” 
“I saw you in the gym,”  
“I remember. You’re the restricted family’s son.”I bristled at the remark. Was that all this girl saw? “What of it?” I snarled. 
“I’m sorry, I meant no offense.” The girl put her hands up. “That’s just how I remembered you. My name is elena.” 
my face relaxed slightly. “I’m damon.” 
“So what are you doing here,I said—” The sound of rapid footsteps approaching cut Elena off mid-sentence. “Damn! The guards. They must have heard the explosion.”“We have to go. They’ll be here any moment.”“Oh, so now it’s we, is it?” 
They left the chamber and entered a long stone hallway that stretched in both directions. When I had followed Elena in here, she remembered entering from the left. But now the sound of footsteps came from that direction. 
“Can’t go that way,” Elena said. 
Footsteps echoed in all directions through the hallways. It was nearly impossible to tell where they came from. I pointed to a tiny alcove on the side of the hallway, covered by the banner of the Great Citadel Library.The two of us crammed ourselves together and hid behind the banner.  
the sounds of clattering footsteps approached. And then passed right by us. It worked. The guards didn’t see us .  
Without a sound, both  left their hiding spot and ran in the opposite direction of the voices. As they fled, I tried to get some answers.“Why are the guards after you? Are you not allowed here?” 
“It’s not who I am, but what I was doing. I’m not allowed in the alchemy chambers. Few are.” 
Once again, the guards came from both directions.“Quick, this way.” Twenty feet above us, sunlight shone through high windows.“I can climb up to those.” I pointed to the windows above.  
The sound of footsteps echoed down the hall. “There’s no time. Please. Take this to the Moonlight Tavern.” she pulled out the vial of light amber liquid and handed it to me. “Give it to Benjin only. No one else. Ask him where the nightshade grows. The answer is under the lilies.” 
my head spun  
“I’ll do it. Be safe.” I turned to the wall to scale it.Then Elena called out. “I forgot to give you something.” 
“What—” I was halfway through the word when Elena ran over and kissed me.  
“Goodbye.” I waved and scaled up the wall with agility and grace. In moments, i was at the top, heading out the window. i paused at the top to look back. my heart sank as guards surrounded Elena and forced her to the floor.  
Inside, the tavern was nearly empty; it was only half past noon. One patron sat passed out at the bar. 
The only other person in the room was a man behind the bar. He looked me over, then bellowed, “Come back when you’re older. Or richer.” 
“I’m here to see Benjin.”The bartender’s eyes became slits. “How do you know that name?”“A friend gave me something to deliver to him. man said  “My name is gunthur. But in the Shadow Guild, I go by Benjin.” 
Where does the nightshade grow?” I asked, remembering the pass-phrase Elena had told him.Benjin’s eyes flashed in recognition. “Under the lilies.” 
He took the vial out of his pocket and held it out. “The Citadel Guard captured Elena. she told me to give this to you.” 
Next day I hid in the shadows. i studied the guards’ movements, listened to their conversations. Finally, after several weeks, I overheard two guards talking. Elena was to be moved to face judgment before a magistrate. They’d transport her by secure carriage. This was the opportunity I had waited for. 
The attack came swiftly. I swung down on a rope from the treetops and placed a drop of the amber liquid on to each of the rear wagon wheels. As the wheels spun around, an explosion rocked the forest. The guards’ horses bolted in different directions, leaving their riders as hapless passengers. 
Speaking through the bars, I called out to Elena. “Get to the back of the carriage.” 
Elena beamed. “Anything for you, my dear damon.” 
I then took one last drop of the amber liquid and placed it on the large iron lock that barred the carriage door.  
Elena emerged from the carriage and ran into my arms.  
I pulled away. “We should go before the guards return.” 
With that, the two of us ran into the forest. When they were safely away, they stopped and looked at each other. 
“Thank you for not giving up on me,” Elena said with a wide smile.I returned the smile. “You gave me something at the library. I want to return it.” 
Then I kissed her. 
""")
text_area.configure(state ='disabled')

btn1= Button(
    win,
    text = "Back to index",
    height = 5,
    width = 50,
    padx = 20,
    command=index,
    fg = "#850101",
    activebackground = "#850101",
    activeforeground = "#ffffff",
    pady = 10,
    ).pack(side = LEFT)

btn2 = Button(
    win,
    text = "Back to 1st page",
    height = 5,
    width = 50,
    padx = 20,
    command=Back,
    fg = "#850101",
    activebackground = "#850101",
    activeforeground = "#ffffff",
    pady = 10,
    ).pack(side = RIGHT)

back = Button(
    win,
    text = "Back",
    height = 1,
    width = 15,
    padx = 20,
    command = Back,
    fg = "#850101",
    activebackground = "#850101",
    activeforeground = "#ffffff",
    pady = 10,
    ).place(x = 1350, y = 0)

#Darkmode Button

DRKMD = Button(win,
               height = 2,
               width = 15,
               pady = 3,
               text = "Toggle Darkmode",
               background = "white",
               foreground = "#850101",
               command = DarkMode,
               ).place(x = 1100, y = 0)

win.mainloop()