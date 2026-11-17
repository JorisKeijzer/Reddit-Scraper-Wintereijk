# Label-batch batch_0070

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
Schrijf het resultaat naar `batch_0070.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1mn0yys, 1ayi8ac, 1d17rjk, pvjrqk).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1mn0yys ===
SUBREDDIT: r/AmazonFC
DATUM: 2025-08-11  SCORE: 62  REACTIES: 115
TITEL: How Are Your Feet Surviving 10.5 Hours??
POST (source_id=post):
I just completed my first 2 weeks doing decant at an FC and although the job itself is easy, my feet are going to make me quit. By the time my second break rolls around I can barely walk to the break room. During the last 2 hours of work I swear I'm on the verge of tears. And when I finally kick my shoes off at home I'm damn near crawling. I was a city mail carrier with a walking route before, so I'm used to being on my feet, but this is unbearable! 

Did I buy the most uncomfortable shoes on Zappos? I bought Reeboks, wide and a half size bigger. They came with insoles but after a few days of pain I switched them out for Dr Scholls and that hurt even worse. So I went back to the previous insoles and added Dr Scholls pillow toppers which were a little better as far as full foot and lower back pain goes, but still very painful for my heels.

Somehow I ended up with a second Zappos credit so I'd like to use the $110 for a better pair of shoes but I need recommendations. What are you all wearing on your feet? Bonus points for fellow plus-sized employees, wearing Zappos shoes with no pain!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[n81mhfw] (score 70, diepte 0) It just takes time to adjust. do all the foot care.. massage/heat&ice, insoles, etc… My feet had me in tears until one day they magically just didn’t hurt as bad.
[n81odpm] (score 27, diepte 0) Spend money on GOOD socks. I wear Fox River socks that are around $20 per pair. No aches, pains, or blisters and they last for years.
[n81rclf] (score 20, diepte 0) I am going to swear on Timberland Pro shoes straight out the box, insoles are the best.
[n81s2s2] (score 14, diepte 0) I was in so much pain my first two months. I would take my shoes off the second I got in my car. I did every aftercare routine recommended on this sub. Nothing helped. A little research told me that your arch difference from foot to foot is particularly exploited by safety shoes. I went to Walgreens and did a dr Scholls kiosk. Turns out, I’m flat footed on one foot and have a considerable arch on the other. I got the custom insoles for a total 60$ and my feet/back felt so much better immediately. Highly recommend
[n81nlcr] (score 13, diepte 1) Same!
[n81ws28] (score 10, diepte 1 OP) That's good to hear. I was surprised on my 5th day I went like 6 hours with no pain then it hit like I was standing on bricks. It gave me hope that it'll get better as weird as that may sound. On the first day my instructor told us to freeze water bottles to roll under our feet after work, unfortunately I'm in a hotel for now with just a mini fridge that doesn't have a freezer
[n81mh7v] (score 9, diepte 0) if you aren't used to working on your feet all day, it's gonna suck. But i guarantee you after a while you won't even notice. I've been working at amazon for like 4 years now and i can't even tell you the last time i thought about my feet whilw working
[n81plnq] (score 9, diepte 0) Compression socks do wonders
[n81w7jw] (score 9, diepte 1) I swear by the timb pros. The laceless ones. The insoles plus 2 pairs of socks
[n81m0ch] (score 8, diepte 0) Yeah, two weeks in, it's gonna suck. For a lot of people, it just takes adjusting to (like a month or three, maybe). Others never adjust. You could always see about getting custom orthotics from a podiatrist, though it could be pricey even with insurance. And even those can take time to arrive and will be uncomfortable during the breaking-in period.

I'd just say ibuprofen, shoes off during break if you can so your feet can breathe, and soak them at home when you have a chance.
[n81x6xg] (score 6, diepte 1 OP) I was a city mail carrier for USPS and although sore, my feet never hurt like this. That being said, since covid, I've been working remote sitting at a desk all day and have new found weight for my poor feet to bare.
[n81nk9j] (score 6, diepte 0) Don’t underestimate bad shoes. I thought I had a foot disorder but now I’m wearing bogs and although they ache a bit at the end of the day, my feet are back to normal.
[n81zo7v] (score 6, diepte 1 OP) Wow I haven't seen a kiosk like that in years and even then i never tried it. didn't know they were still around. I'll be on the hunt for one tomorrow.
[n81ua8y] (score 6, diepte 0) When I worked on Amazon FC, the first 3 months my feet killed me. 

I got compression socks and the plantar fasciitis things from Walmart, i would put on the compression socks, then the plantar fasciitis things, and the I got really good passed socks (Dickies socks are dreams). Also I would come home, soak my feet in warm Epsom salt and I would roll my feet on rollers. Sometimes I would ice them too. It sucks, I only worked at Amazon for the benefits, LOL.
[n81mlvk] (score 5, diepte 0) I sit on my ass in a hostler, day cab, or in the guardshack
[n81n0pl] (score 5, diepte 0) It is not so much about you standing in one place but how often you stretch you can buy $300 work shoes (not available in zappos) with insoles that won’t do much for your body so do stretch yourself every hour that will make a big difference if a pa or am gives you a attitude do remind them that is part of Amazon safety policy to stretch yourself as often as u need that is posting on those weekly posts
[n81qjyp] (score 5, diepte 0) The beginning always sucks, but I’ve found the Airwalks and Vans to be the most comfortable, even with their stock insoles
[n81ub8q] (score 5, diepte 0) I wear Caterpillar boots.  Work boots made by a work boot company, not a sport shoe company are going to be better for work.  The "Excavator" model of boots are comfy to me.  I order the wide version, and stack either an Ariat Power Support insert under it, or the free Protalus one from zappos also works.  The Power Support has a stiff arch support that helps both support the arch, but also distribute more weight off of the ball and heel of my foot, lowering the pressure on those points.  

They're not as light as reeboks, but my first pair is 6 years old, and I wore them until this year.  If possible, get a second pair of shoes, and rotate which pair you wear each day to work.  This lets them dry out all the way between uses, and lets the foams recover a little longer.  Currently, I have 4 pairs of boots I rotate through from working at amazon for too long, and 2 pairs I've "retired" to lawn work.
[n82ojc4] (score 4, diepte 1) $20 a pair is insane but I second the recommendations for good socks. When I started I noticed my composite toe work shoes tended to rub the sides of my toes even with extra wide ones so I started double layering regular socks and then bought some nicer, thick athletic socks and it makes a big difference
[n82j2g2] (score 4, diepte 1) Kinda crazy that one of the most profitable businesses in the US can’t help us getting proper fitting insoles. They would rather push the dogshit ones that are they profit off of from Zappos
[n81n3me] (score 3, diepte 0) As someone who got that plastil thing on my feet . The sad truth is it never really go away. Use icy hot when you’re home before sleep, use pain cream on your feet before work. Take a Tylenol when it’s too much . Make sure you rest and drink lots of water
[n824ckw] (score 3, diepte 1) Just bought some and wore them today for my shift and i definitely think they helped.
[n81pz9o] (score 3, diepte 0) Insoles can help so much. I had to take the ones that came with my shoes out and double.If it's your heels bothering you, try these or something similar. I seriously had to double them up with another type that only go halfway through my shoe, but it helped tremendously. Also, finding a shoe with big toe box for more room helps so much. Best of luck!

https://preview.redd.it/6khhfzp10bif1.jpeg?width=1080&format=pjpg&auto=webp&s=f1deeda7fb580c32dad4563ef13a66712feaee5d
[n81zr9c] (score 3, diepte 2) Always 2 pairs of socks
[n81wr2s] (score 3, diepte 0) I recently just discovered a hidden gem on Zappos.. “Ugg Insoles” are literally amazing.. it’s furry and soft and feel so comfortable on my feet honestly my feet never hurt anymore and I take around 15-20k steps a day “I’m a male by the way if anyone is saying the Ugg insoles are for women, who cares they can see what’s inside your shoe lol” only thing is I paid out of pocket for them but it’s definitely worth the investment.. only like $30
[n81wxtw] (score 3, diepte 0) Massages/heat/ice and time. Standing is harder on the body than walking. Make sure to utilize the stretch breaks. I have a foot massage at home and soak tub I use after shifts, and I also do ankle/leg/feet stretches. After a few more weeks the pain should subside, just take care of your feet!
[n825uyd] (score 3, diepte 0) Lidocaine topical cream.
[n8277ze] (score 3, diepte 0) I wear compression socks AND thick work boots socks. The wellness place in our facility will give us new insoles when ours get bad, they’re Dr Shoals(I know it ain’t spelled right but my technical degree was diesel tech not English). I got my shoes from Indestructible shoes. Not Zappos. I’m a curvy lady who has lost 60 pounds since I started at Amazon and I am still classed as morbidly obese on the BMI charts. So I feel you on the foot pain.
[n81nnag] (score 2, diepte 0) you’ll get used to it when i started i used to suffer walking to my car end of shift i can’t remember if it was my back or feet that used to hurt really bad when i first started but i remember it was torturous to even trek to my car. now im almost three years in and i can walk from here to the moon and my feet don’t hurt. my back hurts eos sometimes cuz i been having back pain recently but ive been going verrryyy gingerly on myself lately and taking extreme care not to injure my back any more and i think it’s almost fully healed now. had horrible back pain for a while recently.
[n81wziu] (score 2, diepte 1 OP) I will purchase some before my shift tomorrow. I forgot to mention my ankles get swollen towards the end of my shift so the compression socks will be helpful.for that as well I'm sure.
[n827g98] (score 2, diepte 1) Timberland radius knit w/ the doctor Sholl's "custom" insoles. Until I got those, I **had** to wear these arch support foot braces that wrap around your foot. I also picked up a bag of ice on my way home from work to ice bath my feet before bed. It's the only thing that helped
[n81t6k9] (score 2, diepte 0) Timberland Pros work best for me. I haven’t felt any foot pain since I started wearing them.
[n81yq0y] (score 2, diepte 1 OP) I'm sure it does! It's a work in progress. It's one of the reasons I decided to step away from the WFH desk and get an active job again.
[n82gf1j] (score 2, diepte 2) Wellness and the massage area are separate in my FC. Ours first floor massage area is by the north side break room along with Learning, Safety, and PXT. Our wellness center is on the other side of the entrance from our massage area. Ask a manager or PA where yours is. They can tell you. Just be sure to specify that you want the area where you can massage your feet and not necessarily where injured associates are taken for medical care because they may be separate areas in your building too.
[n83s7gj] (score 2, diepte 2) It’s separate - self service
[n81zckj] (score 2, diepte 0) The correct shoe/sock combo that works for you is key. Unfortunately, it does require trial and error.
[n821d04] (score 2, diepte 0) If you need a wide toe box-Timberland pro isn’t the shoe. They tend to be narrow in the toe area, even if you get wide. I switched to Keen ( the ones you just slip on) Wider for toes. Big difference and my feet don’t hurt. I did change the insoles, luckily I still had a pair of the ones from the kiosk. Good luck, with your shoes.
[n821zf6] (score 2, diepte 0) Not sure if u do this but micro stretching the stretches from standups help. I used to be in a lot of pain too. But I learned to start doing stretches we're taught from standup at different times mostly towards the end of the day it helps and also Epsom salt is your bestie in my case the first six months. It took me at least a year to get adjusted but I was a receptionist before amazon lol
[n8236xy] (score 2, diepte 0) What made you leave being a mail carrier at the post office, as a former clerk we were peasants compared to y’all 🤭
[n824h8l] (score 2, diepte 0) Man I first day, I remember I was limping out into the parking lot LMFAOOO
[n82dwcz] (score 2, diepte 0) https://preview.redd.it/p4dauqtvxbif1.jpeg?width=3000&format=pjpg&auto=webp&s=1189ded5c48228e32d0b298a751c1464cf3d4d22

Two pairs of socks is the way. I use stretchy diabetic socks covered with ankle socks Google "runners knot" or "ratchet shoelace knot". I keep the very top of my laces tight to hold the heel in, and loosen the further down ones.

Get wider shoes if you find that you get blisters/calluses on your toes.

The insoles are nice too, but it really is a gamble if they'll work for you or not. Most importantly, staying off your feet when you get home... And on your days off.
[n82e7xv] (score 2, diepte 0) Rockport safety shoes and copper fit insoles. Reebok's are the worst. I had Reebok's as my first pair and it felt like I was wearing cement shoes.
[n82icfm] (score 2, diepte 0) Drinking water and improving my diet helped a lot actually. Maybe the increase in protein helped with muscle recovery, maybe eating more whole foods helped reduce inflation and joint pain, or maybe eating healthier in general improved my energy levels, idk. Regardless, I definitely notice a difference in how I feel day to day when eating mostly whole foods versus going home everyday and throwing a frozen pizza after work.
[n82lorg] (score 2, diepte 0) I needed this
[n83tmz3] (score 2, diepte 0) The smartest move I ever made was walking into the Red Wing store and buying a solid pair of composite toe work boots. Now I can put in 30,000 steps a day and my feet feel just as good at the end of my shift as they did at the start.

I see so many people complaining about foot pain—most of them are wearing the cheap “free” safety shoes that come with the job. The truth is, you’re allowed to buy your own. A good pair pays for itself fast. Mine covered their cost in the first week because I could work harder, longer, and more comfortably.

I’ve tried countless Zappos safety shoes, but they start hurting within 45 minutes at home. A proper pair of work boots is a total game-changer.
[n84xluv] (score 2, diepte 0) Double layer insoles. Use cold pack lacrosse balls and elevate your feet at home. Use a ball at work too on break. do micro stretching during your day and don't neglect you full body.
[n8535we] (score 2, diepte 0) Wolverines!!!!
[n81lb6w] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.com/invite/t7jARCs) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[n81mw1v] (score 1, diepte 0) Buy real walking/ running shoes dont be cheap  asics hoka shoes
[n81pnvp] (score 1, diepte 0) the soles i got are good but honestly you just get used to it
[n81zco7] (score 1, diepte 1 OP) I had these in my hand first and switched them out for one that said something like all day work. I'll try these instead. I did try to double up but it pushed my toe knuckles up too high against the shoe. I didn't even think to cut it shorter. My heels are the biggest issue so that's a great idea
[n81qvh0] (score 1, diepte 0) They dont
[n81qy61] (score 1, diepte 0) If you didn't break in your shoes over a couple weeks before wearing them to work, it'll make your feet 100x more painful. Break them in a couple hours at a time over a week or two amd then wear them all the time. Until then, keep a couple pairs on you all the time and switch them out during the day. Wear the toe cover things for your shoes if you have regular sneakers. Sometimes they won't even say anything if you wear regular shoes in recieve. Depends on your building.

Personally, I've always used skechers max cushioning and they do wonders for my feet. If your shoes aren't working for you, just clean the dust best you can and tell zappos hey I need an exchange. Make sure you look around the whole site and compare reviews only to what you need.
[n81r2ht] (score 1, diepte 0) They aren’t.. hope this helps
[n83cpnj] (score 1, diepte 1) If it's the sneakers I had them fall apart after 3 months.
[n81rxc0] (score 1, diepte 0) Easy. Mind over matter.
[n81tvue] (score 1, diepte 0) Adjustment takes time. Micro stretches help from time to time.
[n81u8sc] (score 1, diepte 0) 1. Wear thick wool socks. 

2. Wear them in the shower and until they dry when you first get them. 

3. It's ok to take your boots off, but not your socks, during break. If your feet are really hurting.
[n825uu0] (score 1, diepte 1) I'm definitely going to try this. All this is excellent advice.
[n81ur3e] (score 1, diepte 0) Epsom salt foot soak after work , bring a pair of slides or sandals to keep in your car .take your shoes off as soon as your shift is over and wear the slides on the way home .
[n81vob6] (score 1, diepte 0) I water spider for decant but after doing amazon for years its not bad, give it a month
[n81wczo] (score 1, diepte 0) Drugs.
[n81xcd2] (score 1, diepte 0) I go to the wellness aand massage my feet for 10mi. Every break. I’m  in the same boat and going to an acupuncture tomorrow, I have a kineon for my knee - just used it in my ankle, foot area  after my first 4 day shift. I got the high arch so will be trying out PowerStep High Insoles with the w/ Reeboks - I started with the keen high ankle composites but stabbing pain had me wonder… glad to know it’s probably just my feet/ankles and not wearing work shoes since 2018.
[n8205ss] (score 1, diepte 1 OP) I know wellness exists but we weren't taken there on our tour. I'm not even sure where it is exactly. Can you just walk in? If so, I'll try to find it on my first break tomorrow. I would assume its quite nice given the tacitly I work at is brand new.
[n81yeuk] (score 1, diepte 0) Merino wool thick hiking socks for padding and timberland anti-fatigue replacement insoles for comfort
[n81zpeo] (score 1, diepte 0) The shoes 100% matter. I suggest skechers
[n820u7b] (score 1, diepte 0) Tramadol lol
[n82217d] (score 1, diepte 0) The lighter the shoe the better. tylenol/ibuprofen. Standing in 1 spot is way different than moving around. Take regular mini-breaks to do circles at your area to switch up muscles used. Normally I stow, people think I look crazy doing it, but I hurt less at the end of the day.
[n822ox5] (score 1, diepte 0) Get a good pair of shoes! You can return it to zappos as many times as you need!
[n823hc5] (score 1, diepte 0) Insoles, you can get them for free with the credits that they give you for shoes

Its really not that bad though
[n824ux8] (score 1, diepte 0) it still hurts, you jus kinda get used to it overtime
[n8271wj] (score 1, diepte 0) 10.5 hrs is easy compared to when we did 12 lol
[n82b2sx] (score 1, diepte 0) It just takes time to adjust. I remember the first 3 months, my feet hurt so bad. I used tiger bomb on my feet everyday. The warmth helped with the pain.
[n82d4lu] (score 1, diepte 0) biofreeze kinda helps for like 30 mins
[n82dwwd] (score 1, diepte 0) Just takes time, I’ve been working at Amazon for almost 5 years. The first few weeks were rough!
(41 reacties met lagere score weggelaten)

=== THREAD 1ayi8ac ===
SUBREDDIT: r/Costco
DATUM: 2024-02-24  SCORE: 594  REACTIES: 114
TITEL: My dad found a human foot in his Lays 54 pack
POST (source_id=post):
He is absolutely certain that it isn’t his foot. He even sent me a video of both feet and even his crotch for good measure. He’s going to the doctor next week for safe measures to make sure both of his feet are still in tact. He lost a few feet in nam, but he’s certain than he hasn’t lost any more since then. 

Just wanted to post this to warn any other potatatoe chip enthusiasts and to see if anyone had advice for  us.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kruyjqj] (score 284, diepte 0) Doritoes!
[kruz6b4] (score 181, diepte 0) Man. I'm too high for this right now.
[kruyryt] (score 102, diepte 1) And cheetoes?
[kruyxmv] (score 75, diepte 2) Don’t see any fritoes
[kruy0gc] (score 69, diepte 0) Damn. I hate it when body parts are included in my Lay's 54 pack of chips.
[krv06qo] (score 54, diepte 0) Definitely have your dad talk to a supervisor, escalate this to corporate, and keep escalating it until he cant escalate it anymore. 

Get a lawyer and be ready to own all the Lays 54 packs.
[krv38z7] (score 38, diepte 0) I’m an internet foot doctor, no need to check my credentials. I can definitely say that that’s a Vietnamese foot based on its construction. Definitely let Costco and FritosLays know that one of their suppliers let a foot through QA
[kruz59u] (score 37, diepte 0) That’s just Brett’s foot. He disappeared in the tornado.
[kruzer8] (score 23, diepte 3) Thanks a lot, frito bandito.
[krv05qh] (score 18, diepte 0) I hope he's only a few feet from the doctor's office. If he needs help paying his bill, he could pick up a shift at I-hop. I heard a woman lost her foot and changed her name to Eileen. You can't make this stuff up.
[kruy56r] (score 17, diepte 0) I believe this cause I see lots of Costco posts complaining about things in their food!
[krv1uu2] (score 16, diepte 1 OP) Ew, no! It was a video.
[krv2dx9] (score 15, diepte 2) And Lays Potatoe Chips
[kruzzo6] (score 13, diepte 1 OP) No, fear monger first ask questions later.

We must warn the people!
[kruznkm] (score 13, diepte 0) Rex Ryan would be thrilled
[krv1x7d] (score 13, diepte 0) #nofreefootpix
[krv4vwk] (score 11, diepte 3) Looks like free toes to me.
[krv21n0] (score 11, diepte 0) Ultimate shittoe post
[krv3eic] (score 11, diepte 1 OP) Hm, my dad got his feet replaced it nam… I’m going to need to wait to see what his doctor says before I start questioning my old man.
[krv3e3r] (score 9, diepte 0) Someone check with a dentist?
[kruzxjl] (score 8, diepte 0) I think he needs to see a spudiatrist
[krv23tt] (score 8, diepte 0) At least it wasn't a tooth 😂
[krv3mvj] (score 8, diepte 1 OP) He lives in a town of 78 people in Wyoming. His doctor is also his therapist, dentist, barber, mechanic, bartender, and lover.
[kruz0q1] (score 7, diepte 1) And Cheetoes, and Lay’s Pota-toe chips…and athlete’s foot fungus on all the wrappers!
[krv248o] (score 7, diepte 1) Better call Elias to check if he dropped this foot or not.
[krv1yzp] (score 7, diepte 0) A lot of dad jokes in Costco subreddit.
[krv3yxv] (score 7, diepte 1 OP) At least 3-4 feet. His legs were blown off at the shins so he needed both feet attached to his knees. He lost both feet and also got a couple feet shorter.
[krv2fwz] (score 6, diepte 1) The flavor count on the box is never accurate!
[krv36j5] (score 6, diepte 1 OP) What’s with the all caps? Do you mean God’s foot?
[kruznkp] (score 5, diepte 0) this is so stupid i love it lmao
[krv0stn] (score 5, diepte 0) When will the madness end?!
[krv20zy] (score 5, diepte 1 OP) So do you prefer Venmo or cash app? I promise to donate all proceeds to the owner of the foot once we track them down.
[krv26pb] (score 5, diepte 1 OP) I tip my Kirkland Signature hat to you good sir/madam.
[krv24vs] (score 5, diepte 0) Corn chips
[krv5nsu] (score 5, diepte 0) I actually LOLed.
[krv23aq] (score 4, diepte 1) Dirtytoes
[kruze1q] (score 4, diepte 0) Fake news
[krv1p2h] (score 4, diepte 0) Posting feet pics for free out here
[krv3kcf] (score 4, diepte 0) > He lost a few feet in nam, but he’s certain than he hasn’t lost any more since then.

How many did he lose in 'Nam?
[krv85q4] (score 4, diepte 0) It still looks really fresh, which is what I expect from Costco's meat department.
[krv2nzn] (score 3, diepte 3) 😱
[krv1pp4] (score 3, diepte 0) Your dad sent you a picture of his crotch?
[krv2d8k] (score 3, diepte 1 OP) He actually said that the Fritos were missing from this box, perhaps it was an honest mixup in the factory?
[krv28kp] (score 3, diepte 0) Dorfeetos
[krv2n91] (score 3, diepte 0) Foot-O-Lays on OnlyFans would like their pic back.
[krv2u73] (score 3, diepte 0) Why did you post this? Now EVERYONE will want a foot in their Lays pack!
[krv4eyl] (score 3, diepte 2) Damn.  The agony of de-feet.
[krv5bbv] (score 3, diepte 2) U guys live in Texas?
[krv53cw] (score 3, diepte 0) It’s not a bug, it’s a feeture.
[krv66d4] (score 3, diepte 0) by our powers combined we can rebuild him
[krv93tm] (score 2, diepte 1) Maybe someone else could help him foot the bill
[krv1vaz] (score 2, diepte 0) Must have cost an arm and a leg
[krv2jtu] (score 2, diepte 2) This will never get old 😭I’m sad the mods deleted the other post.
[krv21v3] (score 2, diepte 0) Sauté it with butter and Cheetos. Serve with toast and red wine.
[krv23wn] (score 2, diepte 0) Footatoes!
[krv2pks] (score 2, diepte 0) 😂😂😂😂
[krv2qs5] (score 2, diepte 0) You're gonna want to cook that foot low and slow. It's tough meat. So either braise it, or if possible, skin and smoke it around 250f until it reaches 195-205f internal. You may with to wrap it in butcher paper when it gets around 160f to get it through the stall. Be sure to rest it for at least an hour after it is done.
[krv30qr] (score 2, diepte 0) But is it HIS foot?
[krv3dre] (score 2, diepte 0) Oh God guess which body part is next ...
🍆🎁
[krv3h63] (score 2, diepte 0) All I found was a finger. No fair.
[krv5ows] (score 2, diepte 3 OP) God dammit u/idiotsluggage
[krv3rwq] (score 2, diepte 0) This is just the kind of thing we freaks over at /r/vinyljerk get off to.
[krv3wk9] (score 2, diepte 0) Did your dad look to see if his own foot was missing? That's how the crown in the egg roll turned out!
[krv43pf] (score 2, diepte 0) Mmmmm toe-mato flavor... Some call it ketchup(my fellow Canadians know)
[krv4bbp] (score 2, diepte 1 OP) Except this foot is fully undressed.
[krv44rj] (score 2, diepte 0) I call BS, there’s like 2 bags of potatatoe chips in there, max. OP is a fraud
[krv4k7f] (score 2, diepte 0) Nice! Looks fresh!
[krv5koh] (score 2, diepte 1 OP) Crazy enough, he said it still had a pulse!
[krv4wrn] (score 2, diepte 0) Bonus!
[krv5iov] (score 2, diepte 0) Oh dang, that’s where I left it.
[krv5jyv] (score 2, diepte 0) You're sure he didn't slip into the box while trying to steal a pack and just didnt realise it?

 Summon the podiatrists of reddit!
[krv5qv7] (score 2, diepte 0) Why is his foot flicking me off
[krv5tk1] (score 2, diepte 1 OP) IT ISNT MY DADS FOOT!
[krv62mb] (score 2, diepte 0) I am enjoying this.
[krv6frr] (score 2, diepte 0) Don’t know what’s going on but something’s afoot
[krv6g66] (score 2, diepte 0) This is brutal. Imagine if the guy really did find a crown. 
Thinking it would be in the news? A dna test needs to be done with the father and the ‘crown’
[krv6t3c] (score 2, diepte 0) 🤣🤣🤣
[krv6wlz] (score 2, diepte 0) Gross
[krv6x0u] (score 2, diepte 0) What the fuck is going on here?
[krv7gyj] (score 2, diepte 0) I know the referenced post 😂
(31 reacties met lagere score weggelaten)

=== THREAD 1d17rjk ===
SUBREDDIT: r/AmazonFC
DATUM: 2024-05-26  SCORE: 237  REACTIES: 114
TITEL: Gotta hand it to all you stowers out there. You really keep us Afms on our feet
POST (source_id=post):
Not sure whether to be mad or impressed by this one. But special shout out to the one who improperly stowed this. And if it was a picker that didn’t put in back in correctly. You suck you’re better than that

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l5s29cv] (score 82, diepte 0) Someone definitely just wanted to see the pod fall over cause ain’t no way
[l5sh95j] (score 78, diepte 0) Do you love causing chaos in the workplace ?
Could you give 0 fcks about standard work or policy?
Would you prefer to be stationary & huddle and chat with fellow co-workers and listen to loud music with indulging on Takis & Snaks?
Are you unorganized and love to just throw shit around?

Well, come be a Stower with Amazon ?!
 
Where you can clock in and do the bare minimum without consideration for how your work affects others !! 

Pls Apply 🙏 🥳
[l5s8587] (score 41, diepte 0) I thought yall were exaggerating but a few weeks ago I was in pick and a pod almost fell on me but and my dumbass didn't move I just put my fists up ready to throw down with it lmao God that's scary. It wasn't the stowers fault the pods just kept hitting the metal rail for some odd reason until one hit it hard enough to lean towards me. The AFM had no reaction when he arrived and I didn't report it so I'm just glad I didn't have to beat up a pod
[l5sftbm] (score 32, diepte 1) Definitely…. But free break tho
[l5sdxva] (score 27, diepte 1) Nah you need to go back and show that pod who is boss. Don’t let it get away with that silly ass shit it’s trying to play. It’s just testing you until the day it strikes!
[l5ta41w] (score 16, diepte 1) Damn now it makes sense why they don’t allow me to stow…..I actually do the job with Pick and Amnesty in mind and can still make rate or close to it…..
[l5sswrl] (score 16, diepte 0) Icqa simple bin count here. When I tell you that people that stow have brain. (Some not all) it’s clear how they stuff the pods away. I mean, I’ve had boxes that are three times the size of the pod sticking out. What on gods earth were they thinking? And because I’m doing simple bin count I actually can’t even do anything about it except for make it look “nice” again… can’t look nice if the box is sticking out. And then they’ll put three boxes in there that can’t fit.
[l5skyps] (score 15, diepte 0) Am currently a stower at BDL4. This picture is something I've seen many times and I just keep wondering... who taught these people to stow???

Also hysterical when it does happen.
[l5ve21t] (score 14, diepte 1) I see this 10+ times a day. This very rarely causes a pod to fall over and this is done just because stowers are terrible at their jobs.
[l5sjq6y] (score 14, diepte 1) Those pods can weigh up to 3000 pounds. I know you’re a savage, but that’s not the smoke you want big dawg.
[l5sggbw] (score 13, diepte 2) But I wonder if you’d get walked out for fighting a pod?
[l5sglg1] (score 11, diepte 3) Sounds like a win win situation to me.
[l5suisu] (score 11, diepte 1) OMFG! Haha accurate af.
[l5t1jjy] (score 11, diepte 0) Blame the fucktarded executive who decided new hires only needed 5 hours of training with an actual person.   
And I’ve never understood why they don’t ding people for this.  I know that you can see who put the item in the bin in the inventory history for the bin.
[l5t4mof] (score 10, diepte 1) I agree. Lazy/careless stowers are the worst.
[l5sj6kw] (score 8, diepte 0) That was me, I’ll admit it
[l5sodde] (score 7, diepte 4) For real, win for a paid day, and win for the personal injury lawsuit.
[l5t03p1] (score 7, diepte 3) In my FC, a pod should be about 750 - 800 lbs when fully loaded.
[l5sb24y] (score 7, diepte 0) I used to hate new stowers. It felt like they dropped 50% of their items on the floor
[l5sgnjx] (score 7, diepte 0) Gotta love Stowers.....🙄
[l5t4h49] (score 7, diepte 0) https://preview.redd.it/whdvv7j8pu2d1.jpeg?width=3024&format=pjpg&auto=webp&s=c2457fc5fb6f06ad730966eeec6d6bfe5e30e4e6

Sabotage
[l5tt14o] (score 7, diepte 1) It’s literally not even in the bin.
[l5sogw4] (score 6, diepte 1) 😂
[l5sukhe] (score 6, diepte 2) 😭
[l5suwnv] (score 6, diepte 1) When I was hired I received no training from my LA. He just talked about himself and later on was a huge asshat. However when I did pack training, it was training.
[l5trvme] (score 6, diepte 1) We can actually see who stowed it. We do dirty bin audits (HRR’s) and also STU’s(bin etiquette) for this.  We can trace the bin and the item back to who stowed it, then watch dig dug footage of them actually stowing it.
[l5uduvi] (score 5, diepte 2) It was me
[l5um2yv] (score 5, diepte 4) ![gif](giphy|6901DbEbbm4o0)
[l5udgvc] (score 5, diepte 5) 1000 lbs of phone cases, butt plugs, rubber wedding rings, and packs of water.
[l5ubgix] (score 5, diepte 1) yall call rme for that? ya gap time must be awful
[l5szt98] (score 5, diepte 0) Someone is having a conversation about last touch.
[l5szuqr] (score 5, diepte 0) As a fellow AFM, I have seen some things that have left me in awe of the sheer laziness of some people. I am so glad that in about a month, I will not have to see this stuff ever again because I am moving on to TOM team.
[l5ucmjb] (score 5, diepte 2) https://preview.redd.it/j6gydjxffw2d1.jpeg?width=3024&format=pjpg&auto=webp&s=8f3f44b154f1f31f853dbee083ad7cde37188162

Also That one was Funniest Pod Crash For me . Reason of that pod crash was overhanging items :)
[l5t5hcs] (score 5, diepte 1 OP) When two pods love each other very much…
[l5vkcgb] (score 4, diepte 4) Wow, good thing I only punch my co workers then.
[l5su5rn] (score 4, diepte 2) Those pods are way too easy to move if they are up to 3000 lbs.
[l5sjkix] (score 4, diepte 0) Ayo RME I got a pod LEANING off the drive. Pods out here sipping lean.
[l5t9yks] (score 4, diepte 1) I barely had any training with an actual person for stow. It was almost all training from the monitor, and it doesn’t even explain most things to you. I had to ask my managers so many things my first week
[l5tl6ul] (score 4, diepte 1) no the f we are NOT following that absolutely Absurd "last person to touch it" rule. 10 times out of 10, if stow was the problem, the picker and counter get the smoke and stow NEVER DOES
[l5tk990] (score 4, diepte 0) Thank the job rotation and the cutting down of the training on every pathway for that. Amazon just wants their warehouses to fail.
[l5ucn58] (score 4, diepte 1) Crazy how training went from 3 days to 3 hours
[l5u149q] (score 4, diepte 0) We get it. You are a cool AFM guy/girl. Look, if you don’t want to do the job, why not jump back into function and leave the AFM spot for somebody else? Ready for the downvotes from the stow-hating circlejerkers.
[l5tvrpz] (score 3, diepte 3) Sounds like it’s time for a face off, how many people we need to get together? We will take them all on!!!
[l5tw4ni] (score 3, diepte 4) In training I was told the maximum capacity was 1000 lbs, including pod weight, but they only store 700-800 lbs in each to reduce chances of the pods being unstable.
[l5va2an] (score 3, diepte 3) The training says up to 3000 pounds. When we lift them it can be extremely heavy. You have to barely get it off the ground just enough to slide it out with your foot. Trust me, it can be a real mf especially if it happens a lot in one shift.
[l5soan1] (score 3, diepte 1) All of the stuff that falls out or all the little shit is put under all the heavy ass boxes or it's all sticking out and the pods get stuck n now I'm stuck waiting not gonna make my pick rate I get it they have a quota to buy man a lot of it is awful and makes my job as a picker hell
[l5t02lo] (score 3, diepte 1) Try line loading for inbound. Have your back to that wall of freight and it decides to fall on you.
[l5t5l6o] (score 3, diepte 1) But Amnesty lazy af tho
[l5tqwnc] (score 3, diepte 1) 💀
[l5ulq8p] (score 3, diepte 4) Paycheck stays the same regardless.
[l5v8hdc] (score 3, diepte 4) I was thinking the class definitely said to refer to RME. While I agree it’s easy, why would I do something that I am told not to; that makes my job easier? If I were in an FC I could see just wanting to get it done so you can get off the floor. But I’m at an SSD where you are the only AFM because the floor is a quarter of the size. So RME responds quickly and we are directed to be off the floor as much as possible to avoid added congestion so we do not miss CPT. So yeah RME can handle dat.
[l5t0gmp] (score 3, diepte 2) It all depends on the individual learning ambassadors. Some are great and others just do the bare minimum. When I got hired in 2019, I had excellent learning ambassadors (one of which is an AM that worked his way up from tier 1 to AM within 3 years and is a good dude). Then covid happened and training never quite recovered.
[l5sppnu] (score 3, diepte 0) Noice
[l5vj2yj] (score 3, diepte 1) Some are more concerned about hitting rate then taking the time to see what fits
[l5swlho] (score 3, diepte 0) i stare at their soul when I caught them while im auditing lol
[l5t1ig7] (score 3, diepte 0) This happens all the time. What annoys me they should be able to find out who stowed it and give them at least a warning.
[l5t5d58] (score 3, diepte 0) Them Pods wanted to have an excuse to have the “day off” I see. 👀💀
[l5vecsz] (score 2, diepte 3) Yes, you’ll get walked out if you’re seen hitting a pod. You’ll be walked out of you punch the bottom of a box to break it down, hitting a pod is no different.
[l5tvlrk] (score 2, diepte 2) Damn it I didn't get the pod number it could be any one of them just waiting to strike again 
*
[l5unqex] (score 2, diepte 6) For real. Everything overstuffed so the water burst and gets on everything causing a crash which shoots out wet dildos and butt plugs everywhere.
[l5vgyw6] (score 2, diepte 4) Max capacity on R drives is 1200lbs if I remember correctly. No shot it's 3000
[l5tuzln] (score 2, diepte 2) Yeah it sucks that's why I would like to be trained in stow but they have too many I think
[l5tvda5] (score 2, diepte 2) Nah fuck that bruh that's death if no one can hear you scream for help
[l5v1w1n] (score 2, diepte 2) Facts I used to put item on floor and they’d keep clearing the andon and leaving it there 😂
[l5ui3bn] (score 2, diepte 2) We have to if the pod is hanging off the drive. At least at our site.
[l5v84cd] (score 2, diepte 3) They say you have to call RME for a leaning pod at every site but most responders know they can just fix it on their own
[l5ss8l5] (score 2, diepte 0) Glad to be of service  🫡
[l5stp13] (score 2, diepte 1 OP) You make us all proud to call ourselves Amazonians. Respect to you sir.
[l5sufjj] (score 2, diepte 0) I know that the expectations for stowers are ridiculous but come on now yall. This is way too much.
[l5suivq] (score 2, diepte 0) Luckily my site has an excess of stowers so they're all getting VTO'd outta here.
[l5szdke] (score 2, diepte 0) nothing like a little jousting between the boys
[l5trjfy] (score 2, diepte 1) We do, HRR(dirty bin audits)
[l5uph18] (score 2, diepte 3) When you call Amnesty, have them do a dirty bin audit before they remove the overhanging item. This is what makes the HRR and records the pod, the bin and the asin. It traces back to who stowed it. Then they get an HRR and their manager will come explain FOO. Or, if it triggers an IRDR STU, quality will. These are all verbal coachings, enough of them will lead to a written.
[l5t5b9t] (score 2, diepte 0) No phones allowed on the operations floor.
[l5t7251] (score 2, diepte 2) Too bad I don’t get to see any action while I’m picking……
[l5tc7sn] (score 2, diepte 0) Blame management, blame the numbers were being asked to put away, blame the pod capacity blame the last person to touch it rule, then we could blame the stower. I’ve seen worse but this ranks up there.
[l5tjp0u] (score 2, diepte 0) Amazon doesn't deserve anything but the absolute worst, I hope this is an ongoing daily issue.
[l5ubfq2] (score 2, diepte 0) appreciate the 10 minute break waiting for the people to come and move it
[l5we1dm] (score 2, diepte 1 OP) Don’t let the QB/management/safety hear you do that. At my site it’s a Cat 1 Safety Violation that is grounds for immediate termination and perma ban from ever working at Amazon. Just looking out homie
[l5s0hl5] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.com/invite/t7jARCs) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
(45 reacties met lagere score weggelaten)

=== THREAD pvjrqk ===
SUBREDDIT: r/AmazonFC
DATUM: 2021-09-26  SCORE: 78  REACTIES: 113
TITEL: Feet pain.
POST (source_id=post):
Yes all our feet hurt after our shifts I get it but what products do you use to reduce the pain? I got compression socks,comfortable shoes and I changed the insoles of my shoes as well and that helps a little but what else can I use?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[heajfho] (score 39, diepte 0) https://www.amazon.com/gp/product/B01LZQH9S1

https://www.amazon.com/Dr-Scholls-Massaging-Absorption-Cushioning/dp/B01M7VGCTI

https://www.amazon.com/Heel-That-Pain-Clinically-Guaranteed/dp/B07FL92L1G

https://www.amazon.com/adidas-Mens-Kaptur-Sneaker-Black/dp/B07KTV9YKW


I use those shoes with that insole, I used the original insole to trace the cut of the dr scholl as good as possible. Then I wear two of those socks on each foot and put the heel gel inbetween each sock to hold it in place. Originally it made my shoe really tight but after wearing it for a while you break it in and it will loosen up.

This setup is really great for walking if you have to walk a lot, however if you have to stand I would recommend only wearing one sock on each foot and no heel gels.

The extra sock helps deal with cushion when walking and the gel keeps your heel tinder and soft. If you stand on those gels all day it will hurt but it will hurt slightly differently then if you stand without them so if you want a mixup of pain then go for it.
[heai755] (score 31, diepte 0) One of my coworkers brings 2 ice pack blocks and at lunch he puts them under his feet while he eats. Says it works wonders for him and he's a big dude.
[heamr6x] (score 21, diepte 0) Get a foot massage I pay $30/hr for a foot massage once a week it works wonders.
[heb8oze] (score 12, diepte 5) You ought to see if Nike is hiring. They would do well with an enthusiastic employee like you.
[heasanf] (score 9, diepte 0) Brooks. First time I wore them, I realized about half way into shift that my feet didn't hurt at all. I think I stared at them like a dumbass for about 15 seconds. I was in shock.   
They're pricey, but you can find sales fairly often. Also I've seen them in the fancy Goodwill "Boutiques" that've been popping up. Don't know how well they'll work worn tho. I'll find out soon as I find my size.
[heawww0] (score 8, diepte 0) Compression socks every shift combined with Adidas UltraBoost, Nike Peg 38, multiple Hoka styles, Nike AF1. I don’t use insoles. I have a very high instep. If you have foot pain, a visit to a podiatrist is highly recommended. I do have custom made insoles but the mentioned shoes above don’t require them.  One last thing: Vans make a comfy cush sneaker that’s outstanding.
[heam71a] (score 7, diepte 1 OP) Thanks!! Will check em out

Edit: does the heel thing work with the insoles??
[heanglh] (score 7, diepte 1 OP) I got Adidas ultraboost 4.0 and they’re ok they start hurting after the last 3 hours lol
[heao9nc] (score 7, diepte 0) Superfeet insoles, stretch constantly, invest in some Epsom salts. My recommendations are ultra boosts and Nike epic reacts. I average 25-30 miles a day while working at Amazon and owning a husky. Feet haven’t hurt once until I started wearing safety shoes :(
[heas67v] (score 7, diepte 4) If you wanna know real pain wear safety shoes for a week. Coming October 1st they will be a requirement for all AMs at my FC. I developed plantar faciatis after wearing them for roughly 4 days. Constant foot pain ranging from a pain level of 5-8/10 throughout the day 😑
[heaotg6] (score 7, diepte 1 OP) I’m 160 😥 I work out regularly as well
[heb8gfv] (score 7, diepte 1) I needed to hear this. It’s not that I’m in denial, it’s that I need to know that it will get better. I’m already down 12 lbs.
[heapnbs] (score 6, diepte 0) Hoka Bondi 7. Pretty much any Hoka shoe. I know people that also use the Rincon. Way better than the other ‘major’ brands.
[heant3d] (score 5, diepte 3 OP) What shoes you got lol like the specific type lol there’s air max premium and stuff like that lol
[heaqaxl] (score 5, diepte 0) I bought one of those massage balls for my feet and the use it for 10 minutes before and after work and it helps significantly
[heeo4mi] (score 5, diepte 0) I wear heelys
[heaw077] (score 4, diepte 0) RICE
Rest. Ice. Compression. Elevation
[hecrwr1] (score 4, diepte 1) Lol rest when?
[hed71r5] (score 3, diepte 1) Omg thank for this info. I’ve been wondering what more I could do save my feet.
[heclptq] (score 3, diepte 1) I wanted to say this but wasn't brave enough until I saw your post.  I got into intermittent fasting, took off 11 pounds, and it made so much of a difference!  I sleep better too without a full stomach/gut
[heaykq9] (score 3, diepte 1 OP) I’m a picker I don’t walk :( and actually walking makes my feet feel better lol
[heb31g1] (score 3, diepte 1 OP) Wait can you link the ones you have :) if you don’t mind :)
[hebxveu] (score 3, diepte 0) I put my feet in ice water for 15 to 20 minutes when I get home, and that helps a lot with the pain.
[hebybo8] (score 3, diepte 0) I got insoles for my shoes and that helped, but overall I notice my feet + legs hurt WAY less if I remember to stretch before/during/after my shift. I've been forgetting the past couple weeks and my legs are not happy lol
[hect7hq] (score 3, diepte 1 OP) No! Just did a physical last month!
[hedzlq0] (score 2, diepte 2) Yes, the shoe will be tight at first but once you break it in a little bit, few weeks or so it works fine, at least that has been my experience. Sometimes I just wear the two socks without the gel, its not something you have to use everyday. 

I find I naturally walk faster with the gels. However, wearing the gels for many days in a row can cause some discomfort too. 

I would recommend you definitely replace the insole that comes with the shoe, it's no good.

The gel is just extra that helps me with walking.
[heaoq8x] (score 2, diepte 5 OP) Ima get a pair when I go to the mall lol I gotta see which one is more comfortable lol
[hebnzvb] (score 2, diepte 8) lol
[heavp84] (score 2, diepte 3) Or just find the most comfortable cheap pair at ross, my Adidas with Yeezy sole design are good even if I walk 24k steps
[heb7mjj] (score 2, diepte 1) Our FC is requiring safety shoes :( I would love to just wear sneakers
[hearuhh] (score 2, diepte 3 OP) True lol I just needa go find my pair
[heb9utv] (score 2, diepte 5) This. I'm hearing about people wearing regular running shoes. I had to wear safety shoes from day 1.
[hecxe8o] (score 2, diepte 1) This would be my second recommendation after Hokas
[heaucb8] (score 2, diepte 0) I invested in Oncloud shoes that have helped ease pain. Otherwise I purchased a foot roller to roll out my muscles and when it gets really bad I use tiger balm and foot soaks.
[heavegc] (score 2, diepte 0) Get good shoes I don't use pads just Adidas and puma that are sport and comfortable, can walk 24k steps a day without issue
[hee9j72] (score 2, diepte 2) After work I'm assuming. I can attest to compression socks and elevation of the feet after getting home.
[heb2hot] (score 2, diepte 1 OP) I’ll try those lol
[heb3nhl] (score 2, diepte 2) worth every penny, my feet used to scream @ me

Z-Liner Orthotic Insoles - Full Length Inserts Engineered to Maximize Foot Health & Comfort, Reduce Fatigue, Relieve Foot Pain, Shock Absorption & Cushioning (USA W11.5/M10) https://www.amazon.com/dp/B07KPKX81L/ref=cm_sw_r_apan_glt_fabc_9KEDMWNS0D6EM5XSQCH4
[heb46i4] (score 2, diepte 3 OP) I got em :) thanks!! Will try them out
[heiffla] (score 2, diepte 1 OP) Just got the z liners right now and omg I can feel the difference already lol let’s see on Thursday how they go
[heijn75] (score 2, diepte 3 OP) My shoes feel even lighter as well lol
[heb8psp] (score 2, diepte 0) https://www.amazon.com/dp/B08LYV535N/ref=cm_sw_r_cp_api_glt_fabc_60T3P36V0RWY6X0KD7TP?_encoding=UTF8&psc=1

These are amazing. I also elevate whenever possible.
[hebdt09] (score 2, diepte 0) My feet are killing me lol. I'm on break rn. I know losing weight will help. But something that gives me IMMEDIATE pain relief is rolling a Frozen water bottle under my feet.
[hebdtzu] (score 2, diepte 0) Depends on your feet and how much walking you’re doing. I’m taking anywhere between 15k and 20k steps per shift. Adidas ultra boost, asics gel kayano and nike vapormax utility have all been really good for me. The asics have been the best by far though.
[hebea1h] (score 2, diepte 0) First find a comfortable pair of shoes that fit.  Then get a second pair, it takes awhile for the cushioning of your shoes to come back after a long day.  By wearing the every other day you give it the best chance.

I also got the Dr Scholls work insoles, and that pretty much help me through those MET months we had.
[hebfwxm] (score 2, diepte 0) When you get home, place feet in pan of cold water with ice cubes. It stops inflammation,  thus quickly diminishes pain. Also, if ur not allergic, take 2 motrin or any ibuprofen,  as soon as shift ends. 

Good idea about icing feet on breaks. Even if only 5 min.
[hebiv10] (score 2, diepte 0) Aleve.
[hebrh4n] (score 2, diepte 0) My first day I couldn’t get out of my car my feet hurt so much now I’m used to it. Dr scholls and comfy shoes
[heeu7kg] (score 2, diepte 4) Oohh okay lol. I usually get off at 6pm
[hebzej5] (score 2, diepte 0) Buy a foot bath with a bubbling feature and some Epsom salt or use ice packs/an ice bath on your feet after your shift
[hecoj5z] (score 2, diepte 0) Copying and pasting from a comment I made on another shoe post the other day:

I recommend these safety shoes. They're expensive but worth it. I wear 9.5 xx-wide and they fit great. 

https://www.orthofeet.com/products/cobalt-black-work-shoes

For inserts, I use upstep's "on my feet all day" inserts.
  https://app.upstep.com/products/on-my-feet-all-day-custom-orthotics

Don't cut corners when it comes to your feet/body. I know it's expensive but it's worth it. With this combination, I have no foot pain and reduced stress on my lower back.

Zappos selections are fine...it's the factory inserts that kill. Orthofeet has built in cushion so it's actually still comfy without any additions. I sound like a brand ambassador but the shit really works (at least for me lol). 

Hang in there everyone
[hedaip2] (score 2, diepte 0) i just wear vans compare to those safety shoes , vans just do me wonders
[hee62a3] (score 2, diepte 0) I use a Cbd rub
[hee6css] (score 2, diepte 0) Anyone got any tips for the knees. Mines are beginning to pop sometimes
[hee7g30] (score 2, diepte 0) After the shift… change into sandals
[heegxlz] (score 2, diepte 1 OP) I take my shoes off lol my wife drives on the way back home
[hefi82y] (score 2, diepte 1 OP) Lmaooo
[hefjcau] (score 2, diepte 2) just thought I’d clarify to use a massage gun on your feet as opposed to a machine gun. I guess that’s one way to solve having to go to work tomorrow!
[hedqi7t] (score 1, diepte 1) Definitely going to have a look at this stuff before peak season this year, thank you!
[heap3n0] (score 1, diepte 7 OP) No doubt I’ll let you know what pairs I get lol
[hebnzmd] (score 1, diepte 3) lol
[heavic4] (score 1, diepte 2) Adidas foam with the Yeezy design is very comfortable
[heb28d9] (score 1, diepte 2) I wear the 4.0s and I never feel pain.
[heaxppn] (score 1, diepte 1) I loved the air max but I carry rolling luggage behind me in New York City like at grand central and every time the luggage wheel would pop the air bubble.  Then at work a door closed behind me and the metal part popped the bubble.  I like the shoe and kept buying them but now I have four useless pairs.  I’ve seen the air max 270 and maybe they are a little more protected.
[heaox78] (score 1, diepte 1 OP) I got two ultraboot pairs the 4.0 is ass lol
[hearrih] (score 1, diepte 2) I like mine. One of the few pairs of shoes that I can wear without insoles 🤷🏽‍♂️ Everyone’s feet are different though.
[heb2ll8] (score 1, diepte 1) Fresh cucumbers - (anti-inflammatory)
[hebdo1o] (score 1, diepte 1) *Invest* in something thats $5
[heb2izt] (score 1, diepte 1) (they hate when you speak the truth)
[hecwhob] (score 1, diepte 1) Have to agree with the Hoka bondi 7 the 1st pair of Hoka I  got was the ariah but they only came in a 2E width got bindi 7's last Wednesday and wire them for 1st time ladt night and they are really comfy like walking on air especially with my feet problems. i.e. bone spurs and a  bone on my left foot that is out of place
[hed4n65] (score 1, diepte 1) Yes! Brooks changed my life!
[heb1zmd] (score 1, diepte 2) If that’s the case look up plantar fasciitis and see if that’s where it hurts for you.  If so, a lot of stretching is in your future (and maybe steroid shots).
[heb284y] (score 1, diepte 3 OP) I stretch 3 days a week maybe I have to wake up earlier and stretch everyday lol
[heb3kmw] (score 1, diepte 4) PF requires specific foot stretches.
[hefhsbh] (score 1, diepte 2) Lol.  Yeah.   After work.
[heb2bma] (score 1, diepte 0) Z-Liner insoles for the win !!!
[heijkg7] (score 1, diepte 2) Yeah - pull a whole week & not feel dead on your feet!  Win win !!!!!
[heb4umx] (score 1, diepte 0) New Balance shoes work great for me
[heb7ykr] (score 1, diepte 0) I like the Terra shoes from Zappos@Work because they have a very low heel height compared to others. They look basic and bland but my feet don't feel as if they're breaking in half when I clock out. I won't tell you they will work for you since everyone is different but my feet seems to like flatter shoes.
[hebp00n] (score 1, diepte 0) Massage gun
(32 reacties met lagere score weggelaten)

