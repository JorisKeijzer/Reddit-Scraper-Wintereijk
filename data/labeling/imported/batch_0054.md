# Label-batch batch_0054

## Instructies
Je bent een marktonderzoeker voor een Nederlands e-commercemerk dat koperen inlegzolen gaat verkopen. Je codeert Reddit-threads over voeten, voetklachten, schoenen en inlegzolen volgens een vast codeboek.

Regels:
- Citaten (quotes.text) zijn ALTIJD letterlijk en exact uit de bron overgenomen, inclusief spelfouten. Nooit samenvatten, vertalen of verbeteren in dat veld. nl_meaning is een getrouwe vertaling, geen reclametekst.
- Codeer alleen wat er staat. Verzin geen beroep, diagnose of situatie die niet genoemd wordt; gebruik dan null of een lege lijst.
- Scheid eigen ervaring (first_hand=true) van advies uit de tweede hand, diagnoses door vreemden en reclame van fabrikanten.
- Neem ook tegengeluiden en negatieve ervaringen mee: wat NIET werkt is net zo waardevol als wat wel werkt.
- Noteer elke vermelding van koper, magneten, acupressuur of reflexologie, ook sceptische, in 'copper'.
- Een Reddit-reactie bewijst geen klinische werking. Zet claims_risk op 'medical' bij aandoeningen of behandelclaims, 'material' bij materiaalclaims (koper, antibacterieel, geur), anders 'comfort_only'.
- medical_red_flag bij diabetes, neuropathie, gevoelloosheid, branden/tintelen, infectie, (stress)fracturen of ernstige zwelling.
- marketing_insight_nl is een hypothese voor ons merk, geen feit; beloof daarin nooit genezing of pijnvermindering.
- Is de thread niet over voeten/schoeisel/zolen (bijv. een toevallige zoekmatch), zet relevant=false en houd de rest minimaal.

## Opdracht
Label elke thread hieronder volgens het schema `ThreadLabel` in `vocscraper/schema.py`.
Schrijf het resultaat naar `batch_0054.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: graeri, 115kv1k, 1vdqknx).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD graeri ===
SUBREDDIT: r/TalesFromYourServer
DATUM: 2020-05-27  SCORE: 2019  REACTIES: 200
TITEL: Manchild threw 3 large drinks at my feet in front of his wife.
POST (source_id=post):
So my restaurant is a notable chicken place here in the south known for shitty homophobic practices but damn fast service and good food.

I had been walking food out of our delivery door (we have a fancy automatic door instead of window for drive through) for 7 hours in 90 degree heat serving 200+ cars an hour when our star, this balding 40 year old jackass, pulls up blocking other customers from exiting.

"I got the wrong drinks!" I quickly ran to his car to help and handle things the "Unnamed Homophobic Chicken Sandwich Joint with Really Fast and Good Food"TM way with politeness and apologies.

I started to tell him we'd happily replace his drinks for free and he could keep those but he interrupted me gesturing the cup carrier at me and loudly cursing how they were wrong and he didn't want them.

"Oh I'm sorry sir we can't take anything back from customers due to our health policy but I'd be happy to-"

"What the fuck, well i don't want these god damn drinks"

"Yessir I understand but I'm not permitted to take anything back from customers, I'll happily give you-"

"Well this is fucking bullshit I'm not keeping these"

he then proceeding to - one at a time - take each LARGE drink out of the cup holder and throw each one at my feet, his wife saying something along the lines of "Oh sweetly no, honey" the whole time.

If there is one god damn thing I am good at at my job, it's staying calm and polite in front of human degenerates like this. I kept my composure and let him throw all 3 drinks before looking back up at him.

"Well sir if you had let me finish I was going to inform you I'd be happy to give you your proper drinks for free. What were your drinks again?"

He kinda stopped for a second cause i assume he was expecting a reaction from his childish tantrum, but sunk cost fallacy had him quickly back to raging.

I went to grab his proper drinks and my co-worker stopped me from taking them so she could take them and give him the most passive aggressive "Have a blessed day, sir." I've ever been fortunate enough to witness.

I' lucky to have some great co-workers who helped calm me down afterwards, though I didn't show it my heart was going 150bpm and I was god damn fuming. I so just wanted to ask him "You're an adult, right?" in a calm voice and see what would happen.

There is no moral to the story or happy ending really, fuck customers and fuck the manchild who threw his only 3 brain cells out his window with those 3 fucking drinks at my feet like a toddler. All in front of his poor wife.

Edit: took out my employers name at recommendation of commenter.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[frxs91p] (score 657, diepte 0) That is embarrassing for a grown man to throw drinks like a three year old. Loser.
[fry44w3] (score 455, diepte 2) One time I had a woman like that, in a sit-down restaurant. Her husband just looked like he had been through hell and back. I kept expecting him to try to blink a morse code message for help.

At one point, the wife went to the restroom and I brought the man a complimentary  cocktail. He said he didn't order it. I told him I was aware of that. He asked me what it was for, and I said "I think you know, sir."

He smiled, I imagine for the first time in ages.
[frxu0k9] (score 443, diepte 1) Oh, it is WAY more embarrassing to be the woman sitting next to that three-year old grown up.  Trust me.
[frzrmhs] (score 217, diepte 3) I love people like you. I had a flight attendant do that for me once. I was leaving my husband and was an absolute wreck. I had my tiny little cat, my favorite little pet in the whole world in a carrier stowed under the seat in front of me. She didn’t make a peep the whole flight. 

A little girl across the aisle saw her and squealed and asked to see her. I told her I might let her have a peek after we were in the air. A woman in front of the little girl and by the window (one row and 6 seats away) heard the little girl say kitty and raised a HUGE stink about how she’s allergic and she demanded to be moved. I know people are allergic. I get that. People that are genuinely allergic don’t act like this bitch did. Most severely allergic people take a med or even a benedryl before cramming themselves on a plane where whey run the risk of animals and people that have been in very close contact with them. 

She Kept frantically pushing the button and talking about how her throat was closing up. Clearly it was Bullshit because she continued to get louder. She could breathe perfectly fine with those pipes. 

Her traveling companions kept shooting me apologetic glances, only confirming what I’d suspected. Even her husband said “honey, come on. You’re barely even...” They were trying to talk to her and get her to stop being so obnoxious. She acted like I had a bomb under there with the way she carried on. 

The FA’s swiftly handled it. They moved her up a bit (I was in the very last row, against the window in the hope I’d have as few people around me as possible.) 

However it looked like she was going to have to sit in a dreaded middle seat and she did not like that. Im pretty sure Karen was lobbying for a free upgrade. 

I couldn’t hear her anymore, but a no-nonsense type cabin crew member came over and spoke to her and she shut up. 

I stared straight ahead absolutely mortified, trying my damndest not to lose it and start sobbing. I was already as stressed out as you could possibly imagine that day and she just made it worse. I was beyond humiliated. People kept peering back to look at me and I dead eyed stared straight ahead at the back of the seat in front of me. 

The FA asked me if I would like a drink before takeoff. I assumed she meant water to calm me down so I said I was fine and gestured to the bottle of water I had. She leaned in closer and said “No..I mean something to *drink*, on me.” 

I asked for a whiskey and coke and bless that woman if she didn’t make sure I got as many whiskey and cokes as she could ply me with for the duration of that short flight. Thanks, Peg. You were the best.
[frztj68] (score 208, diepte 4) Those moments are what makes the job worthwhile.

My favorite moment was when I was put in charge on Christmas Eve. Because everyone who would normally be put in charge was taking the night off. Needless to say, I was a bit salty about that.

I was doing table touches, and spoke to a woman with her two teen kids. They gushed about how great everything was and said it was their family tradition to go to our restaurant every Christmas Eve.

I sometimes do something nice for a table like this, maybe send them a free dessert to say thanks for being a loyal customer. But for some reason I still don't fully understand, I chose to comp their entire bill. This was a steakhouse by the way, so that was a good chunk of change I would have to justify later.

About 20 minutes later, the hostess said I needed to go to that table right away, there was a problem. I rushed over and the mom was crying, wracking sobs, and the kids were trying to comfort her.

She explained that 5 years earlier, the Dad had walked out on Christmas Eve and she took the kids to our restaurant because she couldn't emotionally handle Xmas dinner in their house. That's how it became their tradition.

She had been laid off from her job two weeks before Xmas. She couldn't afford dinner in our restaurant, but she didn't want to ruin the tradition for her kids, So she was putting it on her credit card and was going to deal with the consequences later.

I was very humbled by the experience and grateful I had been able to help them at such a difficult time in their lives.


Edit: Thank you for the Gold!
[frxwzz5] (score 158, diepte 0) Whenever I see stuff like this it honestly just makes me sad for their spouse and kids. I work retail as well as fast food in the past and I've seen some shit but at least I only had to interact with that angry person for one interaction. Man imagine being their wife if this is a common thing she is use to dealing with that she can only sit back and quietly go oh honey not please honey don't. You know in some of these cases with these rage aholics there is some legit abuse going on at home. And sometimes the genders are reversed it's the husband whose super nice, quiet and apologetic. And it's his wife who is a total angry bitter Karen type that gets mad at the husband if he doesn't have her back.

&#x200B;

I wouldn't even make it to a second date with a person if they treated any person especially a server or customer service worker like this. Much less marry them and have kids with them. See ya asshole go ruin some other chicks life.
[frxu72i] (score 117, diepte 0) > but sunk cost fallacy had him quickly back to raging.

Well put.   I bet that's exactly what it was.

> All in front of his poor wife.

I now have you tagged as "perceptive and large hearted."
[fry7x0j] (score 114, diepte 1 OP) I 100% agree. Specifically to note on the reversed genders, that's actually often what I see. Like I said we're famous for our customer service and politeness so people - most often Karen's - do their god damn hardest to abuse our kindness.

Funnily enough about an hour before this incident, I had a car we had "Pulled"(Asked to move up a bit while we work on their slightly larger order) that tried to scam some drinks from us.

They had already received their drinks and I delivered them their food when the driver claims "Oh sir we're missing our drinks."

I found this very peculiar since I witnessed my co-worker hand her drinks to her. 

I asked "Oh, I'm so sorry, you didn't get them earlier?"

She and her passenger then looked around for a quick moment and she turned back and went "Nope no sir, no one ever gave us our drinks."

I apologized asked them what their drinks were - 4 larges - and walked back to ask my co-worker and yup, they should've had their drinks. My co-worker who gave them the drinks then went to go ask.

When my co-worker showed up, they were holding the drinks and then denied ever claiming to had lost them. Now they we're saying they payed for Larges but got Mediums.

Then she checked their receipt and nope they were rung up for mediums.

Unfortunately in situations like this where they claim they ordered something but got something else, we just give them what they claimed they ordered. It's quicker to do that than refund them and then pay them out for something new, all at the delivery window.

So my co-worker returned and we figured that they were trying to scam some drinks from us. Before we started making their new drinks - which would've left them with 4 mediums AND 4 larges - our manager overheard and told us to instead prepare 4 smalls to make up for their drinks.

They still got away with free drinks but instead of having 8 full drinks, they got 4 mediums and 4 useless smalls full of mostly ice instead of soda.

They were not happy.
[frxzrbq] (score 96, diepte 0) The best way to handle someone who has lost complete and total control over themselves is to act calmly. They’re just waiting for a reaction to use to further their agenda. 

When they walk away is when you wish they die in a fire. 

Good on you for playing it cool, and fuck that guy.
[frz0bkj] (score 73, diepte 2) Bless your manager for figuring it the best way to follow company policy while also making it clear to the Karens that their scamming ways aren’t going to get them what they want.
[fry4c7m] (score 70, diepte 2) Psychopaths can be very charming and engaging when you meet them. It's very easy to be taken in and not pay attention to the warning signs until it's too late. Then the psychopath gaslights you into believing you can't leave them.
[fry7izc] (score 62, diepte 0) My line I like to use in those situations is “May your day be as pleasant as you.” Used it on a GH driver the other day.
[frxwtyf] (score 59, diepte 1) Embarrassed would imply self-awareness.  It appears he's outsourced that to his wife.
[fry8lbg] (score 56, diepte 1 OP) Exactly, when you stay calm they either calm down themselves and see how ridiculous they're being (which is rare) - or they get even angrier cause this 8.50/hr teenage fast food worker won't act scared or shocked to your childish behavior.
[frz8u66] (score 55, diepte 2) Right? My man would have seen Jesus if he tried anything like that with me. I can’t believe his wife just let it slide

Maybe he’s just as much of a dick to her and she didint wanna catch the back end of his rage back at home 🙁
[frxv3y9] (score 55, diepte 0) His wife has seen much worse.
[fry8h3s] (score 44, diepte 2) Oh fuck off. Way to go, pinning the blame on someone who could very much be trapped in an abusive relationship. Manchild probably didn't start showing his true colors until after they married and divorce isn't as easy as signing a piece of paper.
[frzuzwm] (score 43, diepte 5) What an absolutely fantastic experience to have. I can’t even imagine how grateful they must have been. 

Good job, stranger :)
[frzwcem] (score 36, diepte 5) This made me tear up. I totally understand how that poor mom felt. Thank you kind stranger I really wish there were more people like you in this world.
[frz9hcq] (score 36, diepte 3) Which again, is even sadder. Poor lady. Maybe he was nice at some point? My attitude these days with customers who wanna act like that is more on the "I wish a mfer would" end of the spectrum lol
[frxs7gp] (score 35, diepte 0) I like that I knew the name of the restaurant without you saying it.
[frzbcwp] (score 35, diepte 0) There used to be this thing called "the right to refuse service" that would be enacted to keep the degenerates in their place but fuck corporations that out a dollar over the dignity of their staff. 

Unionize your workforce and fight for your dignity and a living wage.
[frzkupq] (score 34, diepte 2) It be the woman with the fucking patty melt guy. 

I came down to NC OBX a few years ago to visit. 2018 New Years? Had to be my dad had passed. And I had made up mu mind to leave my ex. My now ex was in a roll for patty melts. If we were at a sit down restaurant hat had burgers you best know his next question was for a patty melt. 

He had a fit at this tavern. He didn’t understand how they didn’t have patty melts. He asked if they had bread back there and the poor waitress was all yeah we use buns. And he got cocky and explained that he dosent understand how he can make a chicken sandwhich in the kitchen but not a fucking patty melt. He went in a mansolaining rant. I wanted to die. The rest of the table is looking at us like we’re ass holes and I’m looking at him like he’s an ass hole. I’m so glad I left him.
[frz728s] (score 32, diepte 1) Even sadder for his partner to just "oh honey no" him while watching
[fry985j] (score 28, diepte 2) I feel like there's a story here...
[frzf6kz] (score 27, diepte 2) i'm wondering what their situation is- probably not a good one. if he treats a stranger this horribly, i can't imagine he's kind to her. 

OP this sucks. i'm so sorry. why are some people so damn mean?
[frz7gc3] (score 26, diepte 2) Good...stop rewarding the assholes!
[fs01x8s] (score 23, diepte 5) Is someone cutting onions? 

Someone is cutting onions. 😢
[fs0f70j] (score 23, diepte 2) It’s a rule we have in place to protect our community members. Most corporations have monitoring software and the ability to track down those employees who shit talk them on the internet. Even mom and pop places have Google alerts. By prohibiting identifying information in posts, we are doing what we can to ensure TFYS remains a safe space to vent without fear of repercussions. 

Go after mods for actual abuse all you like, but try to apply just a tiny bit of critical thinking before you get all bent out of shape over reasonable guidelines.
[frz8k24] (score 21, diepte 1) Oh heck yeah. Remaining aloof, placid, and infuriatingly polite is the best way to piss off someone having a tantrum. I've used the "kill them with kindness" in retail a lot and I get so much satisfaction knowing I can make someone angry by simply remaining calm and kind. 
It's twisted, and fun.
[frybtpn] (score 21, diepte 0) I hate how customers can get away with treating us like subhumans and all we can do is smile
[frz8n5y] (score 20, diepte 2) A man that gets violent over a wrong soda (that would be fixed immediately) and starts throwing things is probably not using his coping skills at home. The wife probably gets the issues taken out on her, with force.
[frycjdq] (score 20, diepte 1 OP) It helps to focus on the little things, like how I know having lived 1/2 as long as this guy, I've most definitely felt more joy and contentness in my life than this miserable piece of shit ever has or ever will.
[fry95q5] (score 19, diepte 1 OP) Ooooo that's good, I might test run that and see if management gets pissed.
[fry97ks] (score 19, diepte 2) Oh and don’t forget the infamous Southern saying... Well bless your heart 😂
[fry62nk] (score 18, diepte 0) I wish there was a black list where you can add terrible customers like that. Have businesses in on it and refuse to service them.
[frz89mb] (score 14, diepte 0) I can’t wait until companies stop enforcing this kind of behavior by forcing customer service employees to take abuse with a smile.
[fry5s38] (score 13, diepte 1 OP) Unfortunately my work encourages bending over for asshats like this. Even my co-worker sarcastically telling him "Have a blessed day" would've been risky if a manager saw it.

It kinda sucks but also I've found staying calm is the best way to get back at these people.

Either they themselves calm down and though often don't apologize, they see how ridiculous they're being - or - they go into an even larger fit of rage cause this 8.50/hr fast food worker won't act scared or anything to their childish behavior.
[frxv3jl] (score 12, diepte 1) I thought you might me a place where you can get soda bread in a cask. But then I think you said the name and very politely acknowledged it was trademarked.
[fs0hewv] (score 12, diepte 4) Cat allergies don't make your throat close up!  That's food allergies.  Unless she literally took a bite out of your cat, that seems unlikely!  If she was allergic she'd have been sneezing.  

Also it's funny how she was just fine until she realized the cat was there.

I wish upon her the worst thing that has ever happened to me on a flight - to be surrounded by enormous farting tourists. 

(This happened to me once - I was in a middle seat surrounded by possibly the largest German tourists I have ever seen - each one well over 6'3 and built like a lumberjack, who had apparently been to some sort of beer and wurst festival.  Not only did they not let me have EITHER of the arm rests, they farted almost constantly and one of them broke my headphone plug trying to shove past me.  Oh yeah, and it was a ten hour flight.  It was the wurst!)
[frziypy] (score 11, diepte 2) There's also a time and place for innocently scratching your nose with your middle finger 😉

Also, the ever-popular "sorry, what were you saying? I wasn't listening" (if you like apoplexy)
[frzmfbw] (score 10, diepte 2) Abusive partners don't throw a punch on the first date.
[fs02u3d] (score 10, diepte 2) It varies situation to situation. Sometimes, people change *after* the relationship started, and it does take some time before people leave the changedassholes. I know I wouldn't leave my husband after one measly episode with all the history we have. Not even two or three. It would take a few problem episodes like the one OP had before I broke off a long-term relationship, because only then would I know it was too late for help. 

Sometimes, we catch people in that in-between stage, before they make up their mind.
(144 reacties met lagere score weggelaten)

=== THREAD 115kv1k ===
SUBREDDIT: r/bartenders
DATUM: 2023-02-18  SCORE: 136  REACTIES: 171
TITEL: Is there a level of fitness where you’re not in pain after being on your feet 10+ hours?
POST (source_id=post):
Or is it just not normal for a human to be standing that long? Wondering if it might be worth getting super fit and healthy to make these shifts easier on my body. Reaching 33 now and want to go as long as possible in this industry. Fwiw I am not overweight or particularly unhealthy. Just a thought that has been with me recently.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j92b2xp] (score 109, diepte 2) At the peak of my fitness, shredded, jacked, literally on drugs to make me perform and recover like a superhuman, I would still be fucked up from bartending. So no, it doesn’t get better.
[j92wu6g] (score 106, diepte 3) The shoe question is still relevant imo. You'd be surprised what a good set of insoles will do to help your back, neck, and shoulders
[j927v8m] (score 103, diepte 0) How are your shoes?
[j92hl26] (score 61, diepte 0) It's more about diet than fitness. 

Is it possible you're not drinking the recommended amount of Jameson?
[j92aysb] (score 51, diepte 0) I lift weights 5 days a week and have for almost 20 years. I bartended for 10 years and now I’m an electrician. I’m 42 and always on my feet. No aches. I don’t know if that’s what you’re looking for, but it’s the best I have.
[j9288hb] (score 47, diepte 1 OP) Changed feet to body in OP because it’s not just the feet, just the general body aches after a long day that is usual from most people from what I hear. Wondering if I can get shredded and overcome that 😂
[j928zjf] (score 39, diepte 0) Cycle to work. It gets you warmed up and eased out of your shift. I know it sounds insane. I also take a stretching break occasionally and feel ready to kick ass after 50yo
[j92dz5u] (score 30, diepte 0) Do you have decent bar mats? That always helps. Definitely stay hydrated. If possible move around a lot during your shift (standing mostly in one spot is really hard on the body). Personally what has been keeping me ache free (I’m 45), is working shorter shifts. My current spot keeps the shifts at 8 hours max. Of course that is not always feasible.
[j92ktty] (score 29, diepte 2) Shoes for leg pain, technique for upper body.

Work on your ergonomics.

Shaking more from the wrist than the elbow. Away from the ears, and more in front of the body. Organize your well and garnishes so they don't require excess movement across your body (and work on ambidexterity). Stretch before the shift. 

Those are all adjustments that can vastly help with the physical toll, and definitely something we don't talk about enough.
[j92h5xq] (score 28, diepte 0) Compression socks!! 
I’m a nursing student and a bartender so I consistently do 12hr shifts standing and compression socks are a game changer (and your legs will thank you in the future) 
Also good shoes
Stretching before and after work! I try and take 10 mins when I get home (and after showering) to just do some simple stretches before getting in bed
[j936ock] (score 25, diepte 4) Al Bundy over here
[j92q92f] (score 23, diepte 2) You can absolutely get a DUI on my bike my friend lmao
[j92cguu] (score 22, diepte 3 OP) This is EXACTLY the answer I was looking for. Thank you friend!
[j92we11] (score 19, diepte 3) I agree... 41, 10 years in military and currently best shape of my life.... Tonight is going to destroy me.
[j92ep4d] (score 19, diepte 2) Core and back strength is the name of the game. People often focus on the latter and ignore the former. Also yoga or some other form of stretching routine is important as you get older
[j93cnf2] (score 18, diepte 4) Try wearing compression socks religiously. And keep up with your lower body health. That includes stretches and warm ups before shift.
[j92vka0] (score 13, diepte 4) Yeahhhh but that’s a bit of a detour for me to get back to LA
[j928ojx] (score 12, diepte 2) Ahhhh gotcha. Maybe yoga or a stretching routine would help. I hope you can find something!
[j93mv40] (score 12, diepte 1) Picklebacks have electrolytes
[j92eybf] (score 11, diepte 0) I’ve been bartending for 7 years, in the past year Ive lost about 50lbs (230ish down to 180ish…Im also 6’5”) and lift about 3-5 days a week and my back pain is gone, also my legs don’t seem to get as sore anymore. I think being lighter and having more muscle strength has really helped.
[j92edwo] (score 10, diepte 2) I’m 34 now. Been tending bar since my mid 20’s. I gotta say that you need to go to the gym. Guys younger than me drop likes flies due to back injuries behind the bar. Once a man hits his 30’s his back is basically an injury waiting to happen.
[j92wm9c] (score 10, diepte 1) You are my spirit animal.
[j9282n8] (score 9, diepte 1 OP) Nah the shoes are great, good suggestion though, first thing I flag with my other bartenders if they’re indicating a larger than usual pain level.
[j928xes] (score 9, diepte 2) Nah man, it's the shoes. It's normal to feel tired and not have a lot of energy, but if you are in actual pain after a shift... Either bad shoes or you're doing something wrong to your back.
[j92j5e3] (score 9, diepte 1) Edit- no DUI’s feet and me knees never hurt
[j92drvy] (score 9, diepte 1 OP) It is what I’m looking for thank you! Trying to figure out if its an age or lifestyle thing since it only kicked in in my 30s. Looks like I’ll have to pick up my health game!
[j92q4o4] (score 8, diepte 4) It might be the insoles. My back was pretty effed up from bartending until I switched over to super feet green, made sure to change them out every 4 months


It’s the bar mats and your insoles.
[j934m25] (score 8, diepte 2) TRUTH! dude posture is everything, after a gnarly shift i would be convinced that my lungs were about to collapse. Amazon  has posture braces and get yourself a pair of old man looking sketcher super support shoes and its been a game changer.
[j92adaj] (score 8, diepte 0) Superior running shoes with insoles. Also only drink on off days and workout 3-4 days weekly and drink 3L of water daily min.
[j933xg6] (score 7, diepte 3) 100% stretch before your shift. Work is a workout. Warm up for it. It makes more of a difference than you'd expect.
[j93noal] (score 7, diepte 1) This is key, and a lot of people overlook it. I worked for awhile in a bar that had cement flooring and no mats. That is the only job I worked that fucked my back and legs up.
[j92gss5] (score 7, diepte 0) Fwiw, I just moved out of bartending (Cook before that, now a manager), working in a high volume cocktail bar - 2 bartenders doing 7-9k in liquor (not including wine and beer) per night. I run ~12-15 hours a week (6 days) and workout 2-3 times a week, and cycle twice a week. Being fit drastically reduces the discomfort at work but you trade it for a huge amount of physical investment outside of work and general muscle soreness on a regular basis.  
  
Being physically fit will significantly raise your baseline. You will feel better overall. You don't need to be ripped with an insane six pack or muscle definition, but being active outside of work will do wonders for your physical longevity. You have to want it though. The motivation to stay active is the hardest part. I enjoy running in the mountains in the summer. I have big plans for summer that keep me motivated all year round. Find motivation and the rest is easy.
[j9581vu] (score 6, diepte 5) That last bit is the hardest to achieve. A decade in the industry and I can’t bring myself to stretch before any shift.
[j94fdkh] (score 6, diepte 3) hard same. no-slips with support go a long ways but fuck, 12 hours moving on your feet is gonna hurt no matter how you cut it.
[j937hjo] (score 6, diepte 1) Cycling to work = the best thing.
[j930s8k] (score 6, diepte 0) Yes. It's called being in your early 20's.
[j93mh4l] (score 5, diepte 5) Working without bar mats can make the pain add up after the years.
[j944i14] (score 5, diepte 4) I think there is always pain with that kind of work but shoes with excellent arch support (I like Vionic Orthoheel) and knee high compression socks can make an improvement.
[j9515zd] (score 5, diepte 3 OP) I’ve got the hokkas. Great shoes. Worth the price imo.
[j929ygp] (score 5, diepte 0) no matter how fit you are you will need light movrment and stretches to stand this long, also most people dont really train their feet specifically, even more with regular shoes that have insane padding
[j92az52] (score 5, diepte 0) I am very active during my shifts and I’m never aching or in pain after. Tired? Yes. 

Do you take care of your fitness outside of work? I started going to the gym before work every day and it’s done wonders for me.
[j92gz4c] (score 4, diepte 4) Good luck to you and your body
[j94zfa1] (score 4, diepte 2) Shoes still matter for that. I started walking straighter and having better body posture once I figured out exactly what length and width I needed. I was wearing too long and too narrow forever. My feet were always squeezed on the side, yet slipping forward with each step.
[j9538qj] (score 4, diepte 2) Vionic are my choice. I also like Kuru which are specially made for plantar fasciitis. Too many years of long shifts standing on concrete did me in.
[j92udi7] (score 4, diepte 1) Congrats on the weight loss!
[j934afg] (score 4, diepte 2) Username checks out
[j93lfga] (score 3, diepte 4) You're so adamant about the shoes. Can we get a pic?
[j92yrfa] (score 3, diepte 3) Ive found that the fancy looking shake mechanics are the worst for my wrist and hand (hand has been broken a few times and has permanent soft tissue damage) so my shaker moves look lazy AF but it still get the job done. Gel inserts in the shoes save my feet quite a bit (i work 10 hr shifts normally). 

You are correct, shoes/orthotics for leg/feet and technique for wrist/hands.
[j93mdaz] (score 3, diepte 4) My shoulders are pretty messed from a decade of shaking. I have a suspicion riding fixed gear brakeless didn’t help much either, the way you tense your body to skid.
[j94z8vl] (score 3, diepte 2) When I first started my job where I commonly work 12-13 hour double shifts, I would be in PAIN at the end of the day. Not just my feet but my knees, back, legs.. everything. I didn’t realize how important GOOD shows AND insoles are. Now my feet and legs are a bit sore after a double but nothing how it was. It was shocking to realize how much your shoes impact your entire lower body. I got insoles off Amazon & new balance non slips. Most of my coworkers highly recommend the hoka non slips, with the crazy large sole, but I’m not about to drop $200 for a shoe rn.
[j965k1j] (score 3, diepte 4) Focus on balance exercises.  Build your supporting and fast twitch muscles.  The big ones don't do you any good if they aren't supported.
[j92v9xs] (score 3, diepte 3) Not in Canada! :D
[j93yj8b] (score 3, diepte 5) LA is the only place where I've heard of my friends getting DUIs on a bike
[j93yqfo] (score 3, diepte 6) Went to college in Kentucky and my friend got 2…. On a fuckin bike XD
[j92egzr] (score 3, diepte 3 OP) Gym it is! Thank you for the advice.
[j92f2vs] (score 3, diepte 0) Howdy! all my degrees are in exercise science.  I haven't read any of your replies yet and I will here in a second but feel free to message me your general complaints and your specifics and maybe we can figure something out
[j92fezm] (score 3, diepte 0) Working on concrete sucks. New boots every few months and rubber mats help. Stretching and rolling helps too, invert legs up the wall after a long shift, some massage slides for around the house. 30+ Not as fit as I was before covid, and my legs are crushed by the fourth/fifth shift in a row. Try to work only 3 on in a row. Drinking makes it worse too. Lots of water and bananas help with tight muscles. Don't get old.
[j92g5yn] (score 3, diepte 0) Just a theory of mine, but a very strong foundation will do wonders. I'm a big man who can stand to lose some # and am in the process of doing so.

But even with weight loss, im still a behemoth. Because of my body type, my legs and calfs are very muscular. You dont skip leg day when you a big man. I'm a few years older than you, and I'm doing OK so far. My body creaks, but I'm not sore after work. 

My suggestion would be if you do work on yourself. Legs should be your focus. Also, another small suggestion. Examine your footwork, and I found I am more agile than i used to be than in my younger years. learning more efficient movements, almost dancing behind the bar.
[j930cw6] (score 3, diepte 1) In my country we have a saying that goes “one drink for each leg”. Basically means that you should always take to shots so you can “stand more comfortably”
[j92jrl7] (score 3, diepte 0) Quality insoles changed my life. I wear semi-stylish converse and people always ask if my feet hurt, nope!
[j92plt8] (score 3, diepte 0) - **Give your feet a massage in the morning and after a shift**
- Wear good shoes
- Monitor how you stand and don’t lock your knees, stay on the balls of your feet, roll out your ankles every so often 
- Move with your “whole body engaged”
- drink mostly/only water on your shifts 
- Eat anti-inflammatory foods
- Stretch after a shift
[j92s923] (score 3, diepte 0) Yes. I’ve been bartending for about 4 years now, but from 20-27 I was a tech with Mazda. When I first started at the dealership I was ALWAYS sore, but I also weighed 140lbs at 6’ and had very little strength. I started hitting the gym when I was 22-23 and noticed a massive difference in how my body felt after only a few months. I’ve been going to the gym regularly for about 8 years now and I’m verrrry rarely sore after working my Thursday-Sunday shifts. I’d recommend starting with a program like Starting Strength or Stronglifts 5x5, those compound movements get your strength up very quickly and sort of mimic the movements you’ll be doing at work (changing out kegs, picking shit up all the time, bending down to grab things off of lower level shelves/lowboys, etc.)

Plus, you’ll feel better naked.
Edit: Also, be smart. Wear proper footwear, make sure you stay hydrated throughout your shifts, do some stretching when you think of it, eat healthy foods, all of that good stuff. Going to the gym can only do so much if you aren’t helping yourself in other ways.
[j92uc42] (score 3, diepte 0) Morning karate classes. I go to a 10AM class, no matter how tired I am. It gets your blood pumping and your muscles stretched.

Edit:  I’m in my 40’s.
[j92yybt] (score 3, diepte 0) Late 20s been in the industry little over 10 years. Recently taken up doing 10 minutes of yoga every morning and night which has helped me tons with the 8-10 hour shifts. Still get sore if I’m on a double doing a 14-18 hour shift, might try and do a middle of the day yoga for those ones. Ultimately I don’t think the human body is built to handle it but we do what we can with what we’re given. Hope this helps!

Also I’ve been fit and active but not jacked for most of the 10 years
[j9348dd] (score 3, diepte 1) Fr
[j92dz2o] (score 2, diepte 3 OP) It’s not the shoes, just trying to figure out if its an age or a health thing since I was good to go all through my 20s despite a worse lifestyle. From the comments it definitely seems like a health thing! Might have to pick up my stretching/warmup game.
[j9490vy] (score 2, diepte 2) Oh, I see you are wearing proper footwear. Nice work.
[j94tnki] (score 2, diepte 5) Vionics, either the insert or a shoe, are worth every penny. I will also compression sock sometimes and like Comrad for those.
[j94423c] (score 2, diepte 2) I do not work out much, pushing 40 and work 36 hours a week on my feet I don’t normally have foot or back issues (full transparency I do have knee issues but that is because of a torn ACL from long ago) but I do buy quality shoes and insoles. I don’t know if I am just very fortunate or if it is the quality of the footwear either way I hope you figure out away to rid yourself of this issue
[j948y9m] (score 2, diepte 2) Okay, same question. Your shoes affect more than your feet.
[j95vetn] (score 2, diepte 2) What you're wearing on your feet can have an effect on your whole body.  If you don't have support it can fuck with your knees, hips, and lower back and the resulting tension can affect the rest of the muscles around your spine.

Besides that you don't need to be shredded but you do need mobility(flexibility) and stability. Yoga would be more useful than lifting or cardio though ideally they are done in tandem.

Also hydration.
[j93itx9] (score 2, diepte 1) Any suggestions for shoes? I have to special order my size
[j94l78a] (score 2, diepte 1) I'm gonna second this question. Shoes can make a difference in your whole body through a shift. I can't tell you what a night and day difference it is after a shift with the right shoes. I can feel the difference all the way up to my shoulder blades. Redwings have been my go to for years but there are tons of options out there.
[j928gwb] (score 2, diepte 1 OP) Sorry for not being clearer, my shoes are great and I’m talking about the general aches and pains from a long hard day. Feeling like it’s probably just the way it is working these hours, but somewhere inside me is hoping I can get shredded and not be afflicted by it anymore 😂
[j9294e1] (score 2, diepte 2) Fair play, maybe it’s just what happens after living the vida for a while. Maybe we should all be limbering up before long shifts
[j92z8k4] (score 2, diepte 3) Heavily dependent on where you are
[j930876] (score 2, diepte 4) Which is why it’s important not to say “no DUIs”… people don’t look into shit sometimes and just trust what a Reddit comment says
[j93eb42] (score 2, diepte 2) California is one of the few places in the world and it’s technically nothing like a normal dui, just a misdemeanor
[j92a6x5] (score 2, diepte 0) Stretch more, and go for periodic massages. My gym has a steam room that does wonders once a week or so. 

The body gets stiffer with age if you dont take care of it.
[j92yv4y] (score 2, diepte 2) Thank  you!
(90 reacties met lagere score weggelaten)

=== THREAD 1vdqknx ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2026-08-02  SCORE: 61  REACTIES: 162
TITEL: Just a server with severe foot pain after every shift, no matter if it's a single but especially after a double. I'm in search of non slips with a wide toe box and high arch support.
POST (source_id=post):
# Hi. I have been in the industry for almost 10 years, my horror story is how bad my feet hurt after every shift that I wake up to them still in recovery and have to hop on over to work before they had time to fully chill. My issue is that I keep getting Walmart shoes that have absolutely no support and kill my feet immediately. But my issue is also I keep getting shoes with absolutely no arch support and that are too narrow because if I get wides the whole shoe ends up being wide and are loose on my entire foot. So I just need a good arch support with wide toe box. Please help a girl out and drop your holy grails!!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[p1b7db4] (score 73, diepte 0) if you’re okay with the look of clogs, Danskos are absolutely amazing. i got the recommendation from a nurse who’s on her feet 12hrs a day and she said what a godsend they were for her so i tried them out and absolutely fell in love. 

they’re not super cutesy or fashionable but they have proper arch support and are extremely comfy and are also nonslip.
[p1b755c] (score 24, diepte 0) Insoles
[p1b7vde] (score 20, diepte 0) Hoka Arahi SR, they have stability, slip resistant, high quality, and insane cushion. Expensive but last well over a year.
[p1bleh4] (score 17, diepte 2) Not many shoes will hold up to 8 months of restaurant work, you need to get a few pairs and rotate them.

Feet sweat something like 250ml a day, so if they don't get a day to dry out it makes them break down even faster.
[p1bg0rz] (score 17, diepte 0) Hoka makes a slip resistant shield with a wide toe box and best arch support you can find. They are an little bit of an investment, around $150, but they last for a long time. Only shoe I found that let me consistently be in and out of kitchens for the 12-14 hour shifts.
[p1b7vpj] (score 12, diepte 0) Danskos changed my life.
[p1b9uha] (score 12, diepte 0) Sketchers have a line of wide & extra wide non slips.  If you can find one of their outlet stores in person, you’ll find something comfortable.
[p1begk8] (score 11, diepte 1) Yeah i really loved my vans from that line and the look was prefect for a casual restaurant but after 7-8 months the support was shot
[p1bfuv0] (score 9, diepte 0) You have to buy Hoka Bondi. They make a slip resistant. It's been life changing for me. Been wearing them for years now. Also, make sure you're stretching plenty. Not just legs, but hips and core, and definitely anything that can stretch your Achilles. But the Hoka Bondi is exactly what you're looking for.
[p1befic] (score 8, diepte 1) Exactly what i came to say. All my coworkers clown on my grandma clogs but I'm the only one not routinely bitching about sore feet/knees/hips so like...
[p1bgozv] (score 8, diepte 2) and people don’t realize the repercussions of not supporting your feet! seriously, in ten years your back will thank you and those who clown on us will likely have persistent lower back pain that could have been prevented
[p1bccc0] (score 7, diepte 0) HOKA BONDI NON SLIPS . Life changer
[p1bkcc3] (score 7, diepte 0) Just wanting to put a shout out for stretching before and after work! I have all the shoes- but what works best is if I’m stretching & working out everything lower body related: feet stretches and exercises, calf stretches, quad, hamstring, all of it. The foot that has pain for me is significantly weaker and exercises and stretching help keep it at bay
[p1bts34] (score 7, diepte 0) Not a shoe suggestion, 

But, from personal experience.

If you’ve given yourself Plantar Fasciitis no shoes are gonna fix the pain. 

If you have terrible arch and heel pain and lower leg weakness look into plantar fasciitis treatment.
[p1b7xfp] (score 6, diepte 1) #Facts.
[p1br1da] (score 6, diepte 1) Bondi has a wider toe box and also has SR. My high arches and spread toes prefer them over the Arahi.
[p1cmzv9] (score 6, diepte 2) Me and my plantar fasciitis ride at dawn for the bondi SR
[p1bdsmu] (score 6, diepte 1) Danskos are not wide
[p1baf1f] (score 6, diepte 0) I hate to admit it, but Sketchers cured everything.  Feet arches, ankle fatigue, and calf pain. Maybe just me
[p1cu5en] (score 5, diepte 1) I second this, but with the modification to try different insoles. All feet are different. There are different types of foot pain, and there are different types of insoles. Finding your ideal insole can make nearly every shoe better (a friend in highschool had shoes that distintegrated as he turned on the ball of his foot, so he just kept spinning on his feet Michael Jackson-style because it was too funny. This shoe would not be improved with insoles. Lol.).


Also, where is the pain? If it's plantar fasciitis, you should incorporate stretches and tennis ball massages to your daily routine. Other types of foot pain can also be relieved with daily stretching, range of motion exercises


Also, there are types of foot pain that are caused by posture and how your feet compensate for your spine, hips, and knees. Consider these if the insoles and stretches aren't providing you with relief.


Take care, OP. Foot health and mobility are things we don't notice until there's a problem. It's better to take note and avoid problems.
[p1ba02p] (score 5, diepte 0) I tried lots of shoes and inserts. My boss gave us all OnClouds as a bonus. I can go 8+ hours without foot pain. Just wore them yo NYC and was able to walk 12-13 miles a day.
[p1bfv0k] (score 5, diepte 0) HOKA Biondi or Oofo clogs. Both are mightweight with great support. 

Working 12 hour shifts in the hospital on cement-hard floors these were the only shoes that didn't make my feet hurt.
[p1blhwx] (score 5, diepte 0) Merrell and New Balance both make work shoes that are great.
[p1bhlfv] (score 4, diepte 0) Hokka Bondi black non-slip. I am a chef with osteoarthritis in my feet and toes. Anything with a stiff arch like Dansko and Birkenstock were a big no for my feet
[p1bk90w] (score 4, diepte 0) Workboots. Actual workboots from the likes of Red Wing, Irish Setter, Danner, Thorogood, any of the PNW brands (if you can swing the initial investment), Ariats work line, Double H... 

Clogs are horseshit. Sneakers are horseshit. Crocs will get you sent home in any restaurant I've ever worked in. Anything sold by Shoes for Crews is horseshit. 

I'm partial to the Irish Setter lace-up Marshall's, myself. Nice wide square toe, better nonslip than any kitchen or restaurant shoe, steel toe that isn't particularly heavy, decent support out the box.
[p1bvlj2] (score 4, diepte 1) This is all just terrible advice. 

Id love to know what kitchens will send you home for wearing crocs that you'll find in any Michelin star kitchen but let you wear a pair of lace up cowboy boots essentially with a workbook sole.

None of them look more professional than a pair of crocs in a kitchen setting, you'd get laughed out of any kitchen turning up in a pair work boots laced up to your calf.

I've literally never even skidded slightly in my bistro pro crocs, they weigh 4 times less than your setters (walking round all day with an extra 2kg is insane) I have actual ankle mobility, and they actually have a wide toe box, not some weird square shape that's not natural. 

Plus they cost like 5 times less.
[p1dnqs5] (score 3, diepte 3) This is so key.  But also really hard to find the money starting out.  Once you have 3-4 pairs then you can just buy one every six months and keep switching out the oldest pair.  I got an engraver so I could put the date in the sole of my shoes so I always know which are oldest..
[p1ccf6n] (score 3, diepte 1) Yep when I was an RN on the floor I religiously wore Hokas. Still have them and wear them for exercise even though I have a desk job now
[p1b7y9h] (score 3, diepte 0) ive never been a croc fan, but the last 3 years my feet (especially where the toes begin in those joints)  just hurt in normal shoes (i also need a wide toe area) and i have a high arch in my feet and these make my feet feel so much better after a shift. little to no fatigue.   
i like how they taper to my heel and dont slide.

The only downfall I found with these shoes is they make your toes really sweaty. There is literally no breathing for your toes.
[p1ds58v] (score 3, diepte 1) Love my On so much I bought 2 more pairs after I wore the first pair out from 2.5 years of non stop wear. Getting my fourth pair soon. They weigh next to nothing and fit my feet like a hug.
[p1bn5fd] (score 3, diepte 1) I was going to say that Skechers have been EXCELLENT for me. I'm a CNA who's worked in food service in the past. 

The nice thing about Skechers to me is that they have a wide variety of widths and styles, even in their non-skid line. You may need to buy men's if you're a lady, depending on how wide your feet are, but they'll have something that works. They also have stuff with higher and lower arches, which is wonderful. Look for the max cushion versions.

Combine them with a quality insole for your specific foot issues and you're golden.
[p1blzt9] (score 3, diepte 1) Postal carriers swear by Hokas
[p1bmkps] (score 3, diepte 3) Some are and some aren't...
[p1bjx1m] (score 3, diepte 0) Super Feet insoles. I had so much pain in my feet and heal saw a podiatrist. Rather than expensive custom orthotics it was his recommendation to start. Life changer. Take them when you get new shoes so you can adjust sizing to let them fit in properly.   
Good luck.
[p1br8f2] (score 3, diepte 0) Morning soreness is a classic sign of plantar fascitis. Google exercises to do for this. I had the same issue and just doing 5 minutes of these a day has totally changed the gake for me. For reference, I get about 25k steps per shift.
[p1c3psp] (score 2, diepte 1) Second the Vans for makers.   
I just got a pair and they are really comfortable
[p1d43u2] (score 2, diepte 1) O they make em super cute now!
[p1dicte] (score 2, diepte 1) danskos are great as long as you’re not tall and doing prep on tables that are already too short for you… when i wear them my feet/legs feel great but my shoulder pain is a 10/10
[p1divqi] (score 2, diepte 1) barista lurker seconding dansko clogs ! my mood is genuinely 10x better during/after a work day, when I am wearing supportive shoes 😅
[p1dm0j9] (score 2, diepte 1) Danskos will also last a really long time. So comfortable, too.
[p1e6i9d] (score 2, diepte 1) Hokas are also good i dont know about non slipness. Theyre expensive but worth it is what some nurses have told me. I also find trail shoes surprisingly good if youre on your feet a lot merril is my beloved for that I have yet to sprain anything in them (I am fragile so thats surprising and a ringing endorsement) and have had them for 5-6 months and wear them whenever I leave the house the more thick ankle height ones are the ones I have. i dont know about nonslippness for those either but trail shoes are made for mossy rocks.
[p1dpfed] (score 2, diepte 2) Wide Danskos exist and are available for purchase through many retailers. Look for the "Cm-size(Wide)" designation.
[p1bi1qo] (score 2, diepte 2) They do make some of the pro line in a wider fit. I have some with the closed heel.
[p1dp42l] (score 2, diepte 2) They totally have a wide option. I have wide ass feet and the wides were too wide.
[p1b7wz8] (score 2, diepte 0) Keens with a superfeet brand insole. You need to find the right size insole that matches up with your arch it does not line up with posted shoe size. I am shoe size 12 and i wear the size 13-15 copper insole.
[p1bhon9] (score 2, diepte 1) I’ve been wearing Keens for the past decade. New pair every 18 months to 2 years. The last two pairs both fell apart about 9 months each. Same type of work. Exact same shoe model both times. I switched to Brunt and I’m on about month 3 with them. The toe box isn’t as wide but they are holding up great, so far.
[p1biqrq] (score 2, diepte 2) Oh no. i am just over 2 years on mine and was about to get new ones. I will give them a shot still hopefully it works out.
[p1bec9j] (score 2, diepte 1) These have been my go-to the last couple years, I keep a pair of clogs at work if I have to do something to get my feet wet otherwise I rock these all day. I have a pair of the step-ins that are kinda basic and a pair that are similar but have a great heel cushion. I haven't tossed a pair yet over two years.
[p1cls62] (score 2, diepte 1) Came here to recommend this! And specifically, a pair  in a men's size rather than women's-- this gives a wider toe area without the entire shoe being super wide
[p1equz0] (score 2, diepte 1) Yep this right here. I hate clogs, they are too heavy on my feet. I just need a good shoe. I went from sharp pain. Pins and needles to my feet just feeling good and normal after a 12 hour day.
[p1bmaiq] (score 2, diepte 2) They used to not "officially" be allowed by USPS.
[p1bmyzi] (score 2, diepte 4) Truth.
[p1brd82] (score 2, diepte 1) Wolverine has good sales on their website. Just don't expect the lace eyes to hold up that long, even my jeans bend em out of place and you can only push em back 4 or 5 times before they snap.
[p1fy6u2] (score 2, diepte 2) I've worn my work boots in a kitchen. It kind of sucked. I walk a lot though and adding a work boot to my foot didn't do me any favors. Maybe it would be different if I was standing in place the whole shift. I'm sticking with my super birkis for now
[p1bke7e] (score 2, diepte 0) I also have painfully high arches and a wide spread in my toes; I know you’re probably not looking for a name/outdoor brand, but MEN’s Merrell Trail Glove 6 (SIX, not the newer ones, and NOT the leather ones) have changed my LIFE.    

I’m on my third pair now, 1 retired and 2 active pairs in different colors.   Hated how women’s shoes were always pink or neon or something awful, noticed and tried a pair on at REI years ago— it was like floating.   It was truly the FIRST TIME that I put my foot in a shoe and felt anything other than a void under my arches.   

Whatever your shoe size is in women’s, go down 1 size for men’s.  I’ve tried the women’s— they just don’t fit the same.    And now that there are newer “models,” the 6’s are cheaper.
[p1bllpi] (score 2, diepte 0) Look at sketchers
[p1blqjz] (score 2, diepte 0) Im in uk and wear skechers work ones. They have arch fit and anti slip. They dont have anti ugly however.
[p1bn87v] (score 2, diepte 0) Orthotics
[p1bwemn] (score 2, diepte 0) One of the worst mistakes a restaurant worker can make is wearing the same set of shoes every day. If you're full time, you want to cycle through 3 pairs every week. Wearing the same pair will make them conform to your feet, and you'll lose any support. I was in restaurants for 30 years, you can trust me on this one.
[p1cdzuw] (score 2, diepte 0) Get compression socks. Nurses wear them for their shifts, makes a big difference.
[p1dgasg] (score 2, diepte 0) I’m on my feet a lot. Hoka Bondi 9 rescued my swollen, painful feet at the end of each day. They’re pricy, but less than a Podiatrist and custom arches. Or the Good Feet arches.
[p1eyurg] (score 2, diepte 0) Amazon sells shoe inserts. Type in the search plantar fasciitis shoe inserts and they’ll come up. About $30 but I now use these in every pair. I just worked two double shifts this weekend. My feet are sore but nothing like they would’ve been without the inserts. My feet were sore bad that I’m the mornings I’d have to brace myself along the wall and furniture to get out of bed.
[p1dt9ti] (score 1, diepte 1) Also consider one of the various Superfeet offerings.
[p1dpqqp] (score 1, diepte 2) Folks be hatin on Danskos in my above comment. My posture, health, and safety have all improved since purchasing them. 

The half dozen that I have purchased since I get a new, used, pair every six months.
[p1dteur] (score 1, diepte 2) > shoulder pain

See a physiotherapist?
[p1eb3qh] (score 1, diepte 1) Danskos for sure for your foot. They look nice with pants too!
[p1k6btg] (score 1, diepte 1) I have been using danskos for work since 2004. They do last a long damn time so they are an excellent value. I don't imagine I will ever switch over the life of my career.
[p1b7kyj] (score 1, diepte 0) Super feet inserts are great , keens are wide toe box . Some people dislike mise footwear but honestly I quite like them and they have inserts that are removable so your next shift if it’s the next day swap it out .
[p1c1pdd] (score 1, diepte 2) I’ve tried both and I much prefer the Arahi.
[p1eqq4m] (score 1, diepte 3) Same here!
[p1e0syb] (score 1, diepte 2) Better yet, get one of each and rotate.
[p1b97k1] (score 1, diepte 1) This is the correct answer
[p1c09um] (score 1, diepte 3) I think my problem is that they keep discontinuing the ones I like. I like low tops that look like sneakers. Im on the third “model” of this type and the latest model are the ones that failed twice. Maybe some of their core shoes do better. I reached out to them about my failed shoes and got fuck all in response.
[p1b8geq] (score 1, diepte 0) https://theinsolestore.com/collections/10-seconds/products/10-seconds-3810-ultra-arch-support-insoles

After working with a podiatrist on and off for years and two attempts using custom orthotics he turned me on to these about 10 years ago and they have completely changed my life. 

If you are not used to arch correction, they will feel very awkward and your feet are going to hurt after the first 3 or 4 hours, and they will absolutely kill right after taking your shoes off for about half an hour. 

Keep wearing them and stay with it though, and after about a week you'll wonder how you ever got on without them. 

They will outlast your shoes, I can run them through three pairs of shoes before I need to replace them.
[p1ba6i4] (score 1, diepte 0) Look up SRMax. They have all sorts of styles, and they all are non slips with good arch support
[p1bady9] (score 1, diepte 0) I work in food in a hospital and I surveyed several nurses about their favorite footwear. Hokas, Danskos, and I think new balances were at the top!
[p1bcbd8] (score 1, diepte 0) Dr Scholes custom orthopedic insoles they are like 50 bucks but work wonders
[p1bcl89] (score 1, diepte 0) I have high arches and bunions, so I need a wide toe box. 

I've been working with a combo of Brooks Glycerin sneakers and WalkHero inserts. I switch out the inserts every few months, if I come home sore.
[p1bfdhg] (score 1, diepte 0) My go to has always been New Balance, especially the men's 4E. (I am a woman) Get them from NB, not Shoes for Crews; the latter are NOT made as well.  I have recently discovered Fitwell brand online, not sure if they have any non slips.  They are some of the very few shows I can put on my spatulette feet and say ahhh. 

I also have prescription orthotics, which may or may not be covered by insurance, they are well worth the investment.
[p1bg6uy] (score 1, diepte 0) Danskos were too heavy and painful on my feet.
(83 reacties met lagere score weggelaten)

