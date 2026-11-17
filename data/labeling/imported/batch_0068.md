# Label-batch batch_0068

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
Schrijf het resultaat naar `batch_0068.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1nn20vt, 1gi1q0l, vdopf2).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1nn20vt ===
SUBREDDIT: r/AmazonFC
DATUM: 2025-09-21  SCORE: 119  REACTIES: 124
TITEL: The washing of feet in sink is so fucking disgusting
POST (source_id=post):
I don't care if its part of your religion, its pissing off everyone else, causing a safety hazard and pissing off everyone

People need to start calling it out to their face or it will never stop since management cant babysit the bathroom

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nfh9vt3] (score 70, diepte 0) Or multi faith room has a sink for that reason.
[nfhg983] (score 45, diepte 0) Also squatting on toilet seats to wash your butts with water bottles. I've seen them leave the stall to refill,🤢
[nfhjb10] (score 32, diepte 0) There are stations in the multi faith room for them to wash their feet. Why tf would they use the sinks in the bathroom 🤢🤢
[nfhr1gg] (score 23, diepte 1) That's so gross, omg I'd freak out. Is that why people are complaining about shoe prints on the toilet seat? 🤦🤦🤦
[nfhcvy1] (score 21, diepte 1) If you have poop and pee on your hands, you are doing something very wrong.
[nfhlk1a] (score 21, diepte 2) No. Some of the newer sites have sinks specifically designed for washing feet in the multifaith room
[nfhdcul] (score 21, diepte 1 OP) It does and they still make a fucking mess of bathroom, inside stalls and outside. Constantly dirty ass water everywhere
[nfhrvvd] (score 21, diepte 0) Fire these people
[nfha21k] (score 20, diepte 0) They don’t need to. Does your facility not have a multi-faith room and an ablution room?
[nfhuhh7] (score 16, diepte 1) Import the third world and well
[nfhe2n6] (score 15, diepte 2) mind you cups left everywhere that they can’t pick up, after doing their business
[nfhqa26] (score 12, diepte 0) The sink is made for handwashing. It is disgusting to put your feet in the fucking sink, it is not sanitary to put your feet in the fucking sink. It is a safety hazard, imagine how easy to slip and fall and break your stupid ass neck. It is disgusting.
[nfhaxwf] (score 11, diepte 1) We're also not wiping shit off our ass in front of everyone.

Amazon has private spaces for this exact reason and YOU as a grown adult should comprehend this by now.

![gif](giphy|jnQYWZ0T4mkhCmkzcn)
[nfhdz6i] (score 11, diepte 0) It would be nice of they would wipe the counters off after they are done. Water gets everywhere.
[nfhg10s] (score 11, diepte 0) They can’t understand the civilized society part just YET . It’s going to be a shit storm for yall areas for a the short term.
[nfhy5ux] (score 11, diepte 1) You’re okay with folks washing their feet in the restroom sink? Why on earth would you even need to be doing this at work?
[nfhsn6n] (score 11, diepte 1 OP) "but feet just ride around in socks and shoes" where they belong until you are in the fucking shower
[nfj77sb] (score 11, diepte 0) As a Muslim, I get it. It IS weird to put your whole foot in the sink, public or not. 

I ended up quitting because walking all the way to the multi faith room for each prayer to do the washing in the appropriate sink would cause my rates to go down and I’d get warnings. 

I refused to comprise my faith and also refused to go to the closest bathroom and be a weirdo who stuck their feet in a sink in a public place. So I quit. 

Maybe those people are in the same predicament as I was and don’t want to get in trouble for TOT. The real issue is allowing people to actually use the accommodations without being penalized for TOT.
[nfhpqsd] (score 8, diepte 0) Yeah that's going to be a big big problem! I don't blame you.
[nfhhmax] (score 7, diepte 0) Annoying for sure - but a far worse problem is urinals with urine puddles everywhere on the floor..
[nfhjyuh] (score 7, diepte 0) I’m sorry but this is a hella funny post
[nfj89es] (score 6, diepte 1) After fighting the mess my warehouse decided to finally just add bidet to every toilet and it cut down on that, I haven't seen a water-covered toilet or water bottles laying around in a while.
[nfhled9] (score 6, diepte 0) So people wash shit and piss off their hands but you get upset about someone cleaning their feet?
[nfim9wx] (score 6, diepte 3) They're not illegal most of them came as "refugees", which is why they can be hired at Amazon. Construction sites will push through 12-34-5678 social security numbers, Amazon won't.
[nfj3s2x] (score 6, diepte 0) I think those who wash their feet in the sink are preferable to those who don't wash anything at all anywhere.
[nfiza0l] (score 5, diepte 2) We have a full mother's room (not the pods) and multi faith room. My building is only 3 years old. So yes, the sink in there is for feet washing.
[nfj573l] (score 5, diepte 2) I’m Muslim and definitely use water to clean afterwards but I, and nobody else I know that’s Muslim, is literally squatting feet on the seat to do it. Whoever is doing that is weird ngl
[nfhp98n] (score 5, diepte 1) Sounds like the mess they leave behind, not the act. Everyone doesn't leave a giant ass mess when they do this
[nfiutx8] (score 5, diepte 0) There is no excuse for washing feet in the bathroom sinks. I had to correct a brother when I saw him doing this. I said our  prayer room has a place for that.
[nfjjeqw] (score 5, diepte 3) They can’t actually discipline you for practicing your faith. You quit for no reason as your TOT would have been excused any time a manager would come and ask you the reasoning behind your TOT.
[nfhrvcd] (score 4, diepte 3 OP) Thanks!
[nfhfijk] (score 4, diepte 0) I’ve never encountered that. I’d prefer that over all the nasty people not washing their hands after using the toilet, or leaving shit and blood all over the seat & ground.
[nfjq9o7] (score 4, diepte 3) The restroom sink is supposed to be for washing hands not feet. You’re not opening doors, touching handrails, or touching any one with your feet. 

Taking off your shoes and socks and putting them anywhere near that sink is just gross and unnecessary. 

Wash your feet in your own bathroom at your own home.
[nfhvshl] (score 4, diepte 1 OP) They already do


And if even if they didnt, dont put your dirty ass feet in the sink and wash your ass with cups of water in the stalls


Thank you
[nfiqmvz] (score 4, diepte 1 OP) Wtf? Most jobs do not have special rooms to wash your dirty ass feet in.


If they worked at McDonalds would they be washing feet in sink as well? Gross, uncivilized and not compatible with modern society.
[nfjg2d5] (score 4, diepte 2) Depends on the prayer time and the person, honestly. As you probably know, we pray 5 times a day. Many of us don’t want to delay a prayer before the next one comes in. So waiting to pray after work would make us “miss” at least one. 

Some find it sinful to delay a prayer, some just don’t want to allow anything, even work, to delay prayer, and others will pray after work because they believe work is a valid excuse for the delay.
[nfjmzfc] (score 4, diepte 1 OP) "Did YOU call it out to their face?"


Havent yet, people tend to get get very defensive and often violent when you call out their religious bullshit
[nfhc613] (score 3, diepte 1) They probably just ignore it
[nfhr7od] (score 3, diepte 1) That's a real safety hazard, report it !!!!
[nfjrtza] (score 3, diepte 5) Yeah you going so hard to defend this tells me you must have some gross habits of your own.
[nfiv11d] (score 3, diepte 3) Just because you come from the 3rd world does not mean you are illegal. These people will eventually learn what is acceptable and what isn’t.
[nfibw11] (score 3, diepte 0) It’s definitely never going to stop no matter what. A lot of stubborn people and to think this in particular would change is going to be a hard no unfortunately.
[nfijdoo] (score 3, diepte 0) How is it a safety hazard? Ive seen this complaint a lot, like how does it affect you? Youre not touching the sink when you wash your hands right? Youre not eating off the sink, so whats the problem? Seems like a weirdass thing to complain about.
[nfjfpjw] (score 3, diepte 2) Completely civilized, nor is it "not compatible with modern society". Tell me you don't actually know what the fuck you are talking about, without telling me
[nfj1ivv] (score 3, diepte 0) Well at least I can take solace in the fact it’s not just happening at my Amazon. I’ve walked in on dudes multiple times with their pants off washing their disgusting feet in the sink. Still remember the first time I walked into a stall and saw three partially filled cups of water on the toilet paper dispenser, and first thought man someone must have been really thirsty.. Then saw shit water all over the floor. Disgusting animals!!!
[nfkhfjz] (score 3, diepte 0) Bro everytime I walk into the bathroom theres always a Indian person just sitting on the floor next to the stall. Like bro wtf 💀
[nfjef40] (score 2, diepte 2) Can you explain why washing hands after toilet use is important, if not to remove faecal and urinary bacteria? The mere act of flushing a toilet aerosolises said particles. You're acting shocked people are finding forks in kitchens.
[nfhrfp3] (score 2, diepte 2) Happy Cake Day!
[nfk0m0e] (score 2, diepte 2) they won't do anything.

hair is supposed to be above the shpulders, yet they refuse to do anything about some guy with a turban who has his beard a few inches below his shoulders
[nfhz0qs] (score 2, diepte 1) Nah my FC has started giving out free water bottles and ever since then people have been doing this. The other day the guy in the stall next to me was splashing his ass water all over the floor and I could only think “If this splashed my fucking leg…”
[nfkm469] (score 2, diepte 1) They took the multi faith room out of our fc because 3 dude’s kept going in there to have sex.
[nfjg0nv] (score 2, diepte 3) ever heard of foot fungus?  Were you not aware that bacteria thrive in warm moist environments like the inside of your socks and shoes?
[nfjinsz] (score 2, diepte 5) yes at home in your own shower.  Please shower
[nfhynpd] (score 2, diepte 1) The difference is your feet aren’t making contact with people and every day objects on a regular basis, sir.
[nfiar4z] (score 2, diepte 0) I don't get why people care what sort of stuff drains into the sink. Do you also care that people are putting their shit in toilets? You put your ass on the same toilet as anyone else (hope you're using the sanitation covers). The sinks have automated faucets that pour out clean water when you hover your hands over it. The sinks are cleaned several times a day. You literally don't have to touch the sink at all. 

The only thing that should be an issue is the mess on the floor that can cause you to slip.
[nfj6vgk] (score 2, diepte 1) I was agreeing with everything up until this. Nobody does this…
[nfipt9y] (score 2, diepte 0) Not every facility has the special basins in the multifaith rooms for them. It would be discrimination to prevent them from practicing their religion then. If you don’t like it, then go elsewhere. It’s not that big of a deal. Grow up!
[nfj45fr] (score 2, diepte 0) Bring some baby wipes or something. Does god specify that you have to turn the bathroom into a splash-pad before you pray? Or is modernity acceptable but ignored in favor of dumber solutions?
[nfj642f] (score 2, diepte 0) They even added a thing to wash your feet so you don’t have to use the sink and they still use the sink
[nfjt925] (score 2, diepte 0) So that’s what they’re doing in the washroom. Everytime I walk in, it looks like they’re about to take a bath or something in a public washroom.
[nfjtqvk] (score 2, diepte 0) The same people that don’t wash their hands after taking a sh.t
[nfke6vp] (score 2, diepte 0) It’s the same people that wipe their butthole with their bare hand, that’s why some of them are on here talking about “well you wash shit and piss off your hands on the sink” No we don’t, that’s why there’s toilet paper.
[nfkftev] (score 2, diepte 0) Does Amazon pay you to pray or do you labor track into something? I find it unfair if people can just take time off during work while other people can't.
[nfh94w5] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.com/invite/t7jARCs) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[nfhqrqu] (score 1, diepte 3) Multi-Faith Room has sinks specifically designed for this reason. Newer FCs all have this. If you did not know then I recommend using this new knowledge and applying it so you stop embarrassing yourself and your family.
[nfhuiti] (score 1, diepte 4) Thank you friend. 
Im not sure about the family and embarrassment part, tho. This is a work related group.
[nfjjmiq] (score 1, diepte 3) Your are correct that fecal particles can contaminate surfaces which you are likely to touch. Hand washing is important for preventing diseases caused by bacteria you might acquire from touching the bathroom handle, door, etc. You are however incorrect in assuming thats the argument that the person I responded was referring to. Im 97% sure they think majority of people have feces and urine slathered on their hands after using the bathroom.
[nfk0284] (score 1, diepte 2) as opposed to the sinks in the bathrooms, which are at **waist** height for your *feet*?
[nfkmc80] (score 1, diepte 3) >hair is supposed to be above the shpulders, yet they refuse to do anything about some guy with a turban who has his beard a few inches below his shoulders

Probably a Sikh and they wear both for religious reasons which is why they cant "do" anything
[nfhgfgi] (score 1, diepte 1) There plenty of first gen’s from the 90 00 10 that are perfectly fitting in not to mention their children. Idk why not newer ones..
[nfhr7on] (score 1, diepte 2) Yup
[nfi5war] (score 1, diepte 2) It's like, if that's how you do it then fine, at home splash all over all you want, but at work just use the GD toilet paper. 
And ya if it touched your leg...💪
[nfja6gc] (score 1, diepte 3) Why you accusing me  😭 I  was just wondering lmao didn’t know it was such a widespread issue 😆 ✌️
[nfjignt] (score 1, diepte 3) Yo HOW is this widespread in NA, they got a lil club or sum? Shi can I join tho👀👀😸
[nfhix5w] (score 1, diepte 0) There are ways to solve this but it will be seen as racist and insensitive
[nfkqsdb] (score 1, diepte 2) ![gif](giphy|pCO5tKdP22RC8)
[nfj7125] (score 1, diepte 3) Racist much?
[nfhz3ra] (score 1, diepte 2) All I’m saying is I’ve never seen anyone dig into their asscrack or wipe their nose with their feet.
[nfjggkf] (score 1, diepte 4) All the more reason to keep them clean
[nfi39gb] (score 1, diepte 0) What the fuck why are people washing their feet
(40 reacties met lagere score weggelaten)

=== THREAD 1gi1q0l ===
SUBREDDIT: r/FASCAmazon
DATUM: 2024-11-02  SCORE: 33  REACTIES: 124
TITEL: Why is Amazon pushing for us to order these free insoles so hard?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lv227e9] (score 33, diepte 0) Amazon is offering you free insoles and you're complaining about it? I guess people truly will complain about anything.
[lv1rsot] (score 23, diepte 0) Insoles are cheaper than someone going to the doctor for their feet.

People work harder when their feet don't hurt.
[lv1scms] (score 23, diepte 0) Only Amazonians complain about free stuff that makes their life better.
[lv3c92s] (score 17, diepte 0) Knowing amazon, it probably has nothing to do with safety but instead a tax write-off
[lv1t5eo] (score 15, diepte 0) By “pushing so hard” do you mean offering - by providing information?  What about a company offering a resource, free of charge, is so offending?

If you don’t want them, I’ll take them!
[lv215qu] (score 15, diepte 0) You people are insane
[lv3rpgr] (score 14, diepte 0) Because they want us to stop complaining that the stupid shoes hurt our feet
[lv1thdg] (score 10, diepte 1) Or…Amazon owns Zappos
[lv1yv3i] (score 10, diepte 0) They are free and significantly improved my hip and knee pain.
[lv231w8] (score 10, diepte 1) In a subreddit for either target or Walmart I saw someone upset that their salaried manager was helping to do their job too much it was picking orders I think. So yes people will always complain
[lv26kn4] (score 10, diepte 0) The protalus insoles are trash. They’re so uncomfortable. The cheap insoles I got for only $10 are very comfortable tho.
[lv2go2h] (score 10, diepte 0) Yo. They’re awful.
[lv4c1gr] (score 9, diepte 1) Because insoles are cheaper than workers comp claims
[lv49bp8] (score 9, diepte 0) They made my feet hurt worse ..I threw them to the side
[lv4tfiw] (score 9, diepte 0) Those insoles sucked ass balls. I hated them and didn't use them. Horrible and hard. Just like the stick most managers have up their asses lol.
[lv1tmtg] (score 8, diepte 1) I had the same experience until I realized I didn’t take out the original insoles in my safety shoes.
[lv1wnov] (score 8, diepte 0) Well Amazon does own Zappos but at the end of the day it’s not a bad option if you have nothing else. (Please don’t be like me and refuse to get insoles and then be too broke to have any spending money)
[lv2zq7c] (score 8, diepte 0) They own the company
[lv21dog] (score 7, diepte 0) What they need to do is put gel inserts beneath the composite toe on the inside. That's what I did to finally stop the pain safety shoes cause me.
[lv21px6] (score 7, diepte 0) They’re $60 insoles. The probably buy them by the pallet for $1 each. They have a million employees. 

That’s a $60 million dollar write off for like $200. Or some shit.
[lv4vlnm] (score 7, diepte 0) Those free insoles hurt my feet. 

These are the best insoles I've ever used: [https://www.amazon.com/Tulis-Fasciitis-Full-Length-Orthotic-Absorption/dp/B085Z68XVV](https://www.amazon.com/Tulis-Fasciitis-Full-Length-Orthotic-Absorption/dp/B085Z68XVV)
[lv5zf1v] (score 7, diepte 0) Could be a promotional deal or something they just threw in.  Either way these insoles work best for people like me who have wide flat feet with little to no arch support.  No complaints from me plus beats spending $50+ at the podiatrist.
[lv1tfxi] (score 6, diepte 1) Amazon owns Zappos
[lv206g4] (score 6, diepte 0) Order your free insoles and say thanks to Mr. Jassy. Enjoy your employment at Amazon.
[lv2rhbh] (score 6, diepte 0) Tried them. Legitimately one of the worst decisions I have ever made. Absolutely excruciating.
[lv3s98w] (score 6, diepte 1) Bingo. Bonus was making the drones less prone to having hurt feet.
[lv8gzum] (score 6, diepte 0) I believe they are better than not having them.  The price attached to them is ridiculous but the voucher covers them.  So it's like _have this free cake valued at a million dollars"...  I think the reason they give them up is quality of life for the employee but the price is for tax purposes.  Problem being they last 3 months in a demanding job.  I prefer the random ones I found at Walmart for 12.  But I'll take a set of free ones once a year and then switch to Walmart afterwards.  Shouldn't be complaints either as Amazon turnover mostly within the lifespan of the Amazon employee
[lv33riw] (score 5, diepte 2) PROTALUS T100 Elite Insole

Ngl, I didn't like them at first, they are very firm.  I typically like Memory foam for my feet. But genuinely these have helped my joint pain.
[lv276iw] (score 5, diepte 3) "We're so proud to announce we spent x million on insoles for the employees we make stand all day" doesn't seem like it would go over well.
[lv2g3gf] (score 5, diepte 1) You deduct business expenses, not revenue. Under your logic their write off would be $1,000,000 (1 million employees, $1/insole) which is hardly a drop in the hat (>0.01%) compared to amazons tax liability of 7.1bn last year. Not everything is about a tax benefit.
[lv3ezji] (score 5, diepte 1 OP) I'm not complaining. I'm just trying to understand why they want you to get them so bad
[lv2ia9i] (score 5, diepte 0) Tried to order a pair I couldn't find them for men and just order memory foam insoles off temu
[lv2rm9i] (score 5, diepte 0) Somehow, I got two free already using their link from the emails sent. It’s free and worth 64 dollars.  Can’t complain. Idk if I feel any difference from the ones that came with the shoes, only time will tell
[lv2uztw] (score 5, diepte 0) Somehow, Amazon is benefiting from it. I just don’t know how exactly.
[lv3cr81] (score 5, diepte 1) They have data that shows that the cost of buying everyone insoles is justified to prevent injury risk. It's a win-win for both Amazon and the associate.
[lv388ic] (score 5, diepte 0) I will tell you what I have seen. Because if you get injured, they will look for a few things. Are you wearing PPE, were you in your assigned path, were you following safe work standards. If you end up with a leg or foot injury they will ask why you don’t t have the insoles.
[lv3c5pu] (score 5, diepte 1) Link? Sounds like my feet would enjoy those.
[lv3b8t6] (score 5, diepte 0) so your feet won't hurt as much? 🤦‍♂️
[lv3vef0] (score 5, diepte 2) Ironically the insoles made my feet hurt 10x worse
[lv4i4ou] (score 5, diepte 0) They get a tax return off the shoes and insoles.
[lv6ojen] (score 5, diepte 0) Because they work …… and we stand on hard ass concrete for 10 hours a day
[lv1rl4m] (score 4, diepte 0) Comes from Zappos. And they're free. And Zappos is owned by Amazon.

If they're the same insoles as this year's, it's okay. No different in doing my job.
[lv27cbq] (score 4, diepte 1) Which ones do you have?
[lv1z0u9] (score 4, diepte 0) I like the Dr Scholls work insoles better. Gel and memory foam and $15. I'd rather save my leftover credit to put toward a second pair of shoes so I can switch off.
[lv21k4w] (score 4, diepte 1) These don't exist. There's never an incentive to spend money in Business for no reason.
[lv2lw1c] (score 4, diepte 1) Amazon owns Zappos
[lv39uc4] (score 4, diepte 1) bad insoles make your feet hurt *more*

insole needs are wildly different for everyone
[lv36cwn] (score 4, diepte 0) Don’t know but the female ones are great, I was surprised cause reviews aren’t that great but they work perfect for me.
[lv3ap41] (score 4, diepte 0) hard insoles don't work for me, and neither do memory foam.

I use some that are gel on the bottom, and squishy bumps on the top.
[lv3hrju] (score 4, diepte 2) they are Dr Scholl's, and I used to buy them at Walmart. can't find the exact ones there or on Amazon, but
 https://www.amazon.com/Dr-Scholls-Revitalize-Recovery-Reducing/dp/B0BMNXH8XY/ref=asc_df_B0BMNXH8XY?tag=bingshoppinga-20&linkCode=df0&hvadid=80401921300363&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=m&hvlocint=&hvlocphy=&hvtargid=pla-4584001438394281&psc=1

looks pretty much the same concept
[lv4580b] (score 4, diepte 0) I got them and it took a bit of adjusting but I actually love them. They add a lot of support to my shoes and it knocks out any knee pain id have normally
[lv5ng0e] (score 4, diepte 0) Because they're frickin awesome!
[lv8a2uk] (score 4, diepte 0) To help you clearly
[lvkapfq] (score 4, diepte 0) Because so many people keep asking to see a doctor because of foot pain from standing
[lv21gtb] (score 3, diepte 1) They do work the best out of all the insoles I purchased.
[lv21mce] (score 3, diepte 2) The only ones that compete with these in my experience are superfeet, which are $50/pair.
[lv29aq3] (score 3, diepte 3) I bought like 15 pairs I whined up getting new shoes from Shoes for Crews and the inserts from Amazon stopped my feet from hurting. I got hurt at Amazon and had 3 hand surgeries on both hands now they are messed up. I wasn't going to let my feet get F-UP to
[lv21nqp] (score 3, diepte 2) They won't work if your original soles are still in plus make sure you order the right size.
[lv21bm9] (score 3, diepte 1) Yes they're the best insoles I bought so many pairs ,& 4 pairs of shoes once I got them I had no more problems. 😁
[lv21b1c] (score 3, diepte 1) Zappos is owned by Amazon.
[lv2fbc8] (score 3, diepte 1) Pushing for does not equal forcing tf
[lv3e6x6] (score 3, diepte 1) They own Zappos not the insole company. It seems to be part of some tax write off agreement with superfeet or something. Don't quote me on that it's only speculation
[lv3xo82] (score 3, diepte 3) Plausible deniability.  
Hey, we tried. - Amazon
[lv3dgv1] (score 3, diepte 0) I ordered them (haven’t opened them though) and they still send me the damn emails.  🤣
[lv4tw78] (score 3, diepte 0) I use them with keen shoes and it’s not bad. What helped more were compression socks.
[lv5eq93] (score 3, diepte 0) I actually liked them. My right foot didn't break this year which is unusual since it has broken every summer for the 3 years prior to this year.
[lv5y8un] (score 3, diepte 0) They make a huge difference.
And good socks too.
[lv6ijni] (score 3, diepte 2) Merino wool, darn tough
[lv6g39v] (score 3, diepte 0) Safety shoes are painful for many  and anything helps.
[lvab2r7] (score 3, diepte 0) because they can get tax write off. You can imagine how many people get it and it cost nothing for them(max of $5/pair) and they mark up the price to $60
[lvdnvns] (score 3, diepte 0) They don't want to for the bill for plantar fasciitis that you get from being on your feet for hours on end.
[lvfhzpp] (score 3, diepte 0) Tax write off
[lv3ah1i] (score 2, diepte 1) they don't work for everyone
[lv1snnk] (score 2, diepte 0) They write it off as a business expenditure.
[lv1um1f] (score 2, diepte 3) Probably some tax break shit
[lv1wi6k] (score 2, diepte 3) I just looked it up and I guess Amazon does indeed own Zappos. But I’m still wondering why Zappos employees get a different discount than us
[lv41ses] (score 2, diepte 2) I used Shoes For Crews when I worked restaurant and their stuff is solid AND not too expensive.
[lv49qul] (score 2, diepte 3) Yes I bought 2 different pairs 1 steel toe & 1 composite toe both under 60$ plus did other pair with 1 week try out and return the ones that hurt my feet.
[lv2d8eq] (score 2, diepte 1) i threw away those shitty protalus and asked safety for the dr scholls and like those much better. I can walk normally with them unlike with the protalus. those always made me walk funny
[lv4srla] (score 2, diepte 4) What industries who have employees stand all day, purchase insoles. They book it as revenues and sales quantity then expense it reducing net income reducing taxable profits. FC is a cost center. Look up [**vertical integration**](https://www.investopedia.com/terms/v/verticalintegration.asp) business models like Amazon.

▪️Yes, they get to count it as increasing market share. ▪️Yes, DOJ considers it potential anti-trust. ▪️Yes, its direct competitors are not crazy about Amazon having a captive employee market of 1.5 million.

Capitalism, baby!

![gif](giphy|tu6WafgphRrAk|downsized)
(64 reacties met lagere score weggelaten)

=== THREAD vdopf2 ===
SUBREDDIT: r/Construction
DATUM: 2022-06-16  SCORE: 60  REACTIES: 124
TITEL: What are your tips for dealing with smelly feet after being in boots for a while
POST (source_id=post):
yikes

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[icle6rp] (score 108, diepte 0) Real leather boots + merino wool socks = no stink.
[icle2fc] (score 64, diepte 0) Chop your feet off
[iclfcwl] (score 55, diepte 1) Seriously. You can put as many bandaids as you want on the situation but this is the only lasting solution. 

Also a boot dryer or cedar shoe trees
[icliv1u] (score 43, diepte 0) Buy a second pair of boots and swap them every other day. Supposedly your boots will last way longer that way too. I’ll let you know if the latter is true in about a year
[iclny75] (score 29, diepte 1) I did this for years and it absolutely makes your boots last longer.

Don't swap your boots every other day, swap them at lunch time with new socks.  It keeps the boots from getting really wet by the end of the day.  Plus you feel like a new man/woman after the switch.  You end up with less fatigue
[iclu3g0] (score 24, diepte 1) These are facts. Natural fibres / materials all the way. Reason why trainers/sneakers get smelly are the plastics capture oils which bacteria feed on. I used to wear leather shoes everyday and they still don't smell. Wool is self regulating, and keeps you drier / warmer when wet which is why Navy uniforms were traditionally made from wool. If your feet still smell it's because of a bacterial infection on your skin so treat that.
[icn0bm5] (score 20, diepte 2) And 2 pair of boots so you can rotate them.
[icld3fp] (score 17, diepte 0) Lol wash your damn feet.

Also, they make odor killing insoles, powders, etc. Tons of options
[icldk85] (score 16, diepte 0) Change your socks throughout the day, use powder and a fan or those fancy little boot fans at night, make sure to wash your feet well and let them dry when you can
[iclg97w] (score 14, diepte 0) Clothes peg on your nose
[icll3x7] (score 13, diepte 1) Merino wool socks work great!
[iclokuh] (score 13, diepte 0) Don't wear "cloth" boots.

Only real leather.
Leather doesn't smell.
[iclvldp] (score 12, diepte 0) Boots in a boot dryer every night one with air.
[iclks7c] (score 11, diepte 1) The only true solution
[icmqnun] (score 11, diepte 2) Boot dryer changed my life
[iclgvei] (score 11, diepte 0) Good socks . Good boots . Good showers . If your feet still stink there’s something else up.
[icly4jd] (score 9, diepte 1) Merino for the win!

Before i used light socks for summer and double socks for winter (i worked even inside refrigerator, -35°)

Fuck everything apart merino socks.
[icm0wma] (score 9, diepte 6) You prolly put her in there with your ridiculous comments. The drugs just help her tune you out. 

F ur grandma you’ll be in there soon enough
[icmeyzl] (score 8, diepte 2) Yeah. I don’t care for Darn Tough. Their warranty is a waste of time. The shipping cost is almost as much as a new pair. 

With that said, Bombas are really good.
[iclm000] (score 8, diepte 1) Actually this idea is what works the very best.  2 or 3 pairs of boots allows for them to completely dry out between each wearing.  And if there are inserts, they should be pulled out to dry separately.
[icm0vkn] (score 8, diepte 0) Best thing I have found - Own 2 pairs of real leather boots. Rotate daily. Give the boots a full day to dry out and air out.
[icmin6m] (score 7, diepte 3) Their warranty is the selling point my man. I bought 7 pair about 5 years ago and when the threads come loose or get a hole, I spend like $3 shipping them in for warranty. At that point, they send you email with a warranty code. Enter warranty code for free socks as well as free shipping.
[iclq5k1] (score 7, diepte 0) Idk what u mean. I like the smell
[icn0582] (score 6, diepte 2) The way I've always heard it is that its because cotton socks retain moisture so well, (think about any absorbent product you've ever used), that it basically becomes the perfect breeding ground for bacteria. 

Bacteria multiplies, and they smell. Wool sucks at absorbing stuff, so bacteria mostly sticks to the surface, and then dies. Little to no smell.
[icmky6e] (score 6, diepte 2) Smart wool
[icm0c7o] (score 6, diepte 4) This is a construction sub reddit trying to be helpful to someone. What are you here for?
[iclezqg] (score 5, diepte 0) I’ve tried powders and little shoe balls and sprays and the best thing to ever work for me is a spray called big jobs funk away.

If they’re old open em up as much as you can and spray every square inch of the inside and put a fan on it to dry. Every day when you come home from work take em off and do a quick spray and make sure they dry (boot dryers are great).

When you’re at work and your feet are sweating bring a change of socks. Or two. It’s really a game changer. Also use some gold bond. 

Best thing to do if you have the money up front is to buy two pairs of boots to rotate and doing all the above and you will never have issues again. 

Source: am very sweaty guy
[iclmaht] (score 5, diepte 1) Actually I read the same tip on Reddit a few years ago and it totally works. 16 months ago I purchased 2 pairs of my favorite work boots and they're still going strong. I used to use a new pair of boots every spring.
[icn0kos] (score 5, diepte 2) We are not
[icley8m] (score 4, diepte 0) A: wash your feet
B: wear sandles/flip flops/thongs/whatever gets fresh air over your feet whenever possible. Preferably  after you wash your feet for the rest of us. 

This is what works for me
[icn1poj] (score 4, diepte 2) I don’t work in the field and even I do this when I just wear regular shoes lol. My feet sweat no matter what I do. And I’m just sitting at a desk all day.
[iclliti] (score 4, diepte 0) Shower
[icm7ohd] (score 4, diepte 1 OP) I'll check if everyone in the site office is in agreement
[iclwp6b] (score 4, diepte 0) I wear Smartwool socks year round.  Keeps you dryer and less stinky.
[icndun8] (score 3, diepte 3) You can get electrolysis treatments that will stop your feet from sweating if it's a problem
[iclxhyo] (score 3, diepte 0) Clean your feet. Vinegar in your shoes. Have multiple pairs of boots
[icm001x] (score 3, diepte 2) Do you know how to read? It’s about OP not me you freak
[icm2id9] (score 3, diepte 0) BOOT DRYER. All that sweat gets absorbed into your boots and the only way it's coming out is in a boot dryer
[icmesvm] (score 2, diepte 1) got any specific sock brands thats not darn tough? darn tough socks seem to be made for people with skinny feet/legs.
[icmiukb] (score 2, diepte 4) I had to pay a ton in shipping. Even went through a whole thing with customer service. Even if everyone hasn’t had the same experience, it kept me from buying them again.

Edit: Also, the pair wouldn’t go bad at the same time. I would have to hold onto one mangled sock until the other was able to fall under warranty. To my knowledge they stopped accepting only one sock at a time under warranty claims.
[icot322] (score 2, diepte 2) Yes, Merino is moisture wicking, antibacterial, and self temperature regulating.
[ie6hqff] (score 2, diepte 2) I’ve had a good experience with Bombas socks. They hold up well and have a great price point.
[icm1cmc] (score 2, diepte 8) Use those prayers on yourself, you need it. Maybe consider counseling or something vs throwing out racial comment to strangers on Reddit.
[icmnjn5] (score 2, diepte 7) Lmao
[icm1po4] (score 2, diepte 0) Change socks at lunch time, have two pairs of boots and alternate them. Go see a podiatrist for recommendations on how to get the fungal/bacterial infection off of your feet(that’s what makes the smell)
[icm355i] (score 2, diepte 0) Spray lemonade on it
[icmie97] (score 2, diepte 0) Dude Darn tough brand wool socks and good boots are where it's at. I wear Thorogoods 

The socks have lifetime warranty, get a hole, send back, get credit for new pair with free shipping.

It's a sore pecker deal, can't beat it.
[icn5hah] (score 2, diepte 0) Get a boot heater
[icnam00] (score 2, diepte 0) Use a boot warmer even in the summer, it’ll dry them out and keep them from getting awful
[icnhpx3] (score 2, diepte 0) Take an extra pair of socks and change them at lunch. Synthetic blend socks suck. Merino wool or bamboo blends only. Also good to have 2 pairs of boots and rotate.
[jaxrhyg] (score 1, diepte 1) so funny haha really good stuff
[icxgqu6] (score 1, diepte 3) This is the only answer. You don't know your wearing wet boots everyday until you get a boot dryer and put on dry boots. For some stupid stubborn reason I was against the dryer too. For under $50 you can solve your stinky boot problem and have the pleasure of putting on nice warm dry boots everyday. Crumpled up newspaper doesn't work.
[icn7suy] (score 1, diepte 5) I've been doing it for years and have never had your experience.
[icob4b2] (score 1, diepte 2) Smart wool has worked well for me. They are longer, but stay dry when you're wearing the right boots.
[icp7uot] (score 1, diepte 3) longer isn't the problem, it's the width that's to tight. at least that's my experience with darn tough, going up a size doesn't change the width only the length.
[icqbpcm] (score 1, diepte 4) I haven't noticed any problems with the smart wool socks being too tight, they have loosened up a little in the 6 months I've had them. Darn tough sounds like they are darn tough to wear.
[icnr4td] (score 1, diepte 1) Bingo
[ico20bt] (score 1, diepte 1) 👍🏻this. 


Another option to aid this would be to change those merino socks more often. 
Two sets a day would soak up lots more sweat.
[ico7aft] (score 1, diepte 1) Marino Wool in 100 degree heat?
[icqbtkd] (score 1, diepte 1) Darn Tough merino wool socks are amazing. They have a lifetime warranty. I used to wear a hole through $10 a pair redwing boot socks in 6 months but I've had the same 5 pairs of darn toughs for years now. Zero smell and still look brand new.
[ict1r03] (score 1, diepte 1) And change your socks during break
[ie28i4y] (score 1, diepte 1) This is a really late reply, but do you have a brand or link you could share for good merino socks? I've scoured the web only to find them at $30+ for one pair or finding ones that have a blend of polyester which is the opposite of breathable.
[iclfura] (score 1, diepte 0) Change your socks bro
[iclg8ea] (score 1, diepte 0) Look on Amazon for foot antiperspirant. The only thing that made raising a teen football player bearable.
[iclhc5w] (score 1, diepte 0) Manscape foot duster. basically tea tree oil
[nbedy2j] (score 1, diepte 3) I bet you're feet smell lovely,
[icliwvf] (score 1, diepte 0) Dr. Scholls deodorizer spray works fine for me. Clean your feet well, fresh socks, spray after work. No smell. And it goes over 40°c where I live.
[icljyfz] (score 1, diepte 0) Wash your feet, keep an extra pair of socks with you, throw some baking soda in your boots.
[iclkhzh] (score 1, diepte 0) Dr scholes foot spray.
[iclqv6v] (score 1, diepte 0) Get you some gold bond spray and spray it on your feet before putting your socks on. It helps me a lot. Haven't tried Marino wool like others have mentioned
[iclsiuw] (score 1, diepte 0) Baby powder. If you have athletes foot which I used to get often it can make your feet reek. I used to put a cap full of bleach into 5 gallons of warm water and soak my feet for 5 min. Probably not the healthiest but would get rid of the fungus in one go.
[iclv71d] (score 1, diepte 0) I wash them.  


Edit: That sounded rude. Sorry.  


I wash them with bar soap so they're a little dry, not bad just a little. Then I wear wool socks (wig wams) even in the summer. Then the trick is, air your feet out man. Air your boots out. Usually they don't have any real stink to them until they are ready to be thrown out anyway. On Average for me boots=3 months. After that toss them.
[icm23hb] (score 1, diepte 10) 💀💀 bruh you claimed I was someone I’m not because I defended someone on a show. Claimed I’m a brown guy and now you’re saying I’m white. You made posts about not taking care of your grandma and feeling bad about it. 

Look in the mirror, that’s the person you should be upset with.
[icm2j9o] (score 1, diepte 12) Lmao ur the one writing paragraphs about finding god. 

F ur grandma and u 💀💀💀
[icm2vrt] (score 1, diepte 14) Thanks for the comedy you should be a comedian… at your grandmas rehab center. Call your family. They miss you
[icm35qx] (score 1, diepte 16) You should get on your knees and bow down to your master. Because I own you. 

Now apologize for making a fool of yourself
[icm3geu] (score 1, diepte 17) God can even take the people who are astray and who are sick and heal them with his love. Even you can come to his light after all your sins and after all your hate there’s even help from you and I hope that that inspires you because you seem in your 30s are in your 40s and I think you need direction because this is you crying out for help.
[icm3ylm] (score 1, diepte 18) Are you done?

Apologize to daddy
[icntmty] (score 1, diepte 16) "Wake up call that you get much to invested with strangers and have very emotional reactions" 😂😂😂 jokes write themselves
[icm0j9p] (score 1, diepte 0) Wool socks and Lysol in your shoes/boots at the end of each day.
(50 reacties met lagere score weggelaten)

