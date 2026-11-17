# Label-batch batch_0063

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
Schrijf het resultaat naar `batch_0063.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: s4ab1o, rmm65t, k7zf3o).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD s4ab1o ===
SUBREDDIT: r/AmazonFC
DATUM: 2022-01-15  SCORE: 103  REACTIES: 259
TITEL: Are you serious those shoes hurt my feet
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hsrxc56] (score 76, diepte 0) I’m ready for the downvotes, but there’s a shit ton of different boot and shoe options and plenty are comfortable. Hell I got a pair of Timberland boots and they’re great. I don’t think many of you ever took the time to get them and try options before getting upset over shoes that’ll save your toes. Reality of it is if you’re gonna work a warehouse job, 90% chance you’ll be required protective shoes
[hsqq9to] (score 46, diepte 0) I feel so bad for the pickers .. ouch these shoes aren't made to walk 20 miles a night..
[hsqasvp] (score 44, diepte 0) OMG! Which FC are you at? I’ve yet to see this notice at mine. It may be time to promote myself to customer.
[hsq053i] (score 42, diepte 0) Man their not gonna be scanning your shoes when you enter so I wouldnt care. My shoes are all black so they wouldn’t even see a difference
[hsqq7yf] (score 38, diepte 0) OKC1 is making them mandatory- it’s raising Union talk and people are threatening to quit.
[hsrwann] (score 34, diepte 1) As an electrician who builds your distribution centers i average 10miles of walking a day in those buildings with steel toe work boots. Get proper inserts, lace them correctly, and save yourself some missing toes. I’ve seen exactly once what can happen to an unprotected foot and im certainly not willing to do that to myself.
[hsr3y4b] (score 31, diepte 1) Do it! You have the right to a Union, I think every Amazon warehouse should do it!
[hspw6tw] (score 25, diepte 0) It’s the worst.  The shoes are the worst.  I have four pairs and none are comfortable.
[hspx02q] (score 25, diepte 0) I hope the shoes are mandatory but secretly voluntary, that's how they treat mandatory masks here.
[hss9e0r] (score 23, diepte 1) You can't talk common sense into people they are too ignorant 🙄
[hsr2wb5] (score 21, diepte 0) We all knew this was coming eventually. Happening at my FC too and the response will be fuck em. They're never going to check unless something crushes your foot and then fighf you WC claim.
[hsr9j1g] (score 21, diepte 0) They'll be mandatory at CHA1 in April. They start to hurt my feet after maybe 8 hours. That's in pack too. I can't imagine picking for 12 hours. Yet alone 60 during peak.
[hsqqakw] (score 18, diepte 1) 20 miles is 32.19 km
[hsro137] (score 18, diepte 2) marry me
[hspwbq6] (score 16, diepte 1 OP) I have my one pair and they feel like bricks on my feet
[hssj8v6] (score 16, diepte 3) Hvac guy, we call em tin knockers, had a large piece of equipment fall from about 4-5 feet off the back of a truck onto his foot. He ended up losing 3 toes on that foot and had like 5 months til he was back to work even then he couldnt do anything too physical.
[hsrp0ng] (score 15, diepte 0) I've been on an order picker going on 5 years wearing vans without have a single issue once or hurting myself because I'm careful fuck these shitty ass uncomfortable bs shoes.
[hsr19hc] (score 13, diepte 0) In Italy we can’t choose our safety shoes. You can only use the one amazon give you. It’s for safety issue, so if you hurt yourself with something and not wearing their shoes you can get punished
[hssea3g] (score 13, diepte 1) True. They have so many options. I was wearing New Balance sneakers all year long at other jobs, and was able to find almost the same running shoes with safety toe insert.

People don't have to wear heavy boots they can get tennis shoes or skater shoes if they wanted.
[hsqaxe7] (score 12, diepte 1 OP) MDW4
[hsrvuyr] (score 12, diepte 3) Unions have a lot of benefits around workers rights, quality of life at work, and wages nevermind pensions/annuities that will outweigh the cost of membership by a country mile. Collective bargaining is a powerful tool because corporations like amazon will only listen when profits are on the line and striking forces them to the table. Did you not watch kellogs?
[hsrnw8t] (score 12, diepte 2) I’ve been wearing composite toe shoes to work for the past year and, as non-inventory, I walk my building up and down daily. Get some insoles and break them in. Yes, they’re heavier and will never be as comfortable as a lightweight sneaker, but that’s PPE for you. Harnesses and gloves and masks are also uncomfortable, but they provide protection. I got used to it.

I’m also all for unions, but I doubt a union will be able to do anything to combat safety protocols that have been proven to reduce at-work injuries.
[hsrfeqe] (score 11, diepte 0) I am all for protective footwear. 

I however am against Amazon's self dealings forcing all to go through Zappos.... Which limits options to most likely stock they are trying to clear.

By forcing, I merely mean to get the money towards safety shoes
[hsseyfv] (score 10, diepte 1) I have some nice composite toe hiking boots. Hiking being the key word!
[hsqywr1] (score 10, diepte 0) I'm confused as to how this works. Are new associates exempt for the first couple weeks until they buy them? If they purchase shoes but dislike them, what do they use for the time in-between sending them back and getting new shoes? $110 a year credit isn' t gonna cover it for associates who walk 15+ miles. You're supposed to replace shoes every 300ish miles. Is there any physical location to try these shoes before randomly purchasing them online? How do I know which of the 100s of options to choose from? 

I purchased one pair awhile ago (the cheapest Sketchers shoes). After eight hours of picking, the middle of my knee felt like it wanted to snap. Couldn't walk nearly as fast. Couldn't pivot.
[hss206a] (score 9, diepte 2) What happened?
[hsry60l] (score 9, diepte 0) Well right above it is an opportunity to get a bachelors degree that they will pay for. Think about those hurt puppies and use that for some motivation to get tf out of this place.
[hsq9fyr] (score 8, diepte 1) Damn what brand did you buy, i rock the timberland ones and they work just well
[hspy6lz] (score 8, diepte 1 OP) I hope so
[hstfd1v] (score 8, diepte 1) Delivery station worker here, i walk 20 miles everyday, 40k+ steps, 10 hours 5 days a week, i bought some shoes from Zappos & with INSOLES, it’s definitely the most comfiest shoes ever & for free?? i can’t complain. all i say is, insoles, insoles
[hsrdr1y] (score 8, diepte 1) Oh no I’m at CHA1 :/
[hsrtbjb] (score 8, diepte 2) They announced it at stand up in pack last night. And they have it posted in the inSTALLments in the restrooms.
[hstw3ac] (score 8, diepte 4) I poop on purpose just to see this info lol
[hssjaud] (score 8, diepte 0) It’s all fun and games until 60% of a shift had plantar fasciitis issues
[hssyayb] (score 7, diepte 2) I live in Joliet. I work at ORD9, sort facility. Ours starts January 30th for safety shoes. I bought sketchers. Not going to switch until I have to
[hsqxrs6] (score 7, diepte 0) Of note, I'm pretty sure the safety shoes you wear don't have to be ones from the Zappos site (you'd just have to pay for them out of pocket). There are stores like Red Wing where you could try on the safety shoes and see how they feel
[hsrf39j] (score 7, diepte 2) Big RIP. I'm scared of the day I have to pick for 12 hours in them lol
[hss4yv7] (score 7, diepte 3) I got the lightest pair I could find on Zappos last year.  I managed to wear them until lunch. I’m definitely going to looking beyond Zappos for something to wear. I used the Zappos money this year for insoles, which I really like.
[hssvy63] (score 7, diepte 1) I didn’t like any of the women’s shoes they had in stock, so I got myself a $40 pair of steel toed sneakers off Amazon and they’re totally comfortable to me. I put in almost 4 million steps last year. 

Since the men’s selection was much better, I used my Zappos credits to get my dad two free $110 pairs of timberland pros, and he absolutely loves them.
[hsrzaxd] (score 7, diepte 0) That's a popular misconception. Try the Irish setter line, get the wingshooter wedge sole boot. They run very large so I recommend going down half a size to a full size if you like a snug fit. They are the most comfortable boots you will ever wear once broken in. Don't waste time on those 110$ shitty sneakers they sell on there
[hstngij] (score 7, diepte 1 OP) They do exist but the shoes are still bricks on my feet lol
[hssf03b] (score 6, diepte 3) Nice! I started in November and picked up some new balance for free, and I like my new balance but they gave me another $100 allowance for safety shoes so I want to try something else maybe.

I rock some New Balance and cheap arch support and works good. I don't know why everyone is upset over safety shoes, but it's reddit so I shouldn't be surprised...
[hsqlaja] (score 6, diepte 1) That's how they used to treat mandatory masks at mine too, but now they are cracking down hard.  Daily safety patrols giving out instant write-ups. For masks that probably aren't helping too much when everybody uses the same coffee machine and sticks their hands in all the same places come break time.
[hssa466] (score 6, diepte 4) Exactly! If Amazon was a small company with only a hundred or so people in the warehouse, I would say unions will interrupt work.

But Amazon is a monopoly with billions of dollars, so **unions are essential** for workers to have rights! Unions don’t interrupt work in big companies, since everyone is forced to work instead of being voluntarily working.

I’ve worked in a warehouse before Amazon where there wasn’t a Union, but it only had about 120 employees in the whole company. A Union isn’t necessary there. In Amazon, a Union is necessary!
[hsrw7lb] (score 6, diepte 1) Oof I am already having foot issues with my plantar fasciitis and the weight those shoes add makes it ten times worse.
[hst9ho0] (score 6, diepte 2) Composite toe weigh WAAAAAAY less. I have a pair of new balance safety shoes and they're great. The biggest thing you need to do when you get them is get some inserts. Dr Scholl's aren't great, there are plenty of online brands that are fantastic (protalus and tread labs are two I recommend)
[hsr4s4r] (score 6, diepte 1) For new associates, they try to get you set up with Zappos the first day or you're stuck with those steel toe slip ons that are uncomfortable and clunky. (This is from my experience starting at an AMXL FC)

Zappos has a 365 day return policy. I'm not sure about the wear and tear for the policy. You can get more in depth answers by emailing the Amazon Zappos (with the email you set up your account with) help email or calling them.

For deciding which ones, always ask veteran workers. Anyone who has been there for years will have their preferences for brands or types and will be happy to help you. It's also good to look through the reviews. I also suggest looking into getting some of the insoles that make it a bit easier on your feet.

Also, depending on what position you have, you may require a different kind of shoe. I believe for inbound or outbound, you just need to have steel toe. For TOM team, you need boots that have ankle support and it's better to get composite instead since the steel toe can get cold.
[hss46e6] (score 6, diepte 3) Damn. I’m DA5 so I was off yesterday and haven’t seen the new inSTALLment.  Thanks for the heads up
[hsrrjmz] (score 6, diepte 0) My dumbass went to buy metal toe boots. Biggest regret.
[hssjwur] (score 6, diepte 0) It will get ignored.
[hst7wf0] (score 6, diepte 0) They have talking about by the end of the month you have to have safety shoes at my fc. Its either have the shoes or be forced to wear whatever safety has in stock on site. They've even being helping people though the process. I dunno what you all are complaining about. I've had mine since my 4th day of work and have been fine. Yes they were uncomfortable at first but you've got to break them in. Did y'all know they make insoles for those who work in warehouses/places concrete floors? Someone of y'all need to try those out. I've personally find the safety shoes worth it. The amount of times I've bumped my foot on a wooden pallet has made me thankful for them.

Edit: Just remembered my one complaint about them is they are difficult to drive in. Bulkiness makes it difficult to feel the petels. But that's a minor complaint cause i can just take them off when I drive or wear other shoes and change into them.
[hsrcnu4] (score 5, diepte 2) Also don't breathe so my feet overheat which means I sweat just walking... I'm only 165lbs
[hssdyg4] (score 5, diepte 1) It's gonna roll out in three waves; I saw an email from our safety team that said our site is going to implement the mandatory safety shoes by March.
[hsrxu7n] (score 5, diepte 3) It is hard for people like me who have plantar fasciitis or similar conditions. My feet hurt like hell on a regular day those safety shoes always make it worse for me. I have accommodations now but their accommodation process is so frustrating and I have to renew every month or not go to work.
[hsrmwmt] (score 5, diepte 1) Where did you get this info? I’m at CHA1 as well and haven’t heard anything about them becoming mandatory.
[hsrfyuw] (score 5, diepte 0) I've been avoiding getting zappos shoes and now I'm not ready getting their uncomfortable shoes
[hsrgrdg] (score 5, diepte 0) i wore my shoes from Zappos once and I couldn’t even walk straight, my feet were hurting like crazy. safety gave out insoles for shoes and I tried those but they made my toes feel like they were being crushed. I ordered a size and a half up too just to accommodate for the fact that the steel-toed shoes would be tighter and they’re STILL too tight to where my feet are suffocating. I wear an 8.5 and bought a 10.
[hsrqfvm] (score 5, diepte 0) I have bought three different pairs now over the three calendar years we have offered the program. And all I can say is that the Merrell composite toes I got last year are really comfortable. It took about one work week to break them in, but now they’re just as comfortable as the Nike tennis shoes they replaced.
[hsrrm5h] (score 5, diepte 0) I got some pretty good New Balances through Zappos. They're basically normal shoes just with a composite toe. I got the wide ones, so they aren't tight around the toes.
[hstdpwt] (score 5, diepte 2) The timberland pros, they only took a few work days to break in. I wear them for anything labor related in and out of work and love them
[hst98xl] (score 5, diepte 1) Got some decent Reeboks
[hss0ols] (score 5, diepte 0) My FC can't even enforce the mask policy so I highly doubt they'll enforce this.
[hssc1rb] (score 5, diepte 0) Then get a office job where you sit on your tush all day.
[hsseto7] (score 5, diepte 0) I've seen a broken cart completely collapse right onto someone's foot, and because they were wearing safety shoes they were fine. You might be able to get insoles for free from your safety team, and there's plenty of options on zappos. You'll find at least one pair that you like. And you can return them if you don't like them and just get another pair for free. I personally don't see the issue with wearing them, they're only mandatory to protect your feet from getting injured. Foot injuries are no joke.
[hsqu6r6] (score 4, diepte 2) Skechers, two are Reebok, and the newest ones are Keen.
[hsrn70x] (score 4, diepte 2) New Balance is also pretty decent
[hssru3w] (score 4, diepte 1) These are probably the best bet for pickers. Still suggest get Powerstep Pinnacle Maxx insoles: 

https://www.zappos.com/p/timberland-pro-radius-composite-safety-toe-black/product/9489189/color/3?zlfid=191&ref=pd\_detail-1-sims\_cv
[hsqr8th] (score 4, diepte 0) There’s like hundreds of options to choose from…
[hsr98qe] (score 4, diepte 0) Just a recommendation for anyone who hasn’t got theirs yet. Try to find light weight shoes and be willing to pay a little bit out of pocket after the discount. I got carhart light weight boots that are on Zappos and cost $11 more than the discount allows
[hsuefwy] (score 4, diepte 3) Off topic, the name of the inSTALLments is a bad joke. 🤣
[hssfr2k] (score 4, diepte 1) But did you change the width? I learned before Amazon that I had to buy regular shoes that were Wide or Extra Wide, should have a size option when you order.

So I only had to increase my size from about 11.5 to 12.0, but made sure to order a wider option than the standard.
[hssrw34] (score 4, diepte 1) That's why this sub exists. For crybabies to cry. 🤷‍♂️
[hssh06b] (score 4, diepte 1) I took the offer last year after 4 years of employment but before I left I got myself some carthartt boots I love and used there while I did amnesty so I walked more than most. I told people when they started doing the zappos stuff it was right around the corner from being mandatory and surprised it wasn't from the start.
[hst5btw] (score 4, diepte 1) Facts they even got composite toe tennis shoes
[hssfrr2] (score 4, diepte 1) where
[hssksmk] (score 4, diepte 0) They have been mandatory for years at AIR sites. And on top of it, your not allowed to have steel toe only composite toe. I am in the Rme dept anyway mandatory there as well.
[hstbw6v] (score 4, diepte 0) Shit, I’m glad I wear mine. I dropped a tote on my foot one day and that thing was very heavy. Probably would’ve lost a toe.
[hstl80w] (score 4, diepte 0) You know what I'm surprised the number of comments that are just ok with this ...what's wrong with you.. you're gonna search for comfortable shoes...how about no I won't comply to your idiot policies that don't make sense and not demanded by the type of job I'm performing...have a little spine shish.
[hst6j9x] (score 3, diepte 2) Mdw6 here… us too get something with hood support…
[hsrwzn4] (score 3, diepte 3) Jeff Bezos couldn’t have said this better himself! You’re parroting anti-union talking points that bosses spread to help kill unionization efforts.
(177 reacties met lagere score weggelaten)

=== THREAD rmm65t ===
SUBREDDIT: r/AmazonFC
DATUM: 2021-12-23  SCORE: 193  REACTIES: 212
TITEL: AM 🤡 just made me a permanent Tote runner and According to my Apple watch i walked 16 miles yesterday which is kinda insane, Feet and legs have left the chat 💀
POST (source_id=post):
&#x200B;

[Can you lose alot of weight while running totes? I saw this guy who has been doing it for 2 years and he's pretty thicc. How's that possible?](https://preview.redd.it/72g2atamm7781.jpg?width=947&format=pjpg&auto=webp&s=271ea1456615a97345bf8a7fd6076005dcccb397)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hpn9cl2] (score 87, diepte 0) Word of advice get out of tote running while you can, It gets old real quick.
[hpnnzva] (score 48, diepte 1) The PA that bullied 
me had me on tote running duty and I told him don’t want to do this he said to bad you could clock out right now because that’s the job your assigned to. Glad he quit!
[hpn8e4r] (score 37, diepte 0) Once the tote tanks get old they get harder to push.  The ones we had when I started were a bitch.  Tote running was a hell of a leg workout.  Then we got new ones and it was cake.
[hpn99oj] (score 23, diepte 1 OP) Hell yea, I bet when i leave amazon i will have some good looking calves 😂btw if you were talking about the "Carts" then ours are so fucked up that they move even when you lock them which is a safety issue but safety won't do shit about it 🤨
[hpn7a4l] (score 22, diepte 0) Damn RIP to you sir. Go to HR soon or you’ll be in for some pain
[hpnaps5] (score 18, diepte 1 OP) there's no way in hell ya getting 16 miles in while flirting with the chicks 😂 we are on the move non stop bruh 🤨
[hpnb05b] (score 17, diepte 0) They put me on totes 1 time and I told them I wasn’t ever doing it again and the AM was so salty about it. I haven’t did totes since haha
[hpn5fjf] (score 16, diepte 0) I bet they made it seem like tote running was a good thing 😂. Always say no to other things
[hpn6yat] (score 16, diepte 1 OP) yea, but tbh i like it, it seems way better than standing at a station packing for 10 hr straight. and since we don't really get labor tracked cuz we are indirect i be doing 40 to 50 minute breaks sometimes 😂
[hpnddj4] (score 16, diepte 2) 25 miles a day as a water spider son
[hpnq09k] (score 14, diepte 1) It’s way better than picking.
[hpnq1gp] (score 14, diepte 0) I like tote running. It’s just paid cardio
[hpnabsz] (score 13, diepte 0) lol that’s regular for us flirty waterspiders
[hpna0o5] (score 12, diepte 2) Yeah the brakes work for about a month on a brand new one.  If we red tagged every tote tank with a problem there would be no tote tanks.  I am speaking of the carts that carry 10 stacks of 11 totes.  I thought everyone called them tote tanks.  That is even how we label them and their parking spots.
[hpn90ta] (score 11, diepte 1 OP) 🪦
[hpnwjdd] (score 10, diepte 2) I enjoyed picking back in my day but stowing is where it’s at.
[hpomgqj] (score 10, diepte 1 OP) tbh, for now i like it. it feels better than packing for 10 hrs at a station and like i said we don't get tot so when its not too  busy i can literally stay in the break room for 40 to 50 minutes and my AM or PA doesn't even notice. there are pros and cons to it
[hppgkl4] (score 10, diepte 1) Any job at Amazon get's old real quick. I found it more entertaining to sleep in the bathroom for 7hrs and only work 1 hr.
[hpndeeg] (score 10, diepte 3) 25 miles is 19730.91% of the hot dog which holds the Guinness wold record for 'Longest Hot Dog'.
[hpnqm5a] (score 8, diepte 2) Never picked but my legs were dead after tote running for 2 weeks straight
[hpnve2g] (score 6, diepte 1) You can’t always say no. They wouldn’t let me one day so I just left. I am chronically ill and was nauseous and having a migraine that day so busy work that didn’t keep me occupied wasn’t gonna do it.

Pisses me off I work hard and they give me bs jobs when new people r there. Fuck them
[hpnahvb] (score 6, diepte 3 OP) Yea, We call them carts or tote carts and we actually load 10 stacks of 12 totes on them not 11. might be different in other FC's.
[hpp32j6] (score 6, diepte 4) Take a look at the second pic in this article this is what we use to tote run.  [https://www.nj.com/mercer/2017/08/amazon\_job\_blitz\_hopes\_to\_hire\_1500\_employees\_in\_4.html](https://www.nj.com/mercer/2017/08/amazon_job_blitz_hopes_to_hire_1500_employees_in_4.html)

The top right picture.
[hpnr8fx] (score 6, diepte 2) Nah they put me on the hard tote job where you stack them on the big kart and push them all the way down the the floor and then put them on the elevator repeatedly. They didn’t give me the one where you just push the totes in the elevator.
[hpo8ykx] (score 6, diepte 0) People funny lose weight because they think they can make up for their terrible diets by walking around the building.

"I did 8000 steps today! I deserve two number 9s, a number 9 large, a number 6 with extra dip, a number 7, two number 45s, one with cheese, and a large soda!"
[hpom6mb] (score 5, diepte 4 OP) these bots talking to each other 😂
[hpnbia6] (score 5, diepte 1 OP) why would you not do it? you are not labor tracked so no rates plus you can take long ass breaks and your am don't even know because you don't get TOT if you don't **Scan** something for 5 minutes
[hpnvcg9] (score 5, diepte 2) Bc it hurts my back and body way more then my normal job. I hate it. Id rather do carts(on ship dock we have these blue and grey carts to put boxes on and carts is just getting them off the trailer setting them up and putting them in a staging area, it’s boring AF)
[hpon9lp] (score 5, diepte 1 OP) yep, idk how accurate is apple watch but if i am really burning 1000+ calories then that's awesome
[hpnq7kp] (score 5, diepte 0) I do at least 15 miles a day as a manual palletize scanner. It's nuts to think that I walk 15 miles when I'm mostly walking in circles
[hpnari3] (score 4, diepte 4) We were only supposed to stack them 11 when I was doing that.  Safety, blah blah blah.  Tote Tanks sounds cooler you should have your site adopt that.  Lol.
[hptnecp] (score 4, diepte 4) Thank you
[hpoy4bf] (score 4, diepte 3 OP) oh ok,i meant it in a sense that we are not monitored by a computer scan.
[hpqiq20] (score 4, diepte 3) 16 miles is the length of 5603.97 1997 Subaru Legacy Outbacks
[hpnb2wy] (score 4, diepte 0) I walk 24k steps a day, and in 6 weeks dropped 22lbs, and 3% of BMI. I'm a big guy to begin with, but my legs are toning up great, but that muscle weighs more than fat so I'm doing alright.

At some point my body will get used to it so the losses will slow down. 70% of weight loss is diet, but with all those steps I have more calories to burn, and earn that pizza a week. Lol
[hponwpj] (score 4, diepte 1 OP) so far so good! it's tiring but not boring
[hpok5o1] (score 4, diepte 0) They can not force you to do an indirect role. Tell your AM that you don’t want to do it as often or at all. If they don’t listen to you go to HR.
[hpocuwh] (score 3, diepte 2) I always say no and i think my leadership figured out it was easier to just leave me alone than argue with me about something im not going to do anyways
[hponhwz] (score 3, diepte 4) Our FCa standard just changed from 12 high to 11 high because pick tote runners cannot catch up to demand of the filled tote tanks... so we carry tanks from mix/smalls and just dump them into pallets now... though a few pick tote runners still sit in the break room even though it's peak season
[hpn93mf] (score 3, diepte 0) Losing weight depends on ur intake too..i lost 8kgs in the last two months (i only work on OP) ..always give enough time between floor sessions..i can never run cage/tote for more than 1 session..hope ur shoes are comfy too
[hpqf9oc] (score 3, diepte 2) I had one like that I transfered out 2 weeks after I told him no and he threw a bitch fit everytime he seen me because I kept telling him no and he wouldn't stop...tote running is a indirect role and I flat out refused or is was going to hr it was his choice.
[hppvq2c] (score 3, diepte 2) This. Been an FQA for three weeks and it's getting old cleaning up a delivery area because they don't have their own FQA.
[hpnaqxt] (score 3, diepte 2) 16 miles is 25.75 km
[hpsxbck] (score 3, diepte 7) LOL I just saw this 😂
[hpndf7z] (score 3, diepte 4) 25 miles is 40.23 km
[hptbdsb] (score 3, diepte 3) Cherrys in Amazon: (least in UK)

When your stowing the tote has a lot of small identical items meaning the Stower can easily stow and get their units per hour up with out struggling to find bin space or lift heavy items into the lower bins of the pod or shelf.

E.g a tote with 100 sd cards would be considered a good cherry.
[hpozsui] (score 3, diepte 4) Yeah, I gotchu, Being labor tracked is good, you just can't be caught slacking. I hope the rest of Peak is good for you. We have 2 more weeks of MET coming up. Been like this since September...
[hpnc8zg] (score 3, diepte 1 OP) I am in it to lose some weight too before the summer tbh.i think your body slows down when you don't have alot of fat left...
[hpnetyw] (score 3, diepte 0) Did 12 miles between first and 2nd break as waterspider a few weeks ago. 21 miles the whole shift combined, And that was while wearing Zappos.   Big ouch.
[hpneurp] (score 3, diepte 1) 12 miles is 10274.57 Obamas. You're welcome.
[hpopdro] (score 3, diepte 3 OP) That's what i am telling these people like dude our break starts at 03:00 pm and yesterday i was in the breakroom at 02:35  and stayed there until 03:30 since it wasn't busy 😂no more if you don't scan anything for 5 minutes you collect TOT BS no rates no tot no performance based write ups, just be safe and don't hit someone!
[hpnwkuj] (score 3, diepte 2) Good bot
[hpo0nw7] (score 3, diepte 0) Cancel your gym membership and eat whatever you want 👍
[hpooehl] (score 3, diepte 1 OP) it's not boring tbh.
[hpo1bmr] (score 3, diepte 0) i was a water spider for a week, i was averaging around 55k steps a day my feet haven’t been the same since
[hpoont2] (score 3, diepte 1 OP) That's so true man. this guy at my fc has been running totes for 2 years now,. He is bigger than me and i haven't done any cario in years i just lift weights. Liike i got kinda nervous that will i even lose the last 20-30 pounds of weight running totes cuz this dude clearly doesn't lose any. the i figuered his diet might be fucked up
[hpotzm9] (score 3, diepte 0) The simplest way I can explain the weight issue is: their carb intake is significantly higher comparing to their fat intake. Thus the amount of physical exertion they are applying isn't **enough** to burn the rest of the carbs.

Insulin is a fat storing hormone (one of many functions) and when you consume *too* much carbs, it can store a merely 15gs of fat resulting a build up of subcutaneous fat hence the overweight issue at Amazon.

Which results in the question: **how is it they are doing that much physical work and yet not losing weight?"**

I tried numerous diets from plant base, meal replacements, keto to carnivore.  Plus I'm a diabetic T1) so I get my labs done every three months to really dial in what's happening in my body.  I've been overweight three different times also.

If you want me to go in detail I can do that once I get on my computer. 

So then I waterspider for stow and I use this to manage weight. I have not gained or loss weight out of the year since I've done this.

To add on:  I meticulously count my carbs so I have the precise amount of carbs to burn so then my body switches burning fat.

Example: **For every *moderate* physical exertion requires 35 grams of carbs (a Gatorade bottle) for two hours.  This applies to my body and current weight.**
[hpp2k9d] (score 3, diepte 2) I used to look at it like that too but after experimenting for a year with carnivore, I think caloric intake is now pointless.  Sometimes I'm intaking an average of 2500 to 3000 calories of meat but that's not including the additional fats I add.

So a note on insulin: everybody needs insulin but the luxury I have is I can (have to) manually take it.  This helped me understand the correlation between carbs, insulin and fat. When I was 170 pounds, I was taking around 120~ units of insulin to treat the carb intake I was consuming (250 to 300 grams). 

After I switched to carnivore, my insulin injects reduced to merely 20 to 35 units average per day.  I did near zero carb then I started losing weight within the span of 3 months.  12 pounds per month to be exact.  I also didn't work out, I hated working out.

If you check out the documentary: "That Sugar Film" he shows the 2000 calorie rule with a high carb and low fat diet.  And guess what?  Still had a hard time losing weight AND he worked out.

So another simple way I can explain this:  think of carbs and fat as two different source of fuel for your car.  If you have too much carbs, fat will be stored until you burn the carbs.   When you rid of carbs as fuel, you need an alternative which is fat.  Your body will now then switch fuel.

The massive amounts of subq fat will now be used as energy (assuming you are overweight).

I also just eat once a day.  A 10 to 12 hour work day for me only needs a ribeye steak (1.5 inch cut), coffee with heavy whipping cream (loads of it for fat) Then an additional 90 to 120 grams of carbs depending on the work load.

With that I've maintained my weight of 136 to 140 for an entire year.

I do have cheat days where I reintroduce carbs but then I would fast for my work day.

In all: the reason why obesity is a problem is not caloric intake but more so an overabundance of carbs and misinformation regarding *low fat*

I'm not a medical profession and a lot of this is still coming into light so try at your own risk.  But personally, my labs and health has drastically improved ever since I did all this.

Sources to view: What I've Learned (youtube, he cites his sources), That Sugar Film (2014, crazy how this has been out for this long, yet nobody understands the misinformation of low fat trends.)

Also the transition from high amounts of carbs to low is gonna be a shock to your body unless you have the mental fortitude to *understand* the changes.
[hpp45id] (score 3, diepte 3 OP) this was very informative. Thanks!
[hpovfvy] (score 3, diepte 0) Did tote running almost every day for 8 months. Decided to transfer to ship dock and im so much happier now. Tote running will ruin your feet.
[hpnbmta] (score 2, diepte 2) I know your pain…it’s all I’ve done for the past 2 months…
[hppjl65] (score 2, diepte 4) I finally got put to problem solve lol XD, guess w that’s what happens when you show up nearly a hour late for MET…
[hpod7qj] (score 2, diepte 2) >Pisses me off I work hard and they give me bs jobs when new people r there. Fuck them

This has always confused me. I hit numbers way above rate and they continue to stick me on bullshit jobs. 

Multi pick rate: 50 UPH
My rate: 95-125 UPH

PA: *Please go to stow*
[hpr0spz] (score 2, diepte 7) What i would do just for 1 of those  /;
[hpov22r] (score 2, diepte 5) Tote tank is what we use at CMH1, or UBoat, and totes are still 12 high here. Tote Jackpot operator chiming in....
[hppmv0k] (score 2, diepte 4) Tote tanks at our FC, carts are what our water spiders use, or mobile carts for PSers
[hpoybbl] (score 2, diepte 3) Have you got an example of these carts? I keep wondering what we are because we mainly use Uboats and pallets.
[hpp3bg8] (score 2, diepte 5) Thank you! Those do look a lot more convenient than 5 stacks (UK pallet) or 4 (Europallet).
[hpnfz0k] (score 2, diepte 2) Show us them gams when you leave.
[hpnk24f] (score 2, diepte 2) Oh you will. I just do it once or twice a week and man I don’t need a gym no more. Between that and picking I feel like I do a whole body workout everyday. It’s kinda nice tho I’ve gotten a lot stronger and have way more endurance than when I started. Other than that I’m dying inside :(
[hpn8qad] (score 2, diepte 0) Dang doing stow i only get 7k to 12k steps a day
[hprd5bd] (score 2, diepte 2) Last time i was a Tote Runner i fell asleep in the bathroom while taking a quick break...
[hpobs7v] (score 2, diepte 3) Good bot
[hponink] (score 2, diepte 5) I'm not a bot lmao, I thought you like extra karma or some shit idek I've seen that shit before on this sub 😂
[hpopsza] (score 2, diepte 6 OP) I am talking about useless-convertor-bot and convertor-bot, if you refresh the page they are commenting after eachother 😂
[hpndemv] (score 2, diepte 3) 25 miles is 40.23 km
[hprds1a] (score 2, diepte 2) Cherrys? Like literal cherrys, or am I missing something?
[hpomr97] (score 2, diepte 3 OP) that's what i've been doing too.
[hpp0psv] (score 2, diepte 5 OP) yea we just got an extra hr added to our schedules 💀 but yea good luck to you too
[hpqiovx] (score 2, diepte 2 OP) well walking 16 miles a day is not lazy, and when the work is slow means there are absolutely not enough totes to take them to the elevator then you just stand around.the break room is literally 2 blocks over so i just sat there while the packers accumulated enough totes for me to load them on a cart.I am not sitting in the break room if there's work
(128 reacties met lagere score weggelaten)

=== THREAD k7zf3o ===
SUBREDDIT: r/Construction
DATUM: 2020-12-06  SCORE: 217  REACTIES: 204
TITEL: New construction home. 2 months old. Home is cracking every few feet. Builder is saying this is normal. Even the fake beams are cracking. Any advice?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gev07dk] (score 330, diepte 0) This is actually very common in new construction houses. Especially those framed and roughed during winter and wet months. as the moisture content lowers in the lumber in your house through continual heating the lumber shrinks and moves slightly. The drywall being rigid brakes on the edges at these slight movements. Most contractors come back after several months or maybe a year and fix these after the house has done "settling" ( your house not actually sinking). Is the same phenomenon that allows for truss uplift and breaking of drywall at roof to wall connection.
[gevagev] (score 103, diepte 1) Very true. He said it all correctly. The wood has to age. It's what we get for fast-farming pine and harvesting it so quickly. Get wood with huge grains (that absorb, lose moisture). I would say let it go through 1 cycle of seasons.....2 would be better,if you have the patience, then get a good sheetrock guy and a good carpenter to give your doors and windows a once-over. It is fairly normal, unless you frame your house with aged lumber, which is unheard of.
[geve3id] (score 90, diepte 0) You can really tell who actually works in construction based on these replies, jfc.

Anyone who said this is not normal and is a “serious issue” should be tagged as a “non-working lurker” or something so that everyone knows their posts can be disregarded.

Typically, (and most reputable GCs will do this) - we go back after a full cycle of seasons and fix the cracks in the plaster crowns, base, etc. 

Temperature and humidity shifts will cause cracking in any new construction.

Edit: yes the plaster job is dog shit but that’s a separate issue
[gev1who] (score 82, diepte 0) Looks like your house had high humidity during construction and now, since it's air conditioned, the wood is moving.
[gevpshb] (score 58, diepte 3) Kiln dried wood that gets rained on before roof and envelope can still come to life again. It’s wood construction.
[gevkwib] (score 35, diepte 2) > unless you frame your house with aged lumber, which is unheard of.

Dunno what they're doing nowadays, but when I was working in construction (1970s-1990s) kiln dried wood was used to frame houses, and this kind of thing most certainly wasn't common or considered normal.
[gev71ff] (score 31, diepte 0) This could be normal, maybe the house was built with very wet lumber. House will shrink 1 inch a year later,  most the time it shows up as cracked spackle in a wall but who knows maybe behind the wall is a missing support beam.  If he's a decent builder he already figured in going to your house at some point and fixing normal's spackle cracks from shrinkage. once it's repaired after the house is at least a-year-old if it happens again then its possible structural problem .
[gevaczj] (score 30, diepte 2) You're quite welcome. In my opinion, the builder should still fix it. Builders these days don't condition the houses soon enough.
[gevbk7k] (score 29, diepte 2) Now....go find yourself a piece of old-growth naturally grown pine from an early 1900s house. It's solid as a bowling ball. You can barely drive a nail through it.
[gevbdte] (score 28, diepte 1) Go look at Google Earth. Look at Palm Coast, Florida, the West side. Now, go back in time 5 years at a time. You will see what I mean. It looks like a checkerboard. They harvest the inverse acreage every 15 years. A 15 year old pine jacked full of Schwarzenegger juice grows WAY fast. It has huge, wide grains. It's like a sponge.
[gevfkzo] (score 28, diepte 1) Honestly your right. We should have a flair system to weed out those that know nothing and always open their mouths
[gevzpud] (score 22, diepte 4) Exactly this. Just because it's kiln dried doesn't mean it's warehouse stored and even then it can still absorb moisture from humidity.
[gev9lmo] (score 22, diepte 1 OP) Thank you for taking time to reply!
[gev9kwc] (score 18, diepte 1 OP) Thank you for taking time to reply!
[gew1pu0] (score 18, diepte 3) When they’re developing an area they’ll pour 5 or 6 foundations at a time. Then they’ll drop 5 or 6 loads of lumber. That lumber sits out in the weather snd absorbs moisture. They’ll go from frame to sheet rock in 10 days, long before the kiln dried lumber has acclimated.
[gev8ec8] (score 18, diepte 0) All these people saying it’s not normal, JFC of course it is. Especially if there was high humidity at the time of install and now the house is drying out due to the winter months. Or sometimes drywall can crack if it is mudded and taped in too cold of temps. The only thing I would say is NOT normal is for the builder to avoid coming back to touch up and fix these, especially if there are a lot of them. 

Structurally I wouldn’t be concerned, the cracks seem to be along the joints where two sheets meet and from the limited information doesn’t seem significant.
[gev5vtk] (score 17, diepte 0) Idk for sure about your cracking , could be from the framing drying out, but that taping job in the top left is horrific.
[gevradu] (score 16, diepte 5) I don’t think anyone installs drywall before a roof? What’s your point? Kiln dried wood that gets rained on doesn’t get compromised? Well it does. It’s also applies to cured firewood that can be spoiled. Yes drying in and loading in should occur, but it doesn’t. It’s cheaper to come back later to fix the cracks than it is to investing in dry heat, humidifiers and time.
[gevgogv] (score 15, diepte 4) Yeah. An old piece of pine is like oak. A new piece is like balsa.
[gew0cjt] (score 14, diepte 7) You're right, I actually own 2. I own a WM HM126 and a 10-30 lucasmill and a kiln I built. Of course mills don't pressure treat, I never said they do..
[gevr7wb] (score 14, diepte 3) Seems like they have been lowering standards on kiln dried wood. I get it sometimes and it still feels a bit wet.
[gew1zey] (score 12, diepte 7) He said green lumber, you question him for owning a sawmill, call yourself a carpenter/framer and don’t even know what green lumber is?!?! Don’t be such an ass out of the gate dude, you don’t always have to be a keyboard warrior. That’d be like telling a cement mason “green concrete” doesn’t exist lol. It’s a reference to young wet wood, or new concrete. God damn
[gevxabk] (score 12, diepte 4) I've noticed some of the wood at big box stores is heavy because of the amount of moisture in it. Absolutely crazy it can be sold that wet.
[gevjzxi] (score 12, diepte 0) We always moisture stabilize our builds before drywall to help prevent this. It has become more common to have cracks and it’s common because contractors don’t take the time to check moisture content of lumber or materials in general, it is also more common now because the industry standard is to use watered down gypsum joint compound so tape can be applied with a gun. It’s fast but produces the weakest joint possible. We bed and fill with setting type joint compound which is slower and  takes more skill but produces a stronger joint that has far greater crack resistance. Since using this method it has become extremely rare that we get cracks. If you have cracking every few feet that’s pretty sad. I would definitely hope it is repaired for free. Just know that if the tape is broken in the joints that are cracked they have to be retaped or they will crack through again.
[gew4kht] (score 11, diepte 9) Lmao that's a good one. Green means it hasn't been dried either by air drying or kiln dried. Better ask your boss lol. You could stand to do some googling and learn a thing or two before talking about shit you don't know
[geweiho] (score 11, diepte 8) I live in Florida, these arguments make no sense but I'm laughing in block and concrete.
[gevprhz] (score 10, diepte 5) Get a piece of pine from the late 1800s. You will immediately see the difference. It is basically a hardwood.
[gevfyk1] (score 10, diepte 1) Okay, I don’t do tract homes so maybe it’s different in that type of construction, but in custom home building we dry a house in before insulation.  We measure the framing lumber to get below an acceptable moisture content and bring in dehumidifiers if it’s not low enough.  

I guess we also use KD lumber to avoid this...  so maybe it’s just not realistic in less expensive homes...
[gevi1zb] (score 10, diepte 2) Oh it's different for sure.  When you go from dirt to a CO in 3 months that amount of attention to detail is unheard of.  Not saying the homes are crap, but production builders are all about the number of sales and closings.
[gevgkkl] (score 8, diepte 3) Its crazy how much tighter the grains are too
[gevsgrx] (score 7, diepte 6) That doesn't have anything to do with how it was dried initially though, just how it was grown.
[geway4c] (score 7, diepte 7) North east where? US? Or up County Durham way? Speak up boy
[gevyrse] (score 7, diepte 1) New Drywall cracking is not normal in my climate (Utah - high desert). We don’t usually get enough moisture to saturate wood framing, so we don’t have extreme shrinkage once a home is dried in. Remember that there are codes and conditions that are unique to geographical areas and what’s normal in one place can be abnormal in another.
[gevnzye] (score 7, diepte 0) Keep track with blue tape. Don’t call the builder yet, the cracks are just starting. The concrete and drywall mud have hundreds of gallons of water off gassing out of it. Lumber has some, but concrete and drywall mud has way more. Anyway, the cracks will continue. After about 9 months, call the builder and get on the schedule for crack repair.

Also while you’re looking around, look at all caulk joints in the bathroom around tub, tile, surround, etc. Also caulk joints around windows, doors, etc. Keep track of those also. Sometimes they open up and should be on your list also.

Then also keep track of any cabinet doors and drawer hinges and slides, it’s common to have adjustments to make.

Outside look at the same things and keep track of it.

With your builder the squeeky wheel gets the grease. And when anyone comes to do the repairs, have some nice muffins and coffee for them and you’ll get great service on taking care of those punch list items.
[gew18yc] (score 6, diepte 7) Did you completely misread his comment? He owns a saw mill, not a pressure treating setup. No one owns pressure treating setups lol, you sound stupid for even implying he said that. Lol
[gew3ysn] (score 6, diepte 9) Never seen brown pt?
[gewfo1o] (score 6, diepte 9) You mean we don't have to build our homes out of kindling anymore!? What year is it!?
[gevmwys] (score 6, diepte 2) Umm
[gewm4ws] (score 6, diepte 3) By the time 6 months to a year has gone by and it’s sat in the lumber yard for however long, the wood is pretty well dried out. Trust me. We are the second driest state in the country so lumber dryness is not gonna be any thing like many other states. I know a few people with new houses, I grew up in multiple houses built by my dad, and just finished my own basement; never seen drywall crack. You should definitely not assume site conditions are the same everywhere.
[gevpoi9] (score 5, diepte 4) Everything today is kiln dried. Has been since the 1920s, or so.
[gevrc99] (score 5, diepte 6) My entire house is built with heart pine. Built 1875. The growth rings on that stuff is insane. Gets beat up a bit as flooring, but agree it’s more comparable to oak than today’s SYP.
[gew4fqg] (score 5, diepte 11) You’ve never seen brown PT?! Where the fuck have you been working?! What color is copper green? Hahaha
[gew5jvs] (score 5, diepte 17) Coming from the man who plays call of duty mobile, bye bye
[gew3ed1] (score 5, diepte 5) fuck eh   


they don't make em like they used to ....trees.....lol
[gevakja] (score 5, diepte 1) Yep
[gev9mh5] (score 5, diepte 1 OP) Thank you for taking time to reply!
[gevdfto] (score 5, diepte 2) good luck hope it works out with the builder just  say the truth that your seeing a lot of cracking and it stating to worry you. maybe check your contract with the builder to see if there is anything allocated for 1 yr touch up
[gevix33] (score 5, diepte 3) IMO if the drywall cracks on every seam then some level of crap has occurred.
[gev9kga] (score 5, diepte 0) Looks pretty normal. Wait a year and then go through and have it fixed.
[gew5efj] (score 5, diepte 2) Enclosing and conditioning the space. Checking the relative moisture of the framing and bringing in dehumidifiers to bring it down if necessary. Making sure the sheets are also acclimated before they are hung.
[gev1nhz] (score 4, diepte 1) It’s 100% normal depending on the location.

Wetter wood or wood installed during the winter will shrink, as the wood shrinks the non-shrink drywall will shift slightly causing cracks.
[gew2s23] (score 4, diepte 8) welcome to reddit? 

||||
|:-|:-|:-|
||||
[gevqzg2] (score 4, diepte 5) If you buy from a big box store yeah, unless you're building a deck, then you can buy green treated lumber. I own a sawmill and can tell you people frame with green lumber a lot more than you think
[gewdzu1] (score 4, diepte 13) >Give it up, son. I can tell by your efforts, I've been driving nails longer than you've been alive.

I bet you're great to work with /s
[gew5jh4] (score 4, diepte 11) LOL I'm a bricklayer by trade and a sawyer on the side so don't even tell me I wouldn't last a day as a framer cause that's some funny shit right there. If you wanna start a pissing match I'd like to see you lay over 200 8" block in a day, struck both sides. Maybe I'd let you even hold the s jointer. Maybe.
[gew4yd5] (score 4, diepte 13) From a quick google search: “ brown PT is usually more expensive, it is treated with micronized copper azole, it is less prone to off gassing and fading” you sound like you’ve never driven a nail in your life you man child
[gew597x] (score 4, diepte 15) I bet you’re a troll or a handyman, my work here is done, I proved you’re a fuckin moron.
[gewg20i] (score 4, diepte 9) Green lumber is fresh cut non kiln dried lumber here in  the north west and PT is pressure treated, our PT is typically brown also not green.

https://joneakes.com/jons-fixit-database/1575-What-is-the-difference-between-green-brown-pressure-treated-wood
[gew5dln] (score 4, diepte 2) Drizzt
[gevh10e] (score 4, diepte 1) My sense is the “spackler” put the mud on too thick. A union Sheetrock guy once told me three thin layers min. But of course, they’re paid by the hour.

Edit: spelling
[gevsayu] (score 4, diepte 1) I'm in this sub to learn about residential work. I do Industrial work so a few things translate over, but not enough.
[gevxuz7] (score 4, diepte 1) I did residential in South Florida, I almost never did stick construction. Miami-Dade/Palm Beach wind codes made it easier/faster to just do block construction. Plus we don't have winters so this would not be known to me. Different building conditions in different parts of the country.
[gew9ofi] (score 4, diepte 1) Take a close look at the mud job on that wall. Forget the cracks, I would call that shit drywall  work. 
I’vs seen plenty of cracks develop in new houses but when you also see crap work like that it makes you wonder what the builder accepted from the other trades?
[gevkgwd] (score 4, diepte 0) Would you happen to be in the rust belt? Looks like typical hot/cold cycle growing pains. Your house is just sorting itself out; we usually send a guy out on 90 day Tarion report to fix nail pops and cracking as a complementary service. It is very normal to see cracking, however yours seems to be on the heavy end of normal
[gevopwx] (score 4, diepte 0) I could have run those corner joints better and I hate drywall.  The drywall guys must have run out of meth or something.
[gevr3qp] (score 4, diepte 0) New concrete disappoints me more now also. It can be done so that you don't have 10-20' cracks appearing a few weeks later. Builders that don't hold them accountable are mostly to blame.  I see it in basements most of the time but also in garages and driveways. Maybe it's the risk of building when it's above and below freezing every couple of days I don't know. The lumber shortage probably isn't helping your situation either. I have seen very technical explanations as to why cracks appear in your drywall. I still think it can be built to not crack as much or at all but builders want to maximize profits. You only need to make the house look perfect for a couple months and not fall apart before the one year warranty is up.

Siding installer who was fixing buckled siding yesterday. I didn't gap it enough. Thought the weather was cold enough so that material was at min expansion. I blame the siding maybe it was too green lol.
[geuwio0] (score 3, diepte 0 OP) It’s mostly in the center of the home. We did have to build the pad up quite a bit due to a sloping lot.
[gevycy1] (score 3, diepte 7) Which, in turn, has exactly everything to do with the time it takes to absorb and lose moisture. Why does everyone want to be Mary, Mary, quite contrary without qualifications?
[gew0tje] (score 3, diepte 7) If you read it correctly I mentioned decks using green treated lumber, not framing. You gotta re-read this stuff man
[gew3w54] (score 3, diepte 9) Hahahaa what do you call brown PT? We call PT... PT. Lol
[gew37hp] (score 3, diepte 7) what the heck? why are YOU coming HERE and giving issue with "everyone" and excuse me, but what the FUCK do you know about these anonymous online accounts and their qualifications?
[gew75pf] (score 3, diepte 13) Crack open another cold one and go back to your cave you fucking troll. Sleep it off
[gew7ijo] (score 3, diepte 15) No, I'm getting bored of the stupid shit you type. It was entertaining at first but now it's just obnoxious. For an old fella you need to grow up.
[gew4m99] (score 3, diepte 11) Please, google brown pressure treated lumber, it exists, and I use it every day. It is not aged from the sun lol
[gew30ga] (score 3, diepte 7) who said anything about pressure treating lumber? 

||||
|:-|:-|:-|
||||
[gewlajg] (score 3, diepte 11) You're welcome.

That is exactly the terminology we use here in the north west.

Just the other day I went there and got some 'green dough fir 2x4s' and a couple PT boards.

You say no on on any job but you're only considering your little tiny area of the country, not to mention other countries.  Names for construction materials vary widely. 

I suggest you google 'logical fallacies' because almost every one of your comments uses one.

Cheers.
[gewo64l] (score 3, diepte 13) > I'm not British. Neither are you. Bottoms up!

https://imgur.com/a/UHF0Yrg

You were saying something?
[gewgtrd] (score 3, diepte 5) Florida has entered the chat
[gevm4my] (score 3, diepte 4) Yeah, if that's how the finished layer looks, I'm betting it's not any better where you can't see.
[gew4a2t] (score 3, diepte 2) Speaking of monumental tasks....
(124 reacties met lagere score weggelaten)

