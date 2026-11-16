# Label-batch batch_0056

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
Schrijf het resultaat naar `batch_0056.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: tcw9pk, 1khag9j, umpeer).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD tcw9pk ===
SUBREDDIT: r/Target
DATUM: 2022-03-13  SCORE: 289  REACTIES: 126
TITEL: They couldn’t walk two feet to put this magazine back.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[i0fzbd7] (score 43, diepte 0) I used to call people out when I'd cashier, look right at them as theyre trying to stuff or lay stuff anywhere else and loudly exclaim "if you don't want that I'll take it" in over 6 years up front not one of them showed any kind of shame or remorse for getting caught. People wonder how we cam be heartless to them, they're the reason why we are like this.
[i0g6qwt] (score 27, diepte 0) Lazy
[i0fzz6t] (score 19, diepte 1 OP) I will never understand how people are this lazy. It won’t take much of your time to put it back especially when it’s that close to where it’s brethren are.
[i0g7ey7] (score 18, diepte 0) ppl are so lazy i hate it
[i0gn20r] (score 16, diepte 2) So, I have a theory on this. The whole Karen thing that keeps happening in this country. I worked a job once where my boss taught me “there is no such thing as negative or positive attention. There is only attention and different ways to get it”. I think people in this country are so starved for attention (because we don’t teach people how to express their emotions in a healthy way) that they go places like Chick-Fil-La, Longhorns, Target, etc and behave like jerks or start fights over something stupid (or demand the managers) because they are starved for attention and know we can’t fight back. Does that make sense?
[i0g7igi] (score 11, diepte 0) Every morning, in the air care aisle, I find things one shelf or face away from their home locations. People are shockingly ignorant, but it is no shock. I always mutter to myself, “JUST PUT IT BACK.”
[i0gmzno] (score 7, diepte 0) They’re still making Mad Magazine?!?!
[i0hq79v] (score 6, diepte 3) You’re likely on to something. Think it also has to do with entitlement and power as well.
[i0i7m9e] (score 6, diepte 1 OP) Or you can do it since you were right there when you picked it up.
[i0icpjz] (score 6, diepte 3 OP) >with you guys on your phones all day.

Seriously? Bold of you to assume I’m on my phone all the time at work, I’m rarely on my phone when I’m at work because I take my job seriously the only time I’m even able to be on my phone is moments before I get off shift. If I’m even lucky! 

>You’re guys complain too much
I wonder why.
[i0gfso3] (score 5, diepte 0) I once saw a customer while blabbing on her cell about her worthless life pick up an item to look at it then drop it on the bottom shelf and repeat that the whole way down the aisle
[i0hkrmc] (score 5, diepte 1) One thing that continues to surprise me as a cashier after all this time is the products I haven’t thought about in years which we will suddenly get in and/or people will buy.
[i0gpx66] (score 5, diepte 0) Bob Saget would have got a kick out of this.
[i0i18tv] (score 5, diepte 0) I worked at a grocer many moons ago & I loved (?) catching people doing this shit.

"Hey, why don't you go ahead & hand me that steak instead of hiding it behind that *People* magazine?"
[i0i45ru] (score 5, diepte 1 OP) I HATE THOSE PEOPLE SO MUCH. 

Especially when they leave their carts in my register lane during a rush. Our cart station in the store it’s on your way out fucks sake.
[i0g9a2c] (score 4, diepte 1 OP) Like god forbid you take a second (not even) of your time to put it back where it’ll belong. But I guess people are too lazy and in a hurry to even bother. 

People make retail insufferable
[i0hj3uw] (score 4, diepte 1 OP) My job is to cash you out not put items away for your lazy ass.
[i0i7opd] (score 4, diepte 5 OP) I’m not staying here forever. Y’all make this job suck.
[i0i8dek] (score 4, diepte 7 OP) I never said that but ok
[i0gwolq] (score 4, diepte 0) A woman and I made eye contact as she unloaded her basket and left it right near a basket return spot.
[i0hj4px] (score 4, diepte 1 OP) Wtf
[i0i0dlc] (score 4, diepte 0) Guests think we are their care takers. When it comes to being a lazy pos.
[i0i7zjx] (score 4, diepte 0) The people who do this are the same who say workers don't deserve $15/hr
[i0hzvwy] (score 3, diepte 3 OP) Makes perfect sense actually
[i0hklzh] (score 3, diepte 1) Instead I am just theatrically grateful to people who give me things to put back instead of leaving it somewhere random. “Oh thank you! I can take that and I will put that right in my bin!”
[i0gkt19] (score 3, diepte 0) "guest"
[i0ikwf2] (score 3, diepte 1 OP) Not sure. Those mags have been there since the day Bob died
[i0hj03n] (score 3, diepte 1 OP) Sometimes it’s way too busy for us to put it back for their lazy asses, that’s why we have reshops and even then, they never come over to registers
[i0i110c] (score 3, diepte 1) Because your mom doesn't follow your entitled ass around cleaning up after you.
[i0jfamd] (score 3, diepte 7) It's douche bag customers like you that make retail jobs miserable. Is that so difficult to understand?

How fucking dense can someone be?
[i0ibwxt] (score 3, diepte 1) Wasn't it your parents job to teach you manners?
[i0i2fh7] (score 3, diepte 0) Same sort of asshole who doesn’t return cart to corral.
[i0iv6gy] (score 3, diepte 1) I feel the same way about people who abandon empty carts in the store and leave. You’re literally walking past the spot where the carts are on your way out. Don’t be a lazy asshole and purposely make more work for other people.
[i0ifl8d] (score 3, diepte 5 OP) So I can’t get annoyed? Cool good to know.
[i0ic7fn] (score 3, diepte 1 OP) Cope
[i0im61t] (score 3, diepte 0) Had someone who was buying luggage with wheels and they had the cardboard in between them. What did this dude do?  Put it on the floor for someone to trip. At least put it in the pdq shopper where someone wouldn't get hurt. I couldn't say anything since I noticed when I was helping another customer.  Customers are lazy or don't care enough since they probably never worked retail. Since I'm out of retail I don't do that stuff
[i0gn2i4] (score 2, diepte 2) So, I have a theory on this. The whole Karen thing that keeps happening in this country. I worked a job once where my boss taught me “there is no such thing as negative or positive attention. There is only attention and different ways to get it”. I think people in this country are so starved for attention (because we don’t teach people how to express their emotions in a healthy way) that they go places like Chick-Fil-La, Longhorns, Target, etc and behave like jerks or start fights over something stupid (or demand the managers) because they are starved for attention and know we can’t fight back. Does that make sense?
[i1ch5bu] (score 2, diepte 1) I did that once at a Publix whrn I was on break, dude decided that he was gonna get in my face and scream at me. Even my SM that didn't like me was shocked that I didn't clock him for doing it. Said I went stone cold and he kept expecting to see me swing in the video. But, I had my uniform shirt on and damn well KNEW that same SM would have enjoyed firing me for it. Otherwise, I would beat him in front of his preggo wife and kid like I was his pimp and his butt owed me money.

So, be careful. People are AHs.
[i0gmd1j] (score 2, diepte 0) No, no they can’t. We are here to serve them, that is our purpose in life. 🥸😭
[i0gmpih] (score 2, diepte 0) This is nothing. I’ve found a soda on top of the cooler where that same soda resides. Too high for a small child to put it up there. Someone took it out, decided they didn’t want it, and put it on top and left it there.
[i0hzopp] (score 2, diepte 3 OP) Gee. It’s almost like I can’t always leave register and put shit away because your lazy ass couldn’t be bothered to put it away.
[i0i83eo] (score 2, diepte 6) A magazine 4 feet away from its rack is a sucky day at work? Holy shit are you in you for a world of hurt at a real job.
[i0inng6] (score 2, diepte 3) Yes but you posted on a public website so anyone can be a keyboard warrior.
[i0h75k4] (score 2, diepte 0) Karen: Excuse me! That's 5 ft for your information!
[i0hpvx7] (score 2, diepte 0) Mad magazine is still around?  They sent me a letter saying it was over ot something.  But there it is.  Curious
[i0hzgyj] (score 2, diepte 1 OP) You’re the one who picked it up and put it there. Why couldn’t you do it? Oh wait you’re a lazy fuck that’s why.
[i0i1y3q] (score 2, diepte 3 OP) I’m literally not bitching I’m just saying if you can’t take not even a second of your time to put a mag back that’s not even two feet away why bother grabbing it in the first place? And it’s my account I get to post whatever I want when I want. 

>why did you wake up in the morning when you’re just gonna bitch? 

Some of us have work. Did you ever put two of those braincells together to form that thought? Clearly not.
[i0i3tbp] (score 2, diepte 5 OP) Literally what’s positive about dealing with lardasses? Oh right **NOTHING**
[i0i7ilm] (score 2, diepte 7 OP) They don’t really do anything for me accept annoy me, because oh I’m only on register. 

So they don’t pay my bills the way you think.
[i0hwhv9] (score 2, diepte 0) [Bob Saget!](https://youtu.be/aa96tCx2NU8)
[i0ilzik] (score 2, diepte 1) actual obsessive compulsive disorder or needing things to be neat?
[i0j5mcz] (score 2, diepte 2 OP) At times yes. I wouldn’t call it OCD but I do have this thing where if it comes across my mind I’ll obsess over it until I do it. Sometimes it causes me a panic attack if I don’t do the thing that’s on my mind
[i0igta6] (score 2, diepte 5) By your whole logic though, if you really do work at a DC, your lazies could actually try to load trucks properly instead of creating safety hazards. But no, continue to be a hypocrite, your shitty loading ain't worth what you're paid. See there? Don't assume all the time.
[i0jpc2d] (score 2, diepte 1) It’s not even just about that. You think they just do shit like that with magazines. Do you have any idea how much food we waste everyday bc shitty lazy customers would rather dump their frozen goods and perishable items behind toys and pillows than just put them back in the fridge or give them to an employee. 

How many times I’ve had to throw away inventory because some ass left ice cream sitting out that melted and overflowed. 

I’ve literally had guest throw up because someone hid meat somewhere, instead of just *putting it back*  and it rotted and started smelling before we found it. 

But sure, us being tired of people like that is the *real* problem and not the actual shitty people.
[i0ic4sy] (score 2, diepte 1 OP) I don’t know I didn’t know the man personally
[i0ih2bn] (score 2, diepte 0) Been in retail for 32 years,it never ceases to amaze me just how lazy and inconsiderate  people can be
[i0isl8x] (score 2, diepte 0) I used to find things like this and place them in their proper spot, but over the years it became so commonplace that I gave up. Same thing with shopping carts. Seems like, during the Trump years, the people in my red state became even less considerate and more entitled than ever.
[i0itmnx] (score 2, diepte 0) Oh brother you dont know how many times I’ve found an item that is supposed to be hanging from a pin, but is instead sitting on the shelf directly under said pin.
[i0iv1cr] (score 2, diepte 0) I deal with this everyday in Market, someone grabs an ice cream and leaves it literally on the top shelf of the original location like come on.
[i0j4vh6] (score 2, diepte 1 OP) I will never understand why people do that. Like it doesn’t take that long to put it back. Especially when you’re still there.
[i0iv688] (score 2, diepte 0) This is actually something I teach my kids, especially if I witness someone else do it, I say it out loud and say we shouldn’t be a lazy, a hard working employee has to put this away on top of their many, many tasks. Karens get pissed when I do that. I also have him some the product he pulls 😂 to me it the same as teaching a kid to stack their plates for servers 🤷🏻‍♀️
[i0ivm68] (score 2, diepte 0) Welcome to retail.
[i0j3bcf] (score 2, diepte 0) That’s good job security, right there.👍🏼
[i0m1foo] (score 2, diepte 1) And quite putting the batteries in the charger upside down.
[i0n6st8] (score 2, diepte 2) My favorite is when they take the battery out of a printer but then plug in the printer… what do they think is charging?
[i0jf8i4] (score 2, diepte 0) Guest thought process
Detergent > Magazine
[i0k9sjx] (score 2, diepte 0) Mad magazine!! Fuck all that other bullshit…
[i0kbhlo] (score 2, diepte 1 OP) Right? Mad magazine and bob saget. Two positives
[i0koeym] (score 1, diepte 4) See, I think it's the opposite of power and entitlement (well sort of, let me explain). I've seen a lot of people with fancy titles (and especially their trophy wives) that may look entitled and powerful on the outside. However, they are really very powerless in their world. They may be high up in the ranks at their company, but secretly they know they are just another wage slave working for a company that doesn't care. They may have married for money and are now losing their beauty and feeling ignored by the world that once craved their attention. So, even though on the outside they seem entitled and powerful, they know within their heart just how powerless they really are in this world. So, they go to places where they know people can't fight back to relieve the pressure that they secretly know within their hearts (that they are just as powerless as the people the people they are supposedly above in a system that doesn't care about any of us). Does that make sense?
[i0lsol2] (score 1, diepte 5) I didn’t mean they are already powerful. They abuse the service worker because they live in a world in which they feel powerless. They use this instance where they do know they can get away with powering over someone to feel like they have power and can influence others for once.
[i0jyii2] (score 1, diepte 9) Given how condescending you are, I find a lot of comfort in imagining how many people spit in your food. 😘
[i0jpn4a] (score 1, diepte 1) That’s like purposefully dumping your food on the ground because “oh well they have janitors and it’s their job to clean!”
[i0jq16p] (score 1, diepte 3) No it’s a perfect comparison. Because only inconsiderate assholes purposefully do things to inconvenience workers. 

Also do you think this only happens to magazines? Do you have any idea how much food we have to waste because people do the same shit with frozen and perishable food.
[i0jtz74] (score 1, diepte 5) Actually no, that’s not written in my job description at all. And even if being your maid was my job description it still doesn’t change the fact that food is going to waste and inventory gets ruined by your lazy actions.

I can only assume you’re one of these people because you’re fighting too hard to defend it and becoming much to bothered by a normal human beings reaction to be annoyed and wanting to vent about it in a forum built just for that purpose.
[i0jvgb4] (score 1, diepte 7) I’m not a floor team member so like I said…it’s not my job. And moving merchandise mean putting it on the floor not following around with a napkin and bib. I love how me being rightfully annoyed by horrible manners and horrible attitudes warrants being called a bitch. 

I love that I bother you so deeply that I’ve got you trolling and being disgustingly rude in a subreddit that isn’t even for you. I love how much I’m raining on your day here.
[i0jvmcq] (score 1, diepte 8) Lol the amount of people triggered by my original comment is vastly more entertaining than anything else going on today
[i0jvqwe] (score 1, diepte 9) Glad we can be of service to what I assume is a very dull, messy life.
[i0jwbuj] (score 1, diepte 11) Maybe you should take a break from Reddit. I’m concerned for your mental health. This level of outrage and anger from people venting about something that annoys literally any normal person is very odd. Maybe take a “me day.” 

See if it stops you from calling random women on the internet a bitch. Worth a try.
[i0jxnm8] (score 1, diepte 13) Yes because it not being gender neutral is the *only* thing wrong with calling someone that. 

And refill the what…sweety really I’m worried about you. You’re just typing nonsense at this point. Take a break, have a meal, drink some water, reflect mentally. It will really benefit you.
[i0k4jh2] (score 1, diepte 15) Wow. Quoting Kim Kardashian. A real voice of the average every day woman. Love this insight to you as a person. Go have the day you deserve, and I really hope you take my advise about that “me day.” You really seem like you need it. Maybe it will alleviate this odd rage you have built inside of you.
(43 reacties met lagere score weggelaten)

=== THREAD 1khag9j ===
SUBREDDIT: r/bartenders
DATUM: 2025-05-07  SCORE: 27  REACTIES: 125
TITEL: What are the best budget shoes for bartending for hours on your feet?
POST (source_id=post):
I wore dunks to work and was limping home by the end of my 8hr shift. I have since changed to crocs but my new workplace does not allow them :/. What shoes are the best for bartending but on a budget? I’ve heard good things about Nike p6000s, new balance 530, new balance 740, but not too sure! Suggestions are welcome 🙏

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mr5e2rt] (score 111, diepte 0) Don't get budget shoes. You'll regret it. I wear Skechers that run about $100, but l and I buy new ones every year. New insoles every six months. Take care of your feet, legs, and back.
[mr5bwzs] (score 74, diepte 0) No reason to budget on this one. Hokas SR.
[mr5mvsi] (score 31, diepte 0) Pay for shoes now, or Advil and podiatrist later.
[mr5nuzq] (score 29, diepte 0) Don’t cheap out on things that are between you and the ground: shoes, a mattress, and tires. Being cheap with those is always a mistake
[mr62euj] (score 13, diepte 1) 100 agreed on this.  Also look into work socks, they make a big difference too.
[mr5jkf6] (score 12, diepte 1) Seconded. Worth every freaking penny in how much it has saved my back, my knees, and also my ass since they are a great non-slip.
[mr5f28e] (score 12, diepte 0) I wear red wings, but I only buy them on sale for half off, consequently, I own 6 pairs now
[mr5g78m] (score 10, diepte 1) Definitely a false economy
[mr5kua7] (score 6, diepte 1) I have a pair that I keep at work. Makes them last a little longer.
[mr5e3dk] (score 6, diepte 0) I wear New balance 740 with insoles for a 10 hour shift and they've worked for me for years.
[mr704e9] (score 6, diepte 1) This is the way. I ran iron rangers behind the bar for years, whites boots briefly (more when I was serving) and now Mephisto shoes. Working on your feet all day and wearing cheap shoes is crazy work. 

You will spend less over 5-10 years despite a larger initial cost and you’ll be more comfortable the entire time. 

Don’t wear cheap shoes.
[mr5nd4v] (score 6, diepte 0) Dont budget on shoes haha. I used to buy cheap $20-$40 pairs that would fall apart after 6 months and i didn't realize just how bad it was
[mr5g8kp] (score 5, diepte 1) Yoo Red Wing gang. Boots or shoes? I've been rocking my black Iron Rangers forever
[mr5kdjm] (score 5, diepte 0) Honestly, it might sound weird. Sketchers. I have had pair that have lasted my 2 years without replacement. I was working 50-60 hours a week as both a lead bartender and Manager. 

But inserts are your key. I don’t care who you are e but Dr. Scholls High heal inserts are amazing. I’ll fight anyone on this.
[mr5lm3o] (score 5, diepte 0) Asics cloud. Sorry, budget gotta be bigger when it comes to more important things.
[mr88zz8] (score 5, diepte 1) Thanks, gramps! 

Seriously, the first I heard this was from my grampa. He's never been wrong.
[mr89js5] (score 4, diepte 2) Yeah. It was a weird adjustment for me too. They used to be the Walmart/pay less brand
[mr5ijei] (score 4, diepte 0) Blundstones. They’re worth it in the long run
[mr6ati4] (score 4, diepte 0) I've been bartending for ten years in vans and converse with cheap inserts in them. It was never much of an issue for me until about a year ago. I got doc martens, and was disappointed that while they're a good shoe, they weren't good for me personally for work, because at the end of ten hours they would be pushing my toes together just slightly enough that my feet would be sore.

I was discouraged that those didn't work and then got blundstones. Changed my LIFE. My back, knees, and feet don't hurt anymore. I like them because of the wider toe box while not looking dumb or standing out. They're snug and comfortable but I can easily wiggle all my toes inside, very comfy all night. You can wear them with anything. 10/10.
[mr64bno] (score 3, diepte 1) Just got my 1st pair, feeling good so far
[mr6j5in] (score 3, diepte 1) Blacksmiths all day. I have three pairs.
[mr5yjuy] (score 3, diepte 2) Pricier shoes don't always mean better. I had Hoka's and within a year they were busted since I was working 40-50 hours a week. Thankfully, I had a decent relationship with someone who worked with them, so I was able to get a discount. 

  
That's why I always recommend Sketchers since they are easy to replace on Amazon and available. So you can go 4-5 years and spend the same amount as Hokas. I've also only replaced my inserts twice in 6 years. But that was just my experience. I'm willing to try Hokas again, but I refuse to pay full price since I've been burned.
[mr5o0j2] (score 3, diepte 1 OP) You’re so right!! I will spend the money next pay check :)
[mr5rmt6] (score 3, diepte 0) So many correct answers here. 

I need 4E shoes and the best fit/ comfort/ durability has always been New Balance. I wear 860s.  I buy two pairs each winter and rotate them each week or so. They’re not cheap but you have to invest in a good pair of shoes. Please don’t skimp on your shoes
[mr5y818] (score 3, diepte 0) I will never not wear nonslip shoes, or cheap shoes. My feet, back, and safety are too important. Birkenstock professionals have been my go to lately. They’re not cheap, but you can do a pay in four no interest with klarna I think if you have ok credit
[mr5yidg] (score 3, diepte 0) Sketchers are industry stardard. But a few of my coworkers rock adidas ultraboost, or hokas. Our job gives us 50% off on sketchers so majority of them use those.
[mr5z4js] (score 3, diepte 0) Shoes For Crews. Under $100 and take a beating, they could last up to a year. Easy to replace insoles
[mra51jt] (score 2, diepte 3) socks, for work /s   usually higher quality like wool, or compression.
[mradrpg] (score 2, diepte 3) They're kind of like snowboarding socks.  Some call them compression socks.  I live in Canada and there's a place called Mark's Work Warehouse.  They sell clothes and shoes for physical jobs.  All the socks there are made for different jobs, like working in cold, heat, ect.  They cost maybe twice as much as normal socks, but have much better cushioning and life span.  Once I forgot to wear my work socks, and half way through my shift I could feel my feet getting sore.
[mrcrx2e] (score 2, diepte 4) Thanks! That's cool. I'm gonna look for these.
[mrczp8v] (score 2, diepte 5) Worth every penny ☺️
[mr88ttz] (score 2, diepte 1) I get what you're saying, and I know their products have changed a lot, but thinking Sketchers are anything other than "budget" is still odd to me.
[mr89zfw] (score 2, diepte 3) What's the opposite of enshittification?
[mr9kl0e] (score 2, diepte 2) They still make shitty shoes, they just also make not shitty shoes.  I've been pretty safe grabbing the work branded stuff and have only been burnt by a pair of slip-ons that blew out within weeks.
[mr9koem] (score 2, diepte 1) Any insoles you stand by?  (On?)
[mr9ly22] (score 2, diepte 2) The ones that fit YOUR feet. I spend $20-30 on some decent ones. But I have foot issues that most people don't have to deal with, so I won't recommend a particular brand or style.
[mr5ec80] (score 2, diepte 0) I swear by onclouds. I feel great after 16 hours.
[mr71bsg] (score 2, diepte 1) Just bought my first pair last week . Got the Cloudmonster Voids. So far so good.
[mr96q0z] (score 2, diepte 2) Beckmans and Moc Toes for me
[mr96t3u] (score 2, diepte 2) Vime's Boots theory of economics
[mr5ohyb] (score 2, diepte 1 OP) Ooh I’m from the UK I’ll check if they have those inserts or similar , hopefully it will help until I can buy more expensive shoes !!
[mr5mqv8] (score 2, diepte 0) Asics Gel Nimbus 

  
These are the first shoes I've worn behind the stick where my feet feel fresh after my shifts
[mra57ml] (score 2, diepte 1) And a quarterzone shot in the ball of my big toe. Every other year.
[mrbm4pl] (score 2, diepte 2) > a quarterzone shot

cortisone?
[mr5xxgl] (score 2, diepte 0) Hoka Bondi SR leather. Best work shoes ever. Never cheap out on your feet
[mr5zyvw] (score 2, diepte 0) honestly, go into a shop that specialises in running/walking shoes and they’ll be able to recommend the best shoe for you. everyone’s feet are different so what works for one person won’t work for another.

i went in expecting to buy a pair of hokas and ended up with a pair of new balance 860s and my feet haven’t hurt once since wearing them
[mr9m3t6] (score 2, diepte 1) Standing by Blundstones here, as well.  I have the chelsea boot in two colors and swap them out (plus a pair of Skechers when I'm feeling more casual).  

I'm sorry anyone ever recommended you Docs for work.  They may have been worth breaking in 30 years ago, but the modern version is fast-fashion designer mill trash.
[mr6usjj] (score 2, diepte 0) I have an unpopular opinion on this but I’ll share it. I wear minimal drop, zero arch shoes, non slip shoes with a leather exterior. 

Zero arch is what’s most natural for your feet and I can’t be convinced otherwise. It takes some getting used to but ultimately I think it’s what your feet adjust to most naturally. I do about 16k-20k steps per day and I have no back pain and almost no foot pain (aches at the end of the 20k but nothing lasting).
[mraud2o] (score 2, diepte 1) The only shoes that didn’t make my feet hurt were bare foot shoes. Vivobarefoot makes some really great shoes, but I started to favor tadeevo toward the end of my bartending tenure. I also enjoyed Lems.
[mr7rbg5] (score 2, diepte 0) Skechers slip ons for restaurants. $60 at Kohl’s
[mra5muw] (score 2, diepte 0) Depends if you will be around the fryer.   As other said the skecheters are good, but as silly as it is. My shoes for Crewes were great, and I loved my Doc Martintns. They'd last like 5 years when I would be in the kitchen. Oddly the steel toes came in so handy. I was surprised how often I'd kick something.
[mr7rrcl] (score 1, diepte 1) Yeup. These have changed my life.
[mr9orty] (score 1, diepte 1) And get at least two pairs, they last longer when you don’t wear them every single day
[mr9ywac] (score 1, diepte 2) What are work socks?
[mrcrqmq] (score 1, diepte 4) Thanks!
[mrcry7h] (score 1, diepte 4) Thanks!
[mr8f4lv] (score 1, diepte 2) I just got the new 6’s and they’re so comfortable
[mr6l2bv] (score 1, diepte 2) Beckmans and moc toes for me!
[mr5ifk2] (score 1, diepte 0) Just got these https://www.wolverine.com/US/en/rev-vent-ultraspring-durashocks-carbonmax-boot/48793M.html and I'm a huge fan. They're hard-toed (carbon) but the soles are flexible like sneakers, which is great for having to bend down for something and being light on your feet.
[mr5nnsl] (score 1, diepte 1) I love mine.
[mr5o6ol] (score 1, diepte 1 OP) Ooh I’ve heard asics are good!! Thank you :)
[mr68pc6] (score 1, diepte 2) Good shoes and compression socks. Just try them and they'll change your life.
[mr5nwsr] (score 1, diepte 1 OP) Which new balances did you get ? Are the 530s or 740s any good x
[mr76o8g] (score 1, diepte 2) I have the 880s and that foam makes a huge difference. Would buy them 100 more times
[mr8fp8o] (score 1, diepte 2) I got Arishi v4, but it seems like online people prefer the 880s. Go to a shoe shop and try some on!
[mr5olsl] (score 1, diepte 0) For whatever reason, high-top vans always worked for me. But I bought the "made for the makers" nonslip line, which I think they discontinued.

When you find what works for you, buy two pair and rotate through them so they fully dry between shifts, stink less, and last longer.
[mr5qdzv] (score 1, diepte 0) HOKA Bondi 9's! Pricey at $180, but it's extremely worth the price imo, my feet were immediately happier
[mr5rugs] (score 1, diepte 0) Whatever you do, take care of your shoes...

I recently bought these and put some dr scholls inserts and I'm really very happy with them. 

VILOCY Mens Wide Width Slip On... https://www.amazon.com/dp/B0DS49RKFP?ref=ppx_pop_mob_ap_share
[mr7az8p] (score 1, diepte 1) I've been tempted to get a pair of Birkenstocks myself. Idk about the price,  I just need my feet and everything else to stay healthy. 
I was tempted for a pair with steel toe as well. (Also a bar tender)
[mr5yp4k] (score 1, diepte 0) Insoles for your most durable and comfy shoes.
[mr5ywwk] (score 1, diepte 0) Nike Tanjuns. I buy the same pair every year for the last decade. At 40$ I get my wears worth
[mr5zqkd] (score 1, diepte 0) I used to always wear sneakers. Costco reeboks or something from marshals. But dude, they never last and the pain involved is unbearable at times. Don’t go this route. As bartenders u gotta take care of your body too. I invested $150 for some durable leather boots from Thursday and have not looked back. Complete game changer. Plenty of support, they’re durable, and don’t smell as bad as sneakers. I polish em every other week making them brand spanking new compared to my mud covered shoes
[mr5zrce] (score 1, diepte 0) Brooks ghost max
[mr614vd] (score 1, diepte 0) I like shoes for crews. But only expect a year out of a pair.
[mr61v7k] (score 1, diepte 0) Skechers work shoes
[mr6380y] (score 1, diepte 0) Bar Manager here 👋🏻 i’ve worn Dansko Profressional Black Box Clogs for 3 years. I’ve torn both my meniscus. Mf y knees only ache after working 14 hrs straight after wearing these. Never my feet! They run about $140 new, but tbh, J bought my first (used) pair from a thrift store for $8.00, cleaned them up, and was surprised by how supportive they were. I was always a Walmart Sketcher shoe buyer before; not too picky. I bought a new pair last year after a dog I was sitting chewed up my used pair. Highly recommended!
[mr64b02] (score 1, diepte 0) Chucks
[mr65jti] (score 1, diepte 0) Ive tried everything from 200$ danskos, Unis, kurus, and docs, to 15$ Walmart shoes that I'd toss out once a month, and everything in between. The expensive shoes would work well for about 3-6 months, but are worthless shortly after that. I couldn't justify spending that much, that often. Skechers are a good option in the mid range, but for me, they fail just as fast (they last my wife forever but she weighs 95lbs).  These shoes in the link though, are very similar quality to Skechers, just without the name. I have 2 pairs that I rotate and they've been phenomenal and I don't feel like I need to rip my shoes off the second I get home. They wear like the other shoes, but 35$ every 6 months (if you're only using one pair) is a great deal. My feet sweat horribly in most shoes, but these are so breathable that it's not an issue anymore. Incredibly lightweight and they're more non-slip than any dedicated non-slip work shoe I've worn. (No I'm not an advertiser or spokesperson) 

https://a.co/d/jeAAWUX
[mr68anc] (score 1, diepte 0) Get a good pair of compression socks and some arch support shoes. You only get one pair of feet in this lifetime. When you have feet issues, it affects your entire body. Don’t cheap out on this one, trust me
[mr69lf7] (score 1, diepte 0) I swear by the any of the FreshFoam New Balance plus a pair of Dr Scholls “Work All Day” insoles.
(49 reacties met lagere score weggelaten)

=== THREAD umpeer ===
SUBREDDIT: r/Chefit
DATUM: 2022-05-10  SCORE: 58  REACTIES: 123
TITEL: MY FEET HURT.
POST (source_id=post):
What's the best thing out there for comfortable foot wear? I'm a 10.5 with wide feet. Non-slip is not important to me, comfort after 12-16hr days is paramount. TIA

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[i83205f] (score 117, diepte 0) Non slip will be important once you bust your ass or break open your skull. 

Birkenstocks are my go to. Ridiculously comfortable even after 15+ hour shifts, and they’re non slip
[i833neb] (score 36, diepte 0) I'm flat footed as fuck and overweight. I wear bistro pro Crocs and my feet never hurt after long shifts
[i83ddqt] (score 35, diepte 1) They’re also the only kitchen shoes I’ve ever owned that don’t smell like the inside of the devil’s asshole after a month. They’ve been my choice for 8 years or so now, and I’m only on my third pair.
[i832yzg] (score 19, diepte 0) Snibbs are expensive but they are so damn comfy 

They feel like expensive walking shoes but have non slip bottoms
[i832dj4] (score 13, diepte 0) Birkenstocks and orthotics
[i83bhhw] (score 12, diepte 0) Get non-slips, ya dirty grease surfer!
[i832kaf] (score 11, diepte 0) I have been wearing wedge soled work boots from whites boots had a cobbler put on a vibram slip resistant outsole and they have been the best decision ever. Wore Birkenstocks for years and never had the same level of comfort
[i839qhc] (score 11, diepte 0) I’m about to give Vans another go about but their actual skater shoes and not the ‘Tom’s’ style. I have high arches and a bone spur/plantar fasciitis so walking on a cloud is necessary. You could also do stretches before/during/after your shift to help but a good shoe will do wonders. My ‘non-slip’ danskos definitely slipped and the high clog almost rolled my ankle numerous times but the high arch support is unparalleled from other non slips
[i83uqpr] (score 10, diepte 1) I've been out of the industry for a few months and I still wear my birks. Best shoes I've ever owned.
[i839jpp] (score 9, diepte 0) I've tried Sketchers, Birkenstock, Crocs, everything. 
In the end, I found out that I had plantar fasciitis and it didn't matter what shoes I wore because none of them had the ability to support my feet.
I saw a podiatrist and got fitted with custom insoles and now I can wear any shoe with comfort after several 14 hour shifts in a row.
I currently wear new balance shoes.
[i83onh4] (score 8, diepte 1) This or the non-pro version and just throw in some Dr. Scholl's. I'm not overweight, but I'm pretty flatfooted and i still get the ones designed for overweight men just because I'm on my feet for so long.
[i839cl5] (score 6, diepte 0) Non-slip will be important after you take a dive and now your back and feet hurt.

Orthopedic shoes are a thing? Why does every nurse wear clogs, because they allow the nurses to be on their feet all day. I had a doc recommend them and I laughed because "I'm only 30." I gave in and what a game changer. Spend the money. You can always get more. You can't get another body.
[i83gr0z] (score 6, diepte 1) I wear Dansko and I say that they’re the best shoe on earth 98% of the time and the other 2% of the time they’re actively trying to bring me down….. 

Seriously so comfortable but like uncomfortable at the same time. I’m also in love with being taller.
[i83ujmd] (score 6, diepte 0) I like Dansko, but they take about 2 agonizing  weeks to break in.
[i83beaf] (score 4, diepte 0) birkenstock orthotic in blundstones. not the most ideal for fast on/ off, but the most comfortable shoes I own. many many hours on concrete in the bakery.
[i83kk1h] (score 4, diepte 0) Crocs dude
[i846c5f] (score 3, diepte 1) Birkenstock Bostons all the way, they fixed my back pain
[i84jw9a] (score 3, diepte 2) Super Birkis are the nonslip ones made specifically as work shoes. They’re some sort of rubber construction, but heavier duty and a bit more rigid than Crocs. The insole can be removed and replaced. Without the insole they’re one piece and can be submerged in water for washing.
[i83cf1u] (score 3, diepte 1) This is the way. Get a good custom orthotic made and a pair of Birkenstocks. I wear the Birkenstock Arizona sandal around the house as well and they help vs being barefoot all the time. I have been fighting plantar fasciitis for years now and do the long days as well. Additionally hydrate, vitamin c and gentle daily stretching are key to staying out of pain.
[i83ck6a] (score 3, diepte 0) Crocs with gel insoles bud
[i83hvtx] (score 3, diepte 0) Hoka makes a non slip shoe, it’s the best purchase I have made as a chef. I have tried cheap shoes I’d replace monthly, danskos, Birkenstocks, I bought the new balance x shoes for crews shoes in different styles, hell I even tried the bragard shoes, I have tried everything. These are the best. I will warn you, they have the typical Hoka support so you look like you’re wearing platforms, but you can move so smooth you can dance over your critics
[i8415xj] (score 3, diepte 0) Non slip Crocs kick ass, 10 outta ten
[i845k4u] (score 2, diepte 1) I use to use two different pair over the course of a 14 hour day. Birks 100%
[i84ajyl] (score 2, diepte 2) I like the Birkenstocks tokio super grips
[i86fcv9] (score 2, diepte 1) I have flat feet and I *hated* my birks, just a word to the wise.
[i83sgkv] (score 2, diepte 1) I’ve been on snibbs for a month now. Will prob be my go to shoe from here on out. Super comfortable and I can’t slip if I try lol.
[i84tk6q] (score 2, diepte 1) i tried those but they are destroying my feet. the twelves are too big and blister me, and the 11s are too small and my toes are being crushed. It hurts. I need to find an alternative asap.
[i8346by] (score 2, diepte 0) Birkenstocks. The real cork ones, not the synthetic SuperBirkis. Made by the same company, but you want the real cork footbed. I have a pair of the Tokio style (heel strap) that have lasted me 3 years of heavy use in tougher conditions than most kitchens. (year round in a high alpine indoor/outdoor environment. Snow/ice, dust, dirt, mud, you name it). The non-slip is the best I've used, between Crocs, Mozo(pre shoes4crews, and Birks) 

I'm a 10.5, kinda flat-footed, but can work a 16hr day in my Birks with zero issues. The first two weeks of breaking them in as they mold to your feet are uncomfortable, but after they're broken in, they are amazing.

They've been out of stock on my size for almost a year, I just bought two new identical pair so I don't have to worry about it next time.
[i83kege] (score 2, diepte 2) My feet still ached in danskos but it’s the only shoe I’ve found in nonslips with good arch support.
[i83k246] (score 2, diepte 1) Another vote for vans sk8hi. After a while the leather is butter soft on feet. I added dr scholl’s for arch support. Also good if you cruise to work.
[i83febq] (score 2, diepte 0) I’ve always liked sketchers ones but that’s me
[i84di3l] (score 2, diepte 2) Ah for me the $60-$70 pair lasted about a year, but spending 69 bucks a year to have shoes that made it so I actually could feel my feet felt worth it to me
[i83geo3] (score 2, diepte 0) Not footwear but when I was working long shifts doing fine dining I would submerge my feet in a bowl of ice water for 15-30mins after shift. 

One of the servers was a trained ballerina and she told me that's what they would do after hours of dancing practice. It works really well and tends to help with swelling and pain.
[i86ilm0] (score 2, diepte 1) I sell shoes and Hoka is beyond the way to go, find that non slip version and enjoy the rest of your pain free feet life
[i86ky8t] (score 2, diepte 2) I bought hokas for running after a foot injury and managed to run a half marathon with them. I’m about to retire my running shoes to be my new walking shoes and then I’ll be Hoka in all 3 phases of life
[i83qwys] (score 2, diepte 0) Not a chef but a pharmacist, so standing all day etc. I put a pair of doctor scholls custom fit orthotics in the bottom of a pair of doc martens non-slip boots. Zero pain after a 12 hour shift. They just have to be well broken in first
[i84w5s5] (score 2, diepte 0) real talk: crocs
[i831kib] (score 1, diepte 0) Vans I always found worked for me with wide feet, black slipons. Supra also do slipons called cubans which fit my feet very well. Skate shoes in general are very comfortable to be on your feet for long periods. But NikeSB are so slim fit they kill my feet.

As for actual chef shoes... no idea, ive never had to wear protective footwear.
[i85fw8g] (score 1, diepte 2) I like the leather ones with the cork soles. Bear in mind your feet will be killing you for about a week until they mould into each other but then they are the most comfortable thing ever
[i86gvv3] (score 1, diepte 1) Double the non-slips - it’s a must.

Also, for me, dr scholls inserts worked great. The expensive $40-50 ones where you stand on the stupid thing that like measures your arches and stuff (they have em usually back in the medical/wellness area of any large grocery superstore type place).

If I recall they listed a good year, maybe year and a half. But def did wonders.
[i8c0zjb] (score 1, diepte 1) Do you wear the ones that are open in the back or the closer to a clog looking ones? One of my coworkers wears the open backed ones, but personally that doesn't seem practical in a kitchen when somebody is constantly spraying the floor with the hose.
[i8dj1jc] (score 1, diepte 2) I wear open back ones, at my job spraying the floor isn’t really an issue
[i86qrwc] (score 1, diepte 1) I had a different experience with birks same style you mentioned only lasted around 10 months of working 5 x 13 hour days weekly, then they gave me a horrendous pain in the arch of my foot, switched to crocs about a month in so far so good. I think birkys are pretty great generally but for some reason didnt work out for me
[i8750me] (score 1, diepte 2) Yeah, like recommending knives to someone on the internet, shoes are highly personal too. Everyone's feet are different.

Shame about the durability on yours however, mine and all my my coworkers who have birks use them until the non-slip is almost completely worn away.
[i836oys] (score 1, diepte 0) Used to buy nonslip stuff, but been working in Doc Martins with the added insole 10 hour days for the past few years and my foot pain practically disappeared, only particularly hard days cause any discomfort
[i83892m] (score 1, diepte 0) NB
[i85931h] (score 1, diepte 3) You should try Calzuro’s! Kinda pricy but they’re super easy to clean and maintain.
[i8b4ruq] (score 1, diepte 1) Right? Like wtf, I slip anytime there's any moisture basically, the non-slip part is a lie.
[i8bz6dk] (score 1, diepte 2) Yeah I have no clue how they’re allowed to be called non slip
[i83bnsm] (score 1, diepte 0) Non slips won't be a problem when you can't work due to injury lad
[i85fhop] (score 1, diepte 1) This is the way
[i83ct64] (score 1, diepte 0) Thoroughgood work boots for me. 

Spent thousands over the years on bragards, Birkenstocks, danskos, etc. They all worked for a bit, but wore out quick and I'd often roll my ankles in the heeled ones. 

Other shoes didn't offer protection from spills or drops.

My boots have lasted me five years so far and show no signs of wearing out anytime soon. 

They also saved my toes twice from being crushed. Well worth the $275 I spent five years ago. 

Bonus, they're made in USA by union labor.
[i83d8gu] (score 1, diepte 0) Sika cloggs

Specifically birch wood sole comfort cloggs. 

I usually get about 8 thousand hours out of them, so depending on what your job is like that will do you for 2-4 years. 

I like the wood sole, but it might not be everyone’s cup of tea, and they do have other options.

Good arch support, and they help keep the lower back aligned properly and reduce back pain as well.
[i84btx0] (score 1, diepte 1) Cheaper and does the same job, just don't last as long if you're in kitchen:/ I go through a pair of $70 sketchers about twice a year
[i85el6e] (score 1, diepte 1) I've tried sketchers twice. Both lasted less than 3 months.
[i83hxdi] (score 1, diepte 0) birkenstock clogs used to work for me but it’s hard to put insoles in them. i used to wear the superbirks with insoles and those were great. yes might be a bit heavier but better support i think. 

i wish OOFOS were non slip cos i’ve heard amazing things about them. there’s also a brand called CALZURO that doctors/nurses wear but i don’t think they’re non slip
[i83js7m] (score 1, diepte 0) As a healthcare worker I can say Brooks, Hoka, On Cloud, expensive, but your feet will thank you.
[i83keeh] (score 1, diepte 0) This may not be comfortable, but, it is doable (I hope)
I used to work retail and had to stand on a tile floor in 3" heels and so being inventive we discovered a couple things.
When our feet hurt and calves were killing us we:
Wore support stockings, especially with an arch support band in the stockings.
Get an alcohol based spray (something lightly scented, because you work with food!)
Spray your legs through your socks and your feet.
The alcohol will serve to cool your aching limbs and helps a bit with swelling.
If I were you, I'd get at least two pairs of non-skid foot wear and take both to work, spray your socks (feet and legs) hell, I'd even take a minute and change your socks too. Anyway, then change into a slightly more roomy pair of shoes for the rest of your day. 
Maybe, get some gel insoles for each pair. 
It is imperative you have shoes that are safe and fit your feet, maybe a little wider since kitchens keep you standing all day.
Jell, if I thought you'd do it, get some literal support pantyhose, they literally massage your legs as you move. Sorry, this was so long. But, take care of your feet all that pain will just keep moving upwards in your limbs and body if you don't. Good luck!
[i83lako] (score 1, diepte 0) No one is mentioning compression socks. They will help your entire leg not just your feet. If you are standing all day it will help with fatigue. Make sure they are tapered and dont constrict at the top of the sock or they will have an adverse effect.
[i83m0c5] (score 1, diepte 0) Danskos are good, but they take a while for the leather to form to your feet, so the first day or two might be a nightmare. 

Skechers work are great but be prepared to replace every 3 months =/
[i83pqd0] (score 1, diepte 0) Might want to try a couple options and change shoes (and socks) halfway through your day.
[i83pyqc] (score 1, diepte 0) I'm loving the new balance antislip work shoes these days. They're murdered out and actually something you can wear outside of work. Just be sure and get the extra wide ones.
[i83r07b] (score 1, diepte 0) It’s not about just the shoes, it’s also about the socks. I bought darn tough socks which are a blend of merino wool. Now that my feet are not wet from sweat my feet don’t hurt. They are expensive but lifetime guaranteed.
[i83v3vm] (score 1, diepte 0) Nurse clogs are the only way to go for me. Right now I’m wearing Alagrias. My previous pair were Sanitas. Danskos are cool but not with my high ass arches. One of these three are essential but take a few doubles to break them in proper.
[i83vlx7] (score 1, diepte 0) Wearing compression socks makes a huge difference in feet and leg fatigue.
[i83xih6] (score 1, diepte 0) so Birkenstocks work well but you have to replace those cork soles every 3 months or they're worthless. I recently got corporate approved Bullfrog boots from Shoes for Crews and ,for me, they're a game changer. the only downside is they rub my leg hair so I have baked patches on my legs.
[i83xk59] (score 1, diepte 0) I’ve had great luck for years now with Redback boots from Australia
[i83y1gg] (score 1, diepte 0) a colleague once said, change your socks every 6 hours, what a change!!
[i83yync] (score 1, diepte 0) In the kitchen... Some nice low cut construction shoes(meaning with reinforced toetips) with slip prevention and nice support. Mine even got ESP. Gotta run like 100+ of your currency but well worth it.

Edit. And make sure they are closed. None of this Crocs shit that people are saying... you don't want to run the risk of some hot liquid possibly falling all over your feet.
[i86rvew] (score 1, diepte 1) The crocs people are talking about (Bistro, their work shoe line) *are* closed. They don't have holes like the normal crocs
[i841i5g] (score 1, diepte 0) Walk fit insoles....life-changing
[i842btc] (score 1, diepte 0) Birkenstock are nonslip and heaven on the feet. Most kitchens I’ve worked have a majority of the staff in them
[i842lmp] (score 1, diepte 0) I wear snibbs. I’m on my feet 10-14 hr a day, and they still feel great
[i845hzj] (score 1, diepte 0) Personally, I love my Doc Martens. They’re the service ones. Non-slip, extra padding in the soles, shock absorbent, steel caps in the toe, and waterproof. I’ve had them for the past few months and they’re probably one of the most comfortable pairs of boots I’ve ever owned in general
[i845pvp] (score 1, diepte 0) I tried Crocs for a few months and they worked okay. Then I found these nonslip clogs made by Carhartt and I've been wearing those for the past five years. They are a bit heavy due to all of the padding and thick rubber soles, but considering I'm mostly shuffling back and forth on the line and not really walking anywhere the extra weight compared to the Crocs made no noticeable difference. Highly recommend
[i846ase] (score 1, diepte 0) Im going to tell you what I wish I knew back when I was in the kitchen.  Go to a running store like road runner or fleet feet.  They have this machine that scans your foot and makes a custom insole.  Its not cheep, but damn if a cook is going to spend money its should be on knifes and there feet.  Your a wide foot, I know New Balance makes wide and they make non slip (I put both filters on on NB's website.  Here you go [https://www.newbalance.com/men/shoes/work-shoes/?prefn1=width&prefv1=Wide%20%282E%29&srule=null](https://www.newbalance.com/men/shoes/work-shoes/?prefn1=width&prefv1=Wide%20%282E%29&srule=null) ).

Dude you NEED that non slip, too much "Hospital now" things around you to fall on because you chose to go full nelly stomping in your air force ones.  Non slips will make it much harder to slip.

Also Socks, don't overlook socks.  If you can afford it Bombas socks are awesome, but not cheep.  Wait around to some sale and snatch up packs when you can.  But at least some good Haines.  I developed this thing called pitted keratolysis (dont look it up) because I wore the wrong type of socks for too many 16 hr days.  Its basically trench foot, that shit Lieutenant Dan was warning Forest about.

The other big thing I learned when I hung up the apron.  I dont know anything about you, but if your a heaver person, it gets progressively harder being on you feet for hours.  When I left the kitchen I lost 50 lbs and my knees and feet stopped hurting every day.  Also if you get those custom insoles, you can learn how you walk and land your on your feet.  Apparently we all do it slightly different and that can have some weird effects on other parts of our body.

&#x200B;

Edit.  Just found out Hoka makes a non slip.  Dude I wish that was a thing back in my day.
[i846vsj] (score 1, diepte 0) Good thick socks for 10 to 12 hour days.  Those bargain bin thin cotton ones will not do for me
[i8470o3] (score 1, diepte 0) I preferred Dansko to Birkenstock, or rather my back did... only downside is you look like a jabroni if you wear them to the bar in your street clothes after work.

I usually get a couple years out of a pair.

Work boots by Timberland are nice, but they get rather hot.

Avoid tennis shoes like the plague.
(43 reacties met lagere score weggelaten)

