# Label-batch batch_0055

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
Schrijf het resultaat naar `batch_0055.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1wl1sbi, 1415zu5, 1guo8b4, 10dj2rk).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1wl1sbi ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2026-09-20  SCORE: 32  REACTIES: 155
TITEL: Are we ready to talk about chef toe
POST (source_id=post):
This is a new era for me. I’ve been in this position (50+ hours a week, AM, salary” for like 4 years now, but only recently has the chef toe become an issue. Is there anything i can help it? I literally buy hokas ($180) because they last me longer than clearance shoes and dont make me hurt but they do the chef toe. So if anytone has any tips/ recommendations please let me know

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[pavde6r] (score 178, diepte 0) You want a tow? Cuz I can get you a toe.
[pavdzda] (score 80, diepte 0) Are you sure it’s not gout?
[pavfdhp] (score 61, diepte 0) Hoka’s have a notoriously small toe box. If you’re spending that kind of cash get Brooks, or similar.
[pave3wf] (score 42, diepte 1) Amateurs
[pavjqsv] (score 40, diepte 0) I’ve been doing this almost 30 years now. Go buy some Red Wing Boots. They’re made for guys who are on their feet all day. They’re pricey but totally worth it. Plus you can get them resoled after a year or two.
[pavbdtx] (score 31, diepte 0) tape all of your toes together and then wear high heels.
[pavhz0p] (score 29, diepte 1) "Excuse me, sir. Could you please keep your voices down? This is a family restaurant."
[pavf40o] (score 28, diepte 1) I'm staying. I'm finishing my coffee.
[pavlguy] (score 27, diepte 2) Excuse me, sir?! For your information: the supreme Court has roundly rejected prior restraint.
[pavm1gc] (score 23, diepte 2) Listen here, lady (or dude). 
I've had friends die face down in the dish pit, so you and I can gather here and enjoy some shit posting together.
[pavku1w] (score 23, diepte 0) Find a podiatrist and give them $400. They will make you custom molded orthotics from a 3D scan of your feet. Then, get Brooks. But go to a shoe store like the one Al Bundy worked at that will actually fit your shoes to you. It could be a bunch of different things. But likely your weight is on the inside of your foot.
[pavnag5] (score 20, diepte 2) I fucking love when the dude throws his money down a joint is mixed in with the money and then he snatches it back up.
[paviyg7] (score 19, diepte 1) With nail polish
[pavofx8] (score 19, diepte 1) Bwaaah! Mah boy's not a ghoul!
[pavl3kg] (score 19, diepte 2) It’s common in on the feet jobs. A big part may be … sucks to hear… two pairs the same. Rotate as needed and lots of washing. Socks are key too
[pavk6ux] (score 17, diepte 2) By 3
[pavful6] (score 17, diepte 1 OP) Thank you for the coherent response 🤣unfortunately I’ve tried the brooks and my toes go numb in them 😢 the only shoe I’ve tried where my toe hasn’t gone numb is the hokas, i just lose my pinky toenail lol
[paw6wr5] (score 16, diepte 1) Fuck gout. Hit me last year at 33 and it's stupidly painful, everything I love triggers it :(
[pavqyaj] (score 16, diepte 1) Red Wings *can* be great, but you gotta get the right ones for your feet. Thoroughgood are decent too
[pavy1om] (score 15, diepte 0) You need to do foot and calf stretching. Look up various exercises videos for them. Find what works, but focus 20mins a day on massaging and stretching your feet. Maybe invest in 
 motion therapy specifically for your feet.
[pay4s7l] (score 13, diepte 3) I'm finishing my coffee...
[pavfxhw] (score 12, diepte 1) The most line cook thing ive ever heard
[paxzaha] (score 12, diepte 2) Calmer than you are
[pavnljw] (score 12, diepte 1) Hell I can get you a toe by 3 o’clock this afternoon
[pavnlv3] (score 11, diepte 2) I'd recommend a store. They have a thing to stand on that reads your size and you can try on a few different kinds
[pavd4fe] (score 10, diepte 0) Is this like bunions causing nerve pain in your big toe?
[pavp5fg] (score 10, diepte 1) There are ways, Dude.  You don’t wanna know, believe me.
[paw72dp] (score 10, diepte 1) Not to be a downer here but just saying get brooks doesn’t really fly. I sold specialty running shoes for over a decade. Within every brand they use different lasts or shapes of shoes if you will. Now if you had said buy Altras instead of broiks I would absolutely agree with you bc that’s their claim to fame. Making the widest toe boxes in the industry. Yes hokas are notoriously a narrow toe boxes but not all of them.   
20 plus years ago everyone with a wide foot would come in and ask for new balance bc they were told new balance were wide, but those wider  new balance versions might not fit the shape of their foot and you would have to fit the person and show them what actually did fit correctly.   
I always tell people to go to a local specialty running shoe store and get fitted by someone who’s worked there for a very long time and has a good reputation.  
Shoe companies constantly change stuff to stay relevant and one model can change then next year and not be the same.   
I used Altras in the kitchen for 3 years bc the toe boxes was awesome but they only lasted me 3-4 months tops and at $150 each it became a financial issue.   
Also running shoes suck in kitchens until the sole gets worn in a bit and doesn’t slide around as bad. But still super dangerous.   
Now I’m a Birkenstock Tokyo wearer for half the week and whatever running shoes that fit me the other half. Just depends on what I’m doing that day or how long I’m working.   
Everyone is different and has different hours, floors, stairs, feet, body weight, etc.   
the only right answer it to be fitted and keep trying things until you find what works and then home in on that.
[pavq14p] (score 10, diepte 2) They have brick and mortar stores. Like someone else said, you want togo to the store. 

When I went they took a 3d image of my foot. Then had me walk across a special mat. All of that builds into a digital image of the pressure points on your feet when you’re standing still and pressure points when you’re walking. That way they can get you into the right boot and place you with the proper insole. 

It really was night and day when I switched to properly fitted boots. I’ve worn all the different kitchen shoes over the years. These are hands down the best.
[pavwxi4] (score 9, diepte 2) Go see a podiatrist (if you can) or a shoe shop that specialises in running shoes for a proper fit.
[pavvh4l] (score 8, diepte 1) Nothing is fucked here Dude.
[paw0h5q] (score 8, diepte 3) One hundred percent TWO PAIRS THE SAME. Give your feet and the shoes a fighting chance. Also, I shop the hoka wides and use arch supporting inserts with a deep heel cup. Unfortunately custom inserts will run $350-ish.
[pavhuyv] (score 8, diepte 0) Your formula doesn't work. It might be missing a closing parenthesis. Camel toe is a natural reaction to too tight packaging. Maybe you're experiencing a similar problem.
[pavlbw2] (score 7, diepte 0) https://preview.redd.it/v1u7lihyvkqh1.jpeg?width=498&format=pjpg&auto=webp&s=fb6bed97c4076b7a555d162ae6e6b0ca949dd47e

  
Toes, you say?
[pavlsbb] (score 7, diepte 0) I only wear Birkenstocks. 

When I started wearing them (and no other kind of shoe), back pain lessened. (Still is painful if I'm stooping a great deal.) Foot pain vanished.

I buy them five at a time from some website in Germany (it changes every time I buy them). That way I have access to the world-wide product line. Not the BS Birkenstock America inventory.

This is the Harris model. 

https://preview.redd.it/1sgrkcnfwkqh1.jpeg?width=1200&format=pjpg&auto=webp&s=cf0211743bd62eff0f23ec1d8df2fb188ea2430c
[pavgf66] (score 6, diepte 1 OP) I was genuinely just asking for opinions and very clearly laid out what i have and have not tried. Sorry mr stonefoot i shall never ask for help on a forum that welcomes questions!
[pb0z42b] (score 6, diepte 2) With nail polish
[pavqv6o] (score 6, diepte 3) Did they die from chef toe(™)?
[payuqhd] (score 6, diepte 4) Enjoying my coffee
[pavkon2] (score 6, diepte 2) Thats extra
[pavpsbc] (score 6, diepte 1) With polish.
[pay1q6p] (score 6, diepte 2) Hit up your doc for allopurinal (uric acid reducer, taken daily) and colchicine for flare ups (it might destroy your GI tract for a few days, but it hurts less than gout. Everything hurts less than gout) it only gets worse as you get older.     
Stay hydrated, peeing is key.
[pavi8x6] (score 6, diepte 2) Asics! Also some Nikes have big toe boxes
[pavkmdk] (score 6, diepte 1 OP) Wait….. you’re a chef wearing the same pair of shoes. How often are you on your feet if you don’t mind me asking? Only asking because these fools in my comments are making it seem like 6 hours on your feet should be the blue print lol
[pawfjg2] (score 6, diepte 0) Bro, I’m going to need some more context around what “chef toe” is before I can offer any kind shoe advice
[pavuil7] (score 5, diepte 3) And they will not be forgotten! For a while.
[pawp0lu] (score 5, diepte 1) with nail polish an eveything.
[pavyos0] (score 5, diepte 2) But have you tried the red wings?
[pawd2ed] (score 5, diepte 2) Yeah I hate when people talk about a brand as if all the products are the same, most brands have a wide range of products and usually will have some cheap stuff piggybacking on the name built by the better stuff
[pavkd02] (score 5, diepte 0) On cloud has a bigger toe box than hoka. I gave up all mine for On Clouds.  You can find them on clearance at TJ Maxx pretty often. Hoka are great if you have skinny feet. 

I wore those for years while in a hospital lab, now I wear the On Cloud and it's the same pillow, but more room for my toes.  I put about 35k steps a day, and I don't ache after a shift.
[pawc862] (score 5, diepte 2) A theragun is worth every penny.
[paycucb] (score 4, diepte 1) Yes, chef!
[pavqufq] (score 4, diepte 3) Do they make them easily cleanable? If I'm buying expensive boots, I need them to last a few years at least.
[paw2605] (score 4, diepte 1) Best comment, hope OP sees it!!! Stretching them hamstrings and strengthen feet, ankles and knees
[paw6ukh] (score 4, diepte 0) What the hell is chef toe?
[pawbw0f] (score 4, diepte 0) The fuck is chef toe??? I’ve had gout and one toe is doing the inward thing but never heard of chef toe
[pawegbl] (score 4, diepte 0) "Chef toe" is finally one I've never heard of. What is that?
[pb19l0j] (score 3, diepte 3) By 3oclock this afternoon
[pb0z7ay] (score 3, diepte 2) I’m staying.  I’m finishing my coffee….enjoying my coffee
[pawuar3] (score 3, diepte 1) Yeah? You got a toe guy?
[paxkbo5] (score 3, diepte 1) Who’s your toe guy
[paz5dcl] (score 3, diepte 1) Who's your toe guy?
[pay8who] (score 3, diepte 3) This. No other “remedy” people offer will help. You will still get a flare up at some point. Get on allopurinol. 

I can eat/drink as much as i want of things that used to trigger flare ups and i haven’t had a single one IN YEARS since starting allo, and i used to have 6-8 per year before that.
[payrew6] (score 3, diepte 3) But Nikes notoriously run small and narrow because of the extra padding.
[pawc3rx] (score 3, diepte 4) Just buy birks
[pb3ux3d] (score 3, diepte 3) I’ve got the Birkenstock kitchen clogs (like crocs) with orthopedic inserts and they are so comfy for my wide, high-arched feet. I can work a 14 hour shift and my feet don’t hurt.
[paw76qk] (score 3, diepte 2) Shoes are too short most likely if you’re losing toenails
[pavjm8e] (score 3, diepte 0) I know it's going to seem insane because they're a heavy shoe but I wear Merrell Moab 3s in a wide with some pretty expensive shoe inserts. have been my daily drivers since I was 17 and I'm now in my mid twenties. Don't get the waterproof versions though, otherwise your feet are going to develop athlete's foot.

my two cents
[pavlu8h] (score 3, diepte 2) Sorry, that does read as if I had the same pair of shoes 😅 I get a new pair of them every 2 years/ 2.5 years.

I usually work about 50, sometimes when it's really busy during a Town event / college events I'll work up to 70
[pawj6au] (score 3, diepte 3) Store is a must when you're going to be blowing $200+ on a pair of boots.

They also sell specialty gear.  I had a job where I needed ESD footwear *and* steel toes.  They make a pair of shoes that look like cross trainer sneakers but they're conductive and steel toe/shank.  Guys on the dock tried to make me wear the cow cloppers and I tapped the toe on the floor.  Blew them away... Till I said they were redwings 😂
[paw0t3x] (score 3, diepte 5) How is the non slip compared to other brands you've tried?
[paw8jpz] (score 3, diepte 6) They are on par with any other shoe in the wet. Oil/grease on the floor and they slip a bit. But so does any shoe. A plus is the tread don’t catch and hold food particles.
[pavpzhy] (score 3, diepte 0) Honestly, depending on the severity, you probably need to see a podiatrist
[pavvxad] (score 3, diepte 0) I really recommend a shoe with a heavier sole and a deeper footbed for long lasting foot health.    I am a long time user of Timberland Pro work shoes.  My last 2 pairs over the last 4 years were

https://www.timberland.com/en-us/p/timberland-pro/mens-footwear-10171/mens-titan-ev-composite-toe-oxford-TB0A5ZBY001

The foam insoles and soles of sport shoes are not designed for long hours of wear, they compress and lose their support the longer worn.    Firmer soles and insoles designed to resist compression are the best thing for your long term foot health.  Just my two cents as a 57 year old Chef with 40 years professional experience.  And still going strong!
[pavy9ke] (score 3, diepte 0) I love how helpful this thread is
[paw7rri] (score 3, diepte 0) Ive been in kitchens for 25 years and I have no idea what chef toe is.
[paw9703] (score 3, diepte 0) Hokas are not good for your feet. Too much support discourages the muscles in your feet from working, they get weak, arches suffer and your foot health suffers. This is why I’ll always buy Birki’s, easy to shuffle on and off your feet, encourages foot muscles to work and supports foot health.
[paypimh] (score 3, diepte 1) Been in kitchens for decades and have never once heard “chef toe” and neither has Google. Wild.
[pawc022] (score 3, diepte 0) Birkenstocks rest your feet better and keep you off your toes
[payamok] (score 3, diepte 0) What is chef toe?
(89 reacties met lagere score weggelaten)

=== THREAD 1415zu5 ===
SUBREDDIT: r/bartenders
DATUM: 2023-06-05  SCORE: 36  REACTIES: 153
TITEL: Bartenders what shoes do you wear?
POST (source_id=post):
I’m 39 starting working 26 hrs in two days. My feet hurt. Please let me know what the best shoes insoles are.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jmypynu] (score 74, diepte 0) Don’t underestimate the power of compression socks and good insoles as well!
[jmyw2cg] (score 53, diepte 0) Dr Martens, I've always wore DMs while bartending and I always will.
[jmz3r0p] (score 29, diepte 0) Sketchers non slip work shoe
[jmyw81b] (score 22, diepte 0) Sketchers go walk slip ons
[jmz376y] (score 17, diepte 0) Chuck 70s+. Yes I’m an idiot
[jmzi1h4] (score 14, diepte 0) Chelsea boot Blundstones. Easy to break in, easy to clean, and they look good AF.
[jmyov5s] (score 13, diepte 0) I wear redwing iron rangers, the break in period is kind of rough but after that they fantastic. My old mentor swears by dansco clogs, and a lot of chefs I know wear them.
[jn0dwq5] (score 11, diepte 1) I bought compression socks for the first time recently, game changer.
[jn05xm0] (score 11, diepte 1) Docs with insoles, every day.
[jmzhkad] (score 10, diepte 0) Im 38, i work 32 hours in two days every week. Blundstones + knee sleeves do the trick for me, no pain at all
[jn098u7] (score 9, diepte 1) Yes, this.  Spring for the slightly more expensive ones that are marketed as memory foam
[jmz5iww] (score 9, diepte 0) Hoka Bondi 8 extra wide
[jmzejez] (score 9, diepte 0) On god Dr Marten's are unofficial Bartender uniform tbh

Can be worn every day for years on end, neigh indestructible, and have simultaneously withstood boiling water, oil, and certain combinations of liquids I'm sure would melt through anything shy of lead.

Plus they look hella hard funky
[jmyt7ei] (score 8, diepte 1 OP) I bought a pair of doc martens I wear during winter. They feel pretty good but are heavy. I also deliver pizza for one the big three here in the states 50 hr weeks. Woof!
[jmyy666] (score 8, diepte 0) I wear hokas or brooks, with special inserts. They’re expensive, ugly, and get dirty.. but my feet have never hurt. I feel like I’m walking on clouds and it helps my posture.
[jmzaj5d] (score 7, diepte 0) non-slip restaurant Hokas
[jmzee14] (score 7, diepte 0) Lots of great shoe recs here but to add to this: get a pumice stone from the drug store and scrub your feet with it in the shower after your shift. I don’t even know how it works…but holy shit does it help the soreness. Also keeps your feet from getting long term damage. Costs like $1-$4 max
[jmzf17a] (score 6, diepte 1) Seconding Sketchers. They were a life saver for me.
[jmzags7] (score 6, diepte 0) When I was in my early 20's I'd wear black military boots. I was in the Army Reserves so those were still very comfortable for me. That lasted maybe 2-3 years.  After that I dabbled with a few things before finally settling on Nikes and have worn them ever since. For me they were the most comfortableshoe to work in.
[jmyzeqa] (score 5, diepte 0) 15 years in the industry, I finally got Docs. Best purchase imo
[jn0rk47] (score 5, diepte 1) I do not second this. They offer little to no support. If youve already got foot pain, they probably wont help.
[jmzcy43] (score 5, diepte 0) I wear old school vans sometimes and other times I wear leather palladiums (boots) that are lace ups but with a side zipper. I wear insoles in all my shoes, usually just pretty cheap ones like $15-$20.
[jn0gygc] (score 4, diepte 2) Well rubber soles are naturally non slip but they do have a version with additional non slip protection yes
[jmz2x6z] (score 4, diepte 0) I wear crocs. You’ll say I’m lying but 50 hour weeks and no sweaty feet.
[jn0nsr3] (score 4, diepte 1) When I lost weight and always had rubber mats under my feet, I really loved working in chucks. They have a lot more cushion than I remember from when I was a kid. When I was 20 lbs heavier I could not wear them for long but they’re so light on my feet and have enough cushion that I could stand on them all day so long as I have the rubber mats.
[jn1em8k] (score 3, diepte 2) Shoes for Crews are garbage. Sure, they're non-slip, but the build is garbage. They fall apart after a couple of months. Higher end shoes will last you years, especially if you have two pairs abd throw shoe trees in them between wears. The price per day is much lower.

Buy cheap, buy twice(in this case, about a dozen times).
[jmzrz7z] (score 3, diepte 1) Do they make nonslip Hokas? I have friends that swear by them but they don’t need nonslip shoes
[jmyynms] (score 3, diepte 0) Merrell Jungle Moc Pro Non-slip with Darn Tough merino wool socks.
[jn0dzjz] (score 3, diepte 1) These. I have a pair and they’re unbeatable.
[jmzat5g] (score 3, diepte 0) Blundstones all the way
[jmzlhe5] (score 3, diepte 0) For most shoes superfeet insoles are amazing, not cheap but worth every penny. You'll think I'm mad but I wear handmade dress shoes and find them comfier than anything else. Seems an expensive purchase at first but they still look great after 20 years (resoled at the cobblers as needed). Also, rotate between different pairs of shoes on a daily basis, this trick is so kind to your feet.
[jmzyd0z] (score 3, diepte 0) 41 years old, 25 of those years in the service industry.

I switch between Nike Cortez, Nike Dunk SBs, and Air Jordan 1s. The SBs the way they come out of the box, the other two with insoles.
[jn0huqy] (score 3, diepte 0) I’ve switched to GoClove which are hospital shoes so they have extra support, are non slip, and easy to clean if needed. Prefer this to sketchers because the padding on the sketchers have worn down a lot faster
[jmyta5y] (score 2, diepte 0 OP) Also actual shoes and not insoles. I heard crocs but I don’t know. Scared.
[jmyugqz] (score 2, diepte 0) My On cloud shoes do me good
[jn3sblb] (score 2, diepte 3) I don't go crazy with orthotics or anything. The best I've found is Dr. Scholl's Heavy Duty. They're designed for folks over 200 lbs, and they're fantastic.
[jn0a7k0] (score 2, diepte 1) Do they have non slippery shoes ?
[jn2f7uv] (score 2, diepte 1) yes.  the only shoes that don't make my feet burn after an 8 hour shift are the skid resistant Chelsea docs.  I will never change either.
[jn2ha05] (score 2, diepte 1) I love them, but why are they so heavvvyyyy 🥲
[jmzx7r2] (score 2, diepte 2) They do. Hokas are an expensive life saver and significantly reduce the barking of the dogs.
[jmzxqiz] (score 2, diepte 3) Thank you!! I usually wear Docs now, but I was hoping for a lighter pair of shoes for the end of the week or busier nights when I’m just not feeling it anymore haha.
[jmzubkl] (score 2, diepte 1) Thanks for the rec! Didn't realize Merrell made non-slips, I love my Salomon's but they're a slippery bitch and Alama's just aren't as comfy.
[jn2jey0] (score 2, diepte 1) Oh my god I’m so happy I’m not the only one. People call them my dad shoes because I’m still in my 20’s but they are so great. I like the steel toe so I feel safe around kegs and they act as a great chankla or ball crusher if needed.
[jmyz3pr] (score 2, diepte 0) Doc Marten Chelsea boot
[jn0dykx] (score 2, diepte 1) 48 years old, lifer here. Sketchers all the way.
[jmz53d8] (score 2, diepte 0) Dr martens and wool socks🍻
[jmz7bv9] (score 2, diepte 0) Doc martens
[jmz95x7] (score 2, diepte 0) Dr. Martens with a canvas upper- no break in period, just pure comfort from day 1. They are usually in discount stores like shoe carnival too.
[jmz9czq] (score 2, diepte 0) Redwings
[jn501kd] (score 2, diepte 1) These changed my life. They're not cheap but it's beyond worth it. I've had them for about 8 months now and they've held up great and eliminated any foot pain despite me being a big dude working on tile floor all night.
[jmzc5l5] (score 2, diepte 0) Got lace up docs last year. They can feel heavy at first but you get used to that pretty quick. For regular shoes I get the new balance ones from shoes for crews. They weigh so little it almost feels like you don’t have shoes on.
[jn2fczj] (score 2, diepte 1) I love a good peppermint foot scrub
[jmzl2o1] (score 2, diepte 0) I’m 40 and put Dr. Scholls in my converse. Or Dr. Scholls shoes you can buy online.
[jmztgby] (score 2, diepte 0) Hokas are absolute life savers for those of us with feet problems
[jmzvd7s] (score 2, diepte 0) Adidas Adi Boosts!! I’ve never had an issue and they’ve last me 2+ years with the same pair. they were around $180 but well worth the money
[jn0qzcd] (score 2, diepte 2) They’re still releasing them, just way harder to get than the other SBs. I have some Blazers, just haven’t used them at work yet since the only ones I have are suede and I tend to stick with leather for work. They feel a little narrower, but they’re still comfortable.
[jn05t1x] (score 2, diepte 0) When I first got in, 20+ years ago, Shoes for Crews. Then moved to Doc Martens and shortly after surplus army boots, the tan ones were decently comfortable, I would even go for hikes with my dog in the army boots. 2015 started Nike airmax and those were SUPER comfy. 2019 went with compression socks and Nike Cortez, this was the best combo that worked for me. I haven’t been behind a bar since 2020. I cannot stress the compression socks enough! I went on and on about the compression socks at my last place, but my 35+ self speaking to 20-somethings, it didn’t translate. I wish I had discovered the compression socks in my 20s. :)
[jmzhmc5] (score 1, diepte 1) Havent made the move to kitchen clogs but it’ll happen soon, seems like a top tier work shoe
[jn23wb6] (score 1, diepte 2) Those nonslip crocs be hittin different fs
[jn389vu] (score 1, diepte 3) They’re only good for so long. 2 years deep and strongly feel like switching up. Until then they’re still my workhorses.
[jn3bscz] (score 1, diepte 2) They work?  Just by adding support?
[jmzlk41] (score 1, diepte 1) Any shoe is a million times better with a **good** insole. I like superfeet a lot
[jmzrj5d] (score 1, diepte 1) I'm on here always singing the praises of Shoes for Crews. Huge selection, some familiar brands, good prices, and they have a 30-day return policy- you can wear them *at work, in a restaurant* and if it's within 30 days they'll refund you or you can exchange them.

I've had Hokas and for the money I just can't justify it, they lasted me about 6-8 months when my Shoes for Crews or Sketchers last week over a year. 

I recommend spending at least $80 for your feet/ankles longevity.
[jn31ddg] (score 1, diepte 5) For work or not for work?
[jn308xv] (score 1, diepte 2) Which insoles would you recommend?
[jn4qgj9] (score 1, diepte 1) Really? I used to love Docs and Rockports,, but I feel like now they're another example of "They don't make them like they used to."
[jn6xpll] (score 1, diepte 1) But they’re ugly AF.
[jmywxa1] (score 1, diepte 0) Brogues
[jmyxe2a] (score 1, diepte 0) CAT sneakers for me personally! Decent, rather robust build quaility but also pretty comfy.
If looks don’t really matter for you then chefs in our kitchen swear on clogs.
Doc Martens also a great choice but I found them a bit too heavy for my taste
[jn11af5] (score 1, diepte 2) They make a pair specifically for service workers/nurses, etc. I believe they're the Bondi SR's! I mostly work in Docs, but the Hokas are really damn comfy, too.
[jn11u36] (score 1, diepte 3) Thank you!! I’ll look into this! I wear docs exclusively but I’m trying to find a lighter shoe for the busier nights and end of a few days in a row shifts haha
[jn471ma] (score 1, diepte 1) I also wear hokas. They come in wide sizes and are non slip
[jnfk75h] (score 1, diepte 2) I wish Salomon or Altama made some kind of non-slip, I can't get the look of Merrell's sadly
[jmz4e50] (score 1, diepte 0) I have some cheap slip ons with memory foam in them.  When my feet start to hurt, I switch to my Shemipro hiking shoes with insoles and 2 pairs of socks for a couple days.  They look like socks woth a bedliner sprayed on the bottom, but it works.
[js39yoh] (score 1, diepte 1) How does the canvas hold up against water, juices, liquor, etc?
[js3bpxh] (score 1, diepte 2) I have never had wet feet, ever. The shoes can be thrown right in the washing machine and they come out looking awesome, but generally don’t ever look stained from work, I mow in them so I have to wash them. Seriously I walk through puddles in these shoes and they last for many years.
[jn53ump] (score 1, diepte 2) I added the powersteps insoles as well and it's like walking on a cloud.  before I would get off an 8 hour shift,  crawl to my car and then from my car to the house...now I can walk around after work, run errands or go to the after party &I'm still ready to go.
[jmzbddh] (score 1, diepte 0) Red bricks, super comfy and s3 level safety! For me the anti slip is the best! 

I got these from a different site: https://www.workwearonline.shop/en/redbrick-azure.html

I think they can easily be found sub 100 dollars/euros
[jmzds7o] (score 1, diepte 0) I wear Sorel boots with insoles and compression socks, so damn comfortable right out of the box and I’ve been wearing them 50 hour weeks for about six months with no visible wear.
[jmzmvwk] (score 1, diepte 0) Orthofeet.com … I’m 32 and love these
(83 reacties met lagere score weggelaten)

=== THREAD 1guo8b4 ===
SUBREDDIT: r/Target
DATUM: 2024-11-19  SCORE: 58  REACTIES: 146
TITEL: what shoes do yall wear? my feet are in pain
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lxvi9ee] (score 56, diepte 0) hokas my guy
[lxvox78] (score 20, diepte 0) I always end up in some sort of adidas but I see my coworkers in their crocs and wonder
[lxvq6y0] (score 20, diepte 0) Brooks. I’ve tried all the others. After a couple months I get inserts
[lxw105i] (score 15, diepte 0) As someone who has worked jobs that require long hours of standing and walking (cashier, security, blah blah blah) for like 11 years, here is what I suggest:


- If you're able to (time, money, insurance, etc), see your doctor. They will be able to give you the best suggestions and care resources for you specifically. 

- Shoes that are not super tight on the feet, something a bit roomier (proper sports/tennis shoes and work boots are the first thing to come to mind)

- If you have something structurely wrong with your feet, look into orthotics. Some structure issues include but aren't limited to:
    - [Plantar Fasciition (or Plantar Fasciitis)](https://my.clevelandclinic.org/health/diseases/14709-plantar-fasciitis)
    - [Flat Foot](https://my.clevelandclinic.org/health/diseases/17005-flat-feet)
    - [Cavus Foot (High Arch Feet)](https://my.clevelandclinic.org/health/diseases/21719-high-arch-feet)

- Even if you don't have something structurely wrong with your feet, look into insoles of some kind, such as the Dr Scholl's gel insoles.

- STRETCH YOUR FEET. It may sound weird but there are foot stretches and exercises available. [These stretches from Harvard Medical School](https://www.health.harvard.edu/staying-healthy/exercises-and-stretches-for-foot-health) are pretty good and almost all of them have been suggested to me by various physical therapists over the years.

- Even if you're doing a task that requires standing in one place (like being a cashier), walk as much as you can or shift your weight around as you stand. Not sure 100% on this as i noticed this for myself, but if I stay standing in one spot and or shift my weight repeatedly in the same areas (like rocking back and forth when scanning and setting down items), I hurt WAY more than if I take a few steps or rotate my weight on my feet every 15-20 minutes.

For myself, I have flexible flat feet (explained in link on flat foot earlier on). I am *supposed* to have arch support insoles, but I don't have the money to get proper ones that are best suited for me as it's most effective (so I'm told) to have custom insoles/orthotics and....I'm a cashier at Target I don't make that kind of money. I also just haven't found any pre-made ones that work that have even close to the correct amount of arch support I need.

 I regularly wear a pair of steal toed ankle boots that I wear with the Dr. Scholl's Massaging Gel "Work All Day" insoles, which I've been doing roughly for 4 years now, starting when I worked security in a manufacturing plant that had me walking 8-10 miles a day. For me, that's been the most comfortable I've been on my feet.
[lxw66xa] (score 12, diepte 0) Anything with a wide toe box and good insoles.
[lxx211y] (score 10, diepte 0) A higher quality running shoe.  I have two pairs I have to alternate or my feet hurt.  I use either Brooks, Saucony or Ascis.  I also usually ruin them in 6 months sometimes less depending.   I usually go through 4-6 pairs a year.
[lxyd0ru] (score 9, diepte 1) Ew
[lxxzha3] (score 8, diepte 2) Compression socks are also a must.   Keeps fluids out of the feet.   Yeah I'm an old guy, but the little whipper snappers wear them too!!!  12 hours on concrete will do a number on anybody.
[lxvpst6] (score 8, diepte 0) New balance
[lxvs46t] (score 8, diepte 0) Toe shoes. I used to wear them as a runner, and now i wear them for the comments.
[lxxdeo8] (score 8, diepte 0) ASICS ARE SO UNDERRATED
[lxx5hh7] (score 7, diepte 1) I’ve never worn them but a coworker was just talking about them yesterday. She swears by them
[lxw72sy] (score 7, diepte 1) I also wear adidas!
[lxwjhfp] (score 6, diepte 0) Hokas
[lxxssbw] (score 5, diepte 1) Hoka transports! Or my Nike air forces. Genuinely both are so comfortable for 8 hour shifts
[lxwc7jl] (score 5, diepte 0) converse are my go to
[lxz8f06] (score 4, diepte 3) I'm in my 30s and I wear compression socks. it should be a retail standard.

My shoes: Adidas Kaptir 3.0. (cloud foam).
[lxwx89d] (score 4, diepte 1) Also wear brooks
[lxyuwjq] (score 4, diepte 1) Same for Brooks. Also with the custom inserts from Roadrunner. Idk how my OPU coworkers do it in converse or vans. My knees could never
[lxzfook] (score 4, diepte 3) Then that’s their business, no need to downvote 😂
[lxxytgq] (score 3, diepte 1) My OM got me hooked on them 4 years ago.   Never looked back.   Now,  I'm a Lead and when new hires come in, that is part of my onboarding speech.
[lxyua2l] (score 3, diepte 1) Hoka Kaha and Hoka Anacapa with a Dr. Scholl’s Gel insert both works wonders for me. I’m an Inbound TM.
[lxza33d] (score 3, diepte 1) I did the hoka thing and they were ok for about 4 months and then feet started to hurt again. I wear crocs. (They make ones that are regular shoes) best shoes ever. I look like a tool but now wear crocs most of the time. I have bad feet and the shoes are about $40 and are good for over a year.
[lxzg3lg] (score 3, diepte 2) The thing with Hokas is you gotta have multiple pairs and swap them out so you're not wearing the same ones day in and day out. I know they're pricey and it may not be feasible to get 2 pairs at once, but even if you just alternate them with a crappy random sneaker and give them a day to "rest" they'll hold up longer. (I learned this the hard way lol)
[lxyek6b] (score 3, diepte 1) Brooks are elite
[lxyfq7r] (score 3, diepte 1) Yeah I switched from hokas to brooks and I like the brooks a lot more. Hokas didn’t have enough arch support for me and the heels start to get worn out quicker than I would like
[lxxj8rd] (score 3, diepte 0) panda dunks or air force ones
[lxyu9tu] (score 3, diepte 1) They're going to pay for that once they get into their 30's.
[lxz3lim] (score 2, diepte 3) Agree so much on the compression sock thing! Well worth the price tag, I use copper fits and was impressed with how well they hold up!
[lxvnxj8] (score 2, diepte 0) air maxes! i heard new balances are good aswell
[lxz1bsh] (score 2, diepte 1) My pair of air max 90s were one of the most comfortable shoes ive ever worn but now I just wear some jordan 5s because the inside is really comfortable and spacious.
[lxvpuxs] (score 2, diepte 0) Skechers ❤️. It’s good for 10-15K steps.
[ly0txdt] (score 2, diepte 3) Or cause they're all like 18-20 and their bodies haven't started failing them yet
[lxzo1s1] (score 2, diepte 2) Yup, those are the comments lol
[lxvsihu] (score 2, diepte 0) vans (i have flat feet)
[ly0rltp] (score 2, diepte 1) I said converse because after years of foot problems including plantar fasciitis and collapsing arches multiple doctors appointments and treatments it’s the only shoe that works for me but everyone is different. I didn’t downvote those who mentioned brands that would and have destroyed my feet
[lxwgrif] (score 2, diepte 0) Inserts are the key my friend for your shoes
[lxwr4ge] (score 2, diepte 0) Sketchers saved me
[lxy0z0h] (score 2, diepte 4) I have a foot drag in one leg and boots are too heavy, it's causes me to trip.
[lxyzjhx] (score 2, diepte 0) brooks. not cheap but best close toed shoes i’ve worn
[lxzw9h5] (score 1, diepte 1) I had never heard of brooks or hokas until one day i was venturing about town on my scooter and seen a "running soles" store in our town square of all places. I assumed they had brands like nike, skechers, adidas but they have some i had never heard of like hokas, brooks and altra.

Got the hokas arahi 7 onsale for $125 after the saleswoman sold me on them and cringed a bit at the price (somehow my air forces cost less).
[lxvjg49] (score 1, diepte 0) some of my coworkers wear skechers, nikes, hokas! i wear docs and they’re decently comfortable!
[lxvlfqm] (score 1, diepte 0) i used to swear by my vans but recently i got a pair of reeboks with a comfort footbed by ortholite and have noticed i am significantly less tired after my shifts…so maybe my vans were hurting just a little bit
[ly0s19a] (score 1, diepte 2) Cuz they got stronger bone and muscle?  🤣
[ly0vvtj] (score 1, diepte 4) I'm jealous
[lxvqg59] (score 1, diepte 0) New balance 990v5 and 990v6
[lxyi34l] (score 1, diepte 1) I second those insoles
[lxw63sn] (score 1, diepte 0) Adidas Ultraboost, Nike Invincible 3, Hoka Clifton 9s, New Balance 880s. Cheapest ones out of all these are the 880s. 4 shoe rotation.
[lxxbc38] (score 1, diepte 1) Not you being downvoted for saying what shoes you wear
[lxyukib] (score 1, diepte 2) They're so bad for your feet in every way.
[lxztm5q] (score 1, diepte 4) OP "my feet are in pain" this guy "yo get some converse". 

He gave a bad answer and got corrected. Converse are bad for your feet. Dont recommend shoes that are known to hurt feet lol.
[lxyvc2x] (score 1, diepte 1) My GP is seeing a lot of people who wear Vans, Converse, and Sketchers getting dermatitis on their feet that looks like moccasin athlete's foot. It's an allergic reaction to the glue they started using for the insoles.
[lxxufwp] (score 1, diepte 1) Or save yourself money, buy a quality pair of boots that can be resoled. I was also going through shoes about every 2-3 months as a FFTL
[lxxy5ry] (score 1, diepte 2) Unfortunately I can't wear boots and most boots don't support high arches well enough.
[lxxde89] (score 1, diepte 0) I wear some boots I've had forever. Can't remember the brand off the top of my head, something I bought online. Despite the fact that most people think I'm in pain, they're actually pretty comfortable for me, but each person differs.
[lxxekn6] (score 1, diepte 0) Saucony, Nike Journey, Hoka, On Clouds I wear different shoes every day.
[lxxggp1] (score 1, diepte 0) Hokas for sure, they’re expensive but a very worthy investment
[lxxhq3q] (score 1, diepte 0) Brooks
[lxxiobj] (score 1, diepte 0) Insoles are key. Get the Dr Scholls from hba with your employee discount.
[lxxjxav] (score 1, diepte 0) Kurus. Seriously a game changer
[lxxmbgv] (score 1, diepte 0) Tom’s, because I like pain and don’t learn.
[lxxn3oy] (score 1, diepte 0) New Balance Fresh Foam with Dr. Scholl’s work insoles.
[lxxn6tk] (score 1, diepte 0) Nike Quest 9
[lxxon27] (score 1, diepte 0) Skechers
[lxxosqi] (score 1, diepte 0) new balance 608 in a wide size even if you don’t have a wide feet. no more toe blisters!
[lxxrlha] (score 1, diepte 0) the only shoes that have made standing for so long tolerable are vans 😭
[lxxsy3s] (score 1, diepte 0) Hoka
[lxxtmn6] (score 1, diepte 0) rick owens abstract ramones
[lxxtmvt] (score 1, diepte 0) Black timbs & black hoodies. 
What would Biggie wesr!?
[lxxtq1x] (score 1, diepte 0) Converse and sketchers 🕴️
[lxxu1k5] (score 1, diepte 0) I would highly suggest a good pair of work boots and then rotate in tennis shoes once every so often
[lxxu7gp] (score 1, diepte 0) New  Balance 
Hoka 
Brooks

Worth the price, hands down!
[lxxuezp] (score 1, diepte 0) Brooks! Or bobs if you want a cheaper op
[lxxvvjc] (score 1, diepte 0) I was wearing hokas at first but they made my feet hurt pretty bad. Then I switched to asics and it’s been way better. The shoes will also probably depend on whether or not you have flat feet, high arches etc
[lxxzbxr] (score 1, diepte 0) Black timbs and dr scholls
[lxy2crm] (score 1, diepte 0) Sketchy Skechers do the trick —
[lxy2f9g] (score 1, diepte 0) Sketchy Skechers do the trick —
[lxy2kwd] (score 1, diepte 0) Brooks with a different insole I can’t remember the name of
[lxy38cd] (score 1, diepte 0) My regular New Balance sneakers, with arch support insoles. Total game changer.
[lxy3mcf] (score 1, diepte 0) Doubling down on Hokas. First non-food or utility purchase I made after starting at Target. Best decision I made.
(66 reacties met lagere score weggelaten)

=== THREAD 10dj2rk ===
SUBREDDIT: r/KitchenConfidential
DATUM: 2023-01-16  SCORE: 36  REACTIES: 138
TITEL: Need to buy a new pair of kitchen shoes. Don’t know what to get. What does everyone wear?
POST (source_id=post):
Shoes for crews hurt my feet. Vans are comfortable, but I don’t like falling. Any other brands that are good? Help make my feet happy and I’ll owe you a dish shift or relabel your walk-in.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j4lvqxj] (score 45, diepte 0) Birkenstock non slip Bostons with good socks. Been wearing them for over 30 years. Worth every penny in my opinion.
[j4lq95r] (score 40, diepte 0) Grab a gel insole. I think all shoes for crews hurt everyone's feet!
[j4lqimq] (score 33, diepte 0) Crocs I’ve always liked or my doc martins
[j4m1xek] (score 23, diepte 2) If your feet are hurting constantly, you might have some foot issues that would be vastly improved by visiting a podiatrist and getting a set of orthotics. They’re custom molded to your foot via a laser scan and they make every shoe feel like it’s custom fitted to your foot. I haven’t felt uncomfortable in my shoes since I was 11, even after working in the industry and standing all day. They’re not cheap necessarily, usually come in around $500, but they last for years and they’re absolutely worth it.
[j4ludhh] (score 17, diepte 0) Blundstones nonslip work boots with a Dr scholls gel insole. Been using them for years. Kinda pricey but they will last forever.
[j4m18qm] (score 16, diepte 0) Bistro crocs are indestructible, easy to clean, breath well, affordable. I use them as an exec chef in a large restaurant.

Edit typo
[j4lwp5k] (score 13, diepte 0) Honestly I’ve been rocking a pair from Walmarts non slip section and they’re super comfortable, have insoles, look professional, cost like 40 bucks and the first pair lasted me a whole year and I’m on to the second.
[j4m5dsy] (score 9, diepte 0) Hiya! I just got a new pair of Birki Professionals. They’re polyurethane nonslip clogs with an oil-proof cork insole that molds to your foot. 


Best kitchen shoes I’ve ever had.
[j4lvj89] (score 8, diepte 2) That's why you need the Dr Scholl's. They have nice arch support. Better than the off brands do, speaking from experience.
[j4macsw] (score 8, diepte 1) They last forever and if the soles wear out you can get them resoled.
[j4m0f63] (score 8, diepte 0) I wear birks, but half my kitchen swapped to the new snibbs brand and they seem to like them quite a bit
[j4lrg9a] (score 7, diepte 1 OP) Shoes are beyond throwing a jelly in them lol
[j4nak44] (score 6, diepte 1) I recently obtained some Docs, thinking they'd be perfect for winter. Almost immediately noticed my entire body hurts more, and definitely not non-slip. As soon as I can afford H&B vans crossovers, I'm getting another pair. They'll be my 4th. Cold feet be damned, that's what woolen socks are for.
[j4lykrx] (score 6, diepte 0) Sketchers cessnocks. Probably the most comfortable shoes I own. Went through a lot of crap before finding them. They’re essentially slip-on sneakers, but have great grip and good support. Don’t need to buy separate insoles either.
[j4lzpqn] (score 6, diepte 0) been wearing birk profis for about a month and love them, just take a 12hr or two to break them in. there’s also a startup i’ve seen called Mise but haven’t heard many reviews on their shoes
[j4ltkki] (score 5, diepte 0) Genuine Grip clogs. With Dr Scholl's Work Gel Insoles.
[j4lxxv0] (score 5, diepte 0) Personally I like docs. You gotta break them in first, but theyre sturdy and I never feel anything that falls on my feet accidentally.
[j4m4uz5] (score 5, diepte 0) I wore MOZO Sharks slip ons for several years and they were super comfortable and held up well to the 80k-100k steps I put in each week, but somewhere in the past couple years, the quality really took a dive and they would only hold up for about 6 months before they started falling apart. (Plus they discontinued the cool looking red skull stitching).

I made the switch to KEEN Utility PTC Slip-On II the last time around, and other than the non skid sole taking a week or two to break in, they’ve been fantastic so far. Comfortable, reasonably good looking, and durable. Amazon just knocked $40 off the price, so they’re about $100 right now. I also put a pair of heat moldable SOLE inserts in them (pop the insoles in the oven for a few min at low heat, then take them out, slip into your shoes and wear them around while they cool down).
[j4m5707] (score 5, diepte 0) I’m a dansko guy. Been rocking this pair of clogs with a Dr Scholl insole - went from having the worst foot pain to it being a breeze. The break in period is a BITCH tho.
[j4m5u4i] (score 5, diepte 0) I wear New Balance Shoes for Crews and my feet never hurt. I'm on my feet 50 hours a week.
[j4n1al3] (score 5, diepte 0) New balance came out w non slips
[j4lsvwy] (score 4, diepte 2) I know. Feels like concrete! I'll be checking back here to see if anybody has a better brand because I despite SFC too
[j4oe0pq] (score 4, diepte 2) Also docs make a non slip they’re listed as the 1460’s
[j4mi8zw] (score 4, diepte 1) Butcher here. I’m on year 3 with one pair of Blundies. Replace the insole every 6-8 months  and I’m good to go.  Starting to show their age with some cracking and split upper from sole but for the money, I’ll keep on using them.
[j4mc4l5] (score 4, diepte 0) I swear by sketchers at this point.
[j4m17ud] (score 3, diepte 1) Look for the Made in UK, the non UK are garbage
[j4lrz7g] (score 3, diepte 0) New Balance. My feet don’t hurt anymore and I am old.
[j4n6sdn] (score 3, diepte 2) If you’re not using inserts you’re doing it wrong.
[j4mf4h4] (score 3, diepte 1) Another vote for the Birkenstock Bostons, they take some breaking in but worth it!
[j4mlqug] (score 3, diepte 1) I’ve been wearing birkenstock birkis + super birkis interchangeably for around a decade. $80-90 on average and they last 12-16 months working 50-65 hours a week.
[j4lwbog] (score 3, diepte 0) You need to go to the store and get measured 

Also dr scholls  insole
[j4lxlue] (score 3, diepte 0) Merrel jungle moc pro 2 best shoes imo. Very slip resistant can just spray wipe off. But only down side low ventilation. But they last a long time and slip on. Very light also
[j4pbrvn] (score 3, diepte 2) Can't say for sure, but typically when half a crew of 20 jumps on a bandwagon of a brand and no one complains its a good sign. The way I see it, kitchen shoes kinda come down to quality of construction vs price. Shoes for crews work but they almost always need an insole and rarely make it past 18 months. Birks can go for 2-5 years depending on how well you take care of them, crocs are cheap but they go to shit after the 18 month mark IME. If snibbs aren't falling apart after a couple years, I'd bargain that they're worth the price. It's still kinda a new brand though, no one really knows how durable they are yet lol.
[j4m15es] (score 3, diepte 0) I use my new balance safety boots. Used them for a couple years doing construction and maintenance, no longer in that field so I had no other use for them besides to still be the “work shoes.” They’re definitely overkill, though the steel toes give me confidence in the case of a dropped monied or heavy object. 

The key point though is that these are the most comfortable and supportive pair of shoe I have ever owned. Do wonders for me feet
[j4m7m4b] (score 3, diepte 1) This.
I add Dr Scholls gel inserts. The whole set up lasts me a year.
[j4m4hqq] (score 3, diepte 0) I have had immense problems with plantar fasciitis in the past my feet also swell in the summer months so i always need a wide shoe.  I had to get custom insoles to heal , but I'm pain free now.  I have been wearing  Snibbs recently without any insoles and have been pain free and they work for a wide foot. Really depends on your budget and your feet.
[j4m87vb] (score 3, diepte 0) Gotta be birkis.
[j4m8jj2] (score 3, diepte 0) Birkenstocks
[j4mawnt] (score 3, diepte 0) Skechers have been working great for me the last few years. They’re some of the most comfortable shoes I own, and the slip resistance is solid. They come with good insoles, though I still prefer swapping those for some heavy duty Dr. Scholl’s to maximize comfort and support.
[j4mecjf] (score 3, diepte 0) Croc’s Bistro: super comfortable, but super ugly. By far the best non-slip I’ve ever worn!
[j4mks3v] (score 3, diepte 0) Croc bistro pros affordable and don’t fall apart.
[j4mwh92] (score 3, diepte 0) If you don’t mind mesh shoes(but with a liner under I believe) then I use the Sketchers non slips. They’re like $80 but I find them on sale on Amazon for $50 fairly often. They’re pretty comfortable and not too heavy, not as hot as the fake leather shoes, they aren’t stiff either especially when broken in. The tread usually lasts me about 6 months and only really wears down on the heel and ball where I pivot a lot on the line, if you have more even pressure then it would likely last a lot longer. I will say that mesh holds onto dirt and grease and stuff, flour is your enemy with these shoes haha. And the tread is very small, like hundreds of tiny rectangles, so food gets stuck in them but I just spray them out if I start to slip(cause when I’m busy I drop a lot of kale mix and cheese and stuff that gets stuck obv), otherwise they have great grip on water and grease and if you don’t walk on crumbs and food like me then you won’t have an issue with stuff getting stuck in the tread. The insoles don’t last super long but if you use a Dr scholl’s they last longer, plus I replace them every 8ish months so doesn’t really matter. Anyways, they also have a leather version but I believe the sole is a bit different but they were cheaper too. I recommend these shoes to my friends and they all like them as well, much more support than burks and just look like a nice running shoe. If you like them I need someone to clean off the walk-in racks, really hate pulling them outside to spray them off when it’s cold outside lol
[j4mxn7b] (score 3, diepte 0) Sketchers work shoes. I have the lace up sneaker pair and a pair of oxford slip ons. I buy them on sale at the local DSW mall shoe store when on sale for $40-50.
[j4ney2r] (score 3, diepte 0) Merrell jungle moc ac pro non slip. Most comfortable shoes I’ve worn in my 17 years of working on hard floors
[j4oyxum] (score 3, diepte 0) If you've got some bucks stashed I suggest Kuru's. It's a big investment but they last and are far less expensive (and less painful) than having to fix the problems that are guaranteed to arise after an hot minute of 12-16 hour days
[j4t75nt] (score 3, diepte 0) RED WINGS.  They make construction & hunting boots.  They have a pair of clogs that will last you 2.5yrs under the toughest conditions.
[j4pktgl] (score 2, diepte 2) Whatever pair you buy next, still put in an insole the moment you've got the shoes and change them every couple months.

It's a life saver.
[j4ny35q] (score 2, diepte 2) H&bs are trash my friend a coworker had them and they’re like walking on boards no support at all and didn’t last long at all. I can’t say I’ve been impressed with anything H&B tbh. Docs take a long time to break in and get a very good insole love mine had them for years. Maybe vans work if you’re skinny I’m a big boy and god damn did they make my whole body scream in pain lol however I do the exos for street wear they’re actually comfy if you’re looking for new kicks
[j4pugsp] (score 2, diepte 1) Damn I used to always rock Docs in the kitchen and they lasted forever and we're non slip.

You do have to break them in though. I've heard nowadays you have to be sure to buy the ones made in UK.
[j4qh0o9] (score 2, diepte 2) It’s possible I went down a rabbit hole the other day about levis jeans and it was basically what you’re saying that at this point you need to research heavy which country they come from to ensure quality. So if you’re buying Levi’s stay away from ones made in Pakistan they’re normally cheaper quality and sized wrong vs Vietnam’s
[j4lu7gi] (score 2, diepte 1 OP) Everybody at work wears clogs, but everyone shrugs when I ask about arch support
[j4mj1gk] (score 2, diepte 1) I’ve always used the waterproof thermal blundstones and I love them.  I do have to buy a new pair about once a year though
[jrbmsa2] (score 2, diepte 2) Where do I get them resoled? My non slip tread is non existent now lol
[j4mg0hk] (score 2, diepte 1) Came here to say this. I go through a pair of shoes every 3 or 4 months so I don’t like spending a bunch of money on them. Decided to give the Walmart non slips a shot and I’ve been pretty happy with them. They look decent, are comfortable, and are fairly priced.
[j4ptm4r] (score 2, diepte 1) I have tried many of Skechers non slips. Easily been my favorite nonslip shoe for several years now. Most other shoes would start falling apart in 3 months, I get 6 months to a year out of Skechers
[jw7sqx4] (score 2, diepte 2) Fucking hate snibbs. Whoever fucking suggest this probably works for their marketing team. They look decent but they are cheap as fuck. I bought a pair and in 3 month the non slip sole is non existent. Never buying them again.
[j4m2k7k] (score 2, diepte 0) Do people have problems with the non slip vans? Been my work shoe for years and never had any issues personally.
[j4mfojn] (score 2, diepte 1) Yeah same here, they were my go to when I worked as a fish monger in super wet environments with tile floors. I have to wear something nicer when I do certain work in front of customers but they are still my daily drivers.

It makes me wonder if people are actually trying the Made for Makers line or not
[j4mlxv7] (score 2, diepte 1) I bought a pair and they had no support. Went right back to birkis after one shift
[j4nzwdt] (score 2, diepte 1) I’m an inspector and I swear by them! I’ve never run into a problem in any kitchen!
[j4ntpzq] (score 2, diepte 1) I always try to break in my new pair when my old pair still has a little life left and switch them out mid shift, I did one 14 hr day in a brand new pair of clogs and it was excruciating. The bragard clogs are amazing too but they want like $80 to ship to Me so fuck that.
[jw7tacp] (score 2, diepte 1) Fucking clogs make me feel like I’m wearing wooden shoes from the Dutch. I can’t see how you get comfort in wearing shoes made of wood. Fuck over priced clogs.
[jw850gk] (score 2, diepte 2) I never said I was comfortable in them, just that they provide actual support and durability. Vans/crocs/running shoes etc. may FEEL comfier, but the foot pain while wearing them long term is absolutely atrocious because those shoes are not meant for standing on concrete for 11 hours
[j4m5c39] (score 2, diepte 0) Picked up clogs on amazon for like $30 about a year and a half in and theyre just now breaking down, honestly tho if i just got insoles they would be fine.

I dont like laces or any of that frill shit, i want to be able to slide in and out and have a strong enough material so i dont get any holes
[j4m8isq] (score 2, diepte 1) I liked the pair I had, but they fell apart in less than a year. Same border splitting and worn tread that I would get from my regular vans.
[j4m8cbw] (score 2, diepte 0) I've got a pair of shoes called kivini 

Non slip steel toe, I feel like a fucking mountain goat in these those.

First pair lasted me a good couple of years before I beat them to shit and had to but a new pair.
[j4m8p5z] (score 2, diepte 0) I have kuru Kinetic sneakers (they're the anti-slip ones for restaurants). anti-slip, shock absorbing, good insoles. specifically made to help with foot pain. they take a few days to break in but then they sort of mold to your foot shape and are super comfy. easy to wipe clean, but i've replaced the shoelaces because they got gross. i've had them for 2 years and only now am looking to get a replacement pair.
[j4mc0dk] (score 2, diepte 0) Check out mise.

I think they used to work for vans kitchen shoes and broke off and started there own company.
[j4mcqs8] (score 2, diepte 0) If you don't mind heavy, I wear Ace steel toed workboots every day for the past year and they show no sign of wearing down. Theyre super water proof which is big for me because I work with tons of boiling liquids that I spill on my shoes pretty often. My feet have never been dryer, or safer from pesky falling drawers.

Edit: and my girlfriend wears the bistro Crocs. Ive never heard her complain. Just be mindful that the bistros run slightly smaller than the regular croc sizes.
[j4mdk8b] (score 2, diepte 0) I love my danskos but that only works if you have small feet, because I believe they’re designed for women.
[j4meu03] (score 2, diepte 0) Dansko walker.
[j4mjbda] (score 2, diepte 0) Blundstones, steel toe.
[j4mmju4] (score 2, diepte 0) Sika super clogs

Everything is trash in comparison
[j4mn20j] (score 2, diepte 0) I second the idea of a podiatrist. SFC destroyed my feet. I wore them for 12+ years as I was naïve enough to think they were the best despite constant foot and back pain. 
I just had xrays and MRI of my feet which showed a bunch of crap caused by those bad shoes. I meet with my podiatrist again tomorrow to discuss surgery. 

I switched to Sketchers about a year or so ago and they did seem to help, but the damage was already done. 

Before I saw a podiatrist, my primary recommended going to a specialty store for running shoes as she said most of them will make you custom inserts for a fraction of the cost.
[j4mopmw] (score 2, diepte 0) Keens. I recently switched to boots, because my ankles were getting sore
[j4mwrvi] (score 2, diepte 0) I switched to Danskos about 10 years ago and can't imagine I'd ever wear anything else. Worth the premium.
[j4my16r] (score 2, diepte 0) Birkenstock bostons, break in takes a while but they’re super comfortable and look good (depending on how high end your place is). They carry a little bit of a higher cheque but the investment in having good, firm arch support is worth it. Keeps gourmand are a good option if you like the comfort of vans sneakers with non-slip qualities.
[j4mygtr] (score 2, diepte 0) [TRACTION SPRAY](https://www.homedepot.com/p/Shoe-Grip-Shoe-Adhesive-BGSG-1/202327832)

Also, hairspray will work in a pinch.
[j4n0srt] (score 2, diepte 0) Sanita shoes - they are the old Dansko’s before Dansko moved to China.
[j4n1e4g] (score 2, diepte 0) Birkenstock clogs all the way.
(51 reacties met lagere score weggelaten)

