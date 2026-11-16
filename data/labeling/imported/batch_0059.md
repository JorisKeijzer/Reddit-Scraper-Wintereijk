# Label-batch batch_0059

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
Schrijf het resultaat naar `batch_0059.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 16y7clz, psq5gl, 1r1u4xt).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 16y7clz ===
SUBREDDIT: r/Chefit
DATUM: 2023-10-02  SCORE: 40  REACTIES: 103
TITEL: Aspiring Chef Question: Foot pain.
POST (source_id=post):
So, young man here, always liked cooking food and I would love to be a chef.  
I love working in the kitchen and preparing food.  
And I am taking classes to become a professional chef.

However, For some reason (most likely due to being heavy set) whenever I stand for like 1-2 hours, my feet starts hurting like crazy.  
My "classmates" don't seem affected to the same degree, and I find that it genuinely disturbs my ability to learn / perform.

Anyone have any tips or suggestions? Have anyone experienced the same?  
I find it frustrating and I have as of yet not found any solution for it.  
(Really hard to work efficiently when I have to bounce from one foot to the other to reduce the pain)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k370mei] (score 66, diepte 0) I was 265 with bad foot pain when I started my life inside the kitchen. After 12 months I was 200. That’s the only solution. 

Smaller people have bad feet too but weight really effects the paws.
[k36w3tq] (score 38, diepte 0) Quality shoes and insoles. 

Talk to a podiatrist if it is really bothersome, as they’ll have the best insights as to how to alleviate that.

I also find that staying moving, rather than standing still prevents some of this pain.

Ultimately, and I mean no disrespect here, if you think your weight could be playing a factor you could come up with a solution to remedy that. 

Whether it’s a lifestyle change, or a medical discussion (I don’t know your scenario) that could be your best long term solution if that’s the root of the issue.
[k36wj18] (score 23, diepte 2) Footwear has a huge impact on the pain your feeling, especially if you’re heavyset. A standard running show is not meant to support you the same way a work boot or kitchen shoe are. Having worked construction and been a chef, spend money on some good shoes and they will pay you back. 

You can get away with running shoes for a little bit, but I personally blow through those in about 3-4 months of long days (8-14 hours) in the kitchen. Dansko, mozo, shoes for crews, and even sketchers and doc martens are good kitchen brands.

I’ve gotten older and like a light duty work boot for the added ankle support, but that is my personal preference.
[k3781pt] (score 20, diepte 0) Shoes for Crews + Gel Insoles + Kitchen Mats.

Ibuprofen if it gets bad.
[k38chko] (score 17, diepte 2) What
[k374em8] (score 15, diepte 2) Lol you are getting down voted for this because footwear is EXTREMELY important in this industry.  I go through a pair of expensive shoes anywhere from 6 months to a year.  Get the best thing you can between you and the ground.
[k36wiog] (score 13, diepte 0) You're going to want a better shoe, I prefer kitchen clogs (basically a version of crocks without the holes) personally because they're easy to get on and off (they look ugly as fuck, but Idgaf anymore). You're going to be spending long periods of time on your feet, so the combination of bad footwear and being overweight leads to foot pain (among other things).
[k36yrzl] (score 12, diepte 2) Oh sweet summer child….
[k36vgoy] (score 10, diepte 0) Yes, being overweight can significantly exacerbate foot pain. That will be the number one reason for the severity, though part of it is also just acclimating to standing for long periods if that’s something you’ve never done before. Having comfortable footwear is also obviously important. More rigid insoles provide better support and are generally better for standing, and it might be worthwhile to see a podiatrist and be fitted for orthotics. You could also look into compression socks. But the simplest and most direct answer would be to lose excess weight.
[k36wdg9] (score 9, diepte 0) How fit are you? Working in a kitchen is pretty physical and those muscles take some time to develop. It also helps to work out and to stretch so you can build up your body
[k37ei51] (score 8, diepte 2) Someone gave you the good advice of getting a good pair of shoes and you said that you were sure that your shoes were not the problem. I'm not being a dick, I'm being brutally honest.
[k39zjl5] (score 7, diepte 1) Legit. I was 300, that's when my foot pain started. After being on the line for a year, I was 250. That and the cuts, burns, and calluses on my hands began to be my pain focus so maybe I just didn't notice my foot pain as much because of that too hahahahah....

Then I got a deskjob....then I got back to close to 300....then I went back full time in kitchen. The foot pain has returned....
[k36v388] (score 6, diepte 0) What shoes do you wear?
[k36vudl] (score 6, diepte 2) Think they were asking if you were wearing running shoes, skate shoes (flat bottomed) or another kind. Pick up a pair of kitchen shoes, they're usually in the style of clogs and are better for your feet when standing for a long time.
[k37c86x] (score 6, diepte 3) Shit, fuck this industry, footwear is extremely important to foot comfort in general. 

That said I’m a hefty motherfucker and I default to crocs that have always kept my feet feeling fine on a 10+ hour shift.
[k37m0bc] (score 6, diepte 1) Love crocs for the kitchen but can't stand how much shit from the kitchen floor sticks to them during a busy service when sweeping is not an option.
[k3787yl] (score 6, diepte 0) Anti fatigue mats, proper footwear with good arch support, stretching/ yoga. If all that fails go and see a podiatrist and get orthotics.
I’ve been a chef for 20+ years and am now currently dealing with plantar fasciitis
[k375foz] (score 5, diepte 2) Footwear is a big deal in the kitchen, you need to be able to stand for 12 hours, no joke. It hurts everyone, but extra weight and bad shoes will make it reallly difficult
[k37p3e5] (score 5, diepte 2) Bruh I am 280 and if you don’t start forming strong opinions about shoes you are in for a lot of pain in your future. There are no “normal” shoes…. 
Only shoes that help and shoes that hurt. 
Your arches are collapsing because like me u are LARGE. You need a support shoe with some strong insoles like “superfeet”  or the clogs that were mentioned elsewhere. Wait till you’re older it will be worse.
[k36x2gh] (score 5, diepte 2) Do you exercise or workout, can you run? The strength of your legs and core is what’s being put to the test in the kitchen. 

It might be you need to work on building up your legs. Your shoes are also really important when being on your feet all day
[k36xvj8] (score 5, diepte 4) I’m sure you’re very strong, but just having upper body isn’t going to help you that much, that’s just more weight on your legs. Plus other than lifting pots and pans, there isn’t a lot of vigorous strength work in the kitchen. You’re going to be on your feet everyday, you’re going to be crouching to get in fridges and shelves every day.
[k37dxaj] (score 5, diepte 1 OP) No need to be a dick
[k3748ej] (score 3, diepte 2) I am quite certain that quality footwear is the only thing keeping me from constant body aches. I can get by with cheap shoes, but they MUST be non-slip, and I absolutely have to keep fresh insoles in my shoes. $20 bucks every 3 months.
[k36vkds] (score 3, diepte 0) Invest in a good pair of non slip shoes

I wear Dansko clogs

Also go see a podiatrist, a pair of orthotics might help depending on what your issue is.
[k37op4y] (score 3, diepte 5) Yeah, depending on what your day actually looks like, those speed-squats will wear you down in a hurry, too.
[k390olw] (score 3, diepte 4) Working in a kitchen usually means being on your feet for close to 8 hours a day, if not more. You never stop moving, and you dont have time to sit. Think long and hard on that before you fully comit to this industry.
[k37q3as] (score 3, diepte 2) I use a "croc" style shoe, it's smooth on the top, waterproof, oil proof (learned that when changing the oil in a fryer) and steel toed (thank holy christ since some people are absolute idiots when it comes to attempted pranks/bravado when someone has a fucking knife in their hand). I've never had an issue with stuff getting stuck to them, but if it were the case, in theory you could just toss them in the washing machine on a low temp.
[k3746ne] (score 3, diepte 0) I did a regiment of Advil and Witch Hazel every night when I got home. Chef shoes of course (will cost you.) Line have decent mats?
[k37532r] (score 3, diepte 0) Get orthodics. It will change your life.
[k377j0s] (score 3, diepte 0) I’m 6’2 270lbs, buy either work crocs or if you want to spend some money some work birks. Trust me.
[k379y5r] (score 3, diepte 0) Your feet hurt and you aren't even looking at the shoes you're wearing? Can you do 2+2? Logic and common sense go a really long way, and preferably you'll have those skills by the time you're running a kitchen as the chef, lol.
[k37ec67] (score 3, diepte 0) As others have said it's probably your shoes, try going to a shoe store and getting actually fitted for shoes (your feet might be wider than you think). Whatever the solution is you need to figure this out NOW. People will talk about how important it is to wear shoes that fit and they're 100% right and it's not just a comfort thing. I wore slightly uncomfortable shoes to work for less than a year and developed tarsal tunnel syndrome (think carpal tunnel but in your ankle) as a result. I'm in my early 20s and I can't walk more than 30 minutes at a time without incredible, lasting pain and it's likely I will never be able to because a lot of foot problems can be managed but not fixed.
[k38i6k4] (score 3, diepte 0) Posture is usually really poor in the kitchen. Working over a counter causes you to usually bow over the counter to work resulting in lower back pain, sciatica, and foot problems. Focus on keeping you pelvis forward and knees with a with a rotational bias outwards. So instead of hips collapsing keep them open which should cause your knees to slightly push outward(don’t focus on pushing them outward the idea is if you keep your hips open it will naturally happen) by doing this you shouldn’t be collapsing your arches as much. Look on YouTube  how to ground your feet on the ground with proper floor contact. Shoes and arch support help for sure but if you can mechanically teach your body to strengthen the muscles to support yourself better you will benefit as well. 

Not a doctor or medical professional but my partner of 20 years is a physical therapist and I’ve suffered from a lot of postural issues working the kitchen
[k37svsu] (score 2, diepte 2) dog i hate to tell you but it’s true. over a decade on the line makes you approach you’re feet, back, ass, neck, all different got damn. listen to the folks here
[k386o57] (score 2, diepte 4) CDSNXORE Chef Shoes on Amazon. [https://www.amazon.ca/Women-Kitchen-Shoes-Safety-X-Wide/dp/B09ND8JTLX/ref=sr\_1\_7?hvadid=666108745877&hvdev=c&hvlocphy=9000918&hvnetw=g&hvqmt=e&hvrand=1328292715134593920&hvtargid=kwd-339208939906&hydadcr=26053\_13645135&keywords=steel+toe+chef+shoes&qid=1696297482&sr=8-7](https://www.amazon.ca/Women-Kitchen-Shoes-Safety-X-Wide/dp/B09ND8JTLX/ref=sr_1_7?hvadid=666108745877&hvdev=c&hvlocphy=9000918&hvnetw=g&hvqmt=e&hvrand=1328292715134593920&hvtargid=kwd-339208939906&hydadcr=26053_13645135&keywords=steel+toe+chef+shoes&qid=1696297482&sr=8-7)
[k36xdqd] (score 2, diepte 0) Better shoes or at least some decent in soles. New Balance has a decent non slip kitchen shoe . For about 100$ also maybe look in to compression stockings to help keep your circulation up .
[k3ftkre] (score 2, diepte 4) Names bonds having a stronk.
[k38j4pz] (score 2, diepte 1) Same here. Got plantar fasciitis about 1.5 years ago, still haven’t properly healed. Have heel spurs now and I walk with a limp. I found that wearing barefoot shoes helps me the most, instead of insoles. Xero makes a good non-slip kitchen shoe for that purpose.
[k393sez] (score 2, diepte 1) Came here to talk about plantar fasciitis too.
Physiotherapy helps
Building strength on your feet
Wearing comfortable shoes
Ibuprofen on harder days
[k3b80n9] (score 2, diepte 1) Crazy, I've been in the industry for about 24 years and just started suffering from Plantar Fasciitis about 2 months ago - stretch before lifting weights has helped tremendously! I also opted for a pricy pair of Hoka Bondi Non-Slips (amazing footwear with a price to match lol) to add to my footwear rotation!

Both have made it wildly bearable - some days I'll have no pain at all!
[k3b8q99] (score 2, diepte 2) I’ll have to check out the hoka bondi shoes
[k391c7w] (score 2, diepte 2) For real tho bro I'm reading through these comments ans you don't have realistic expectations yet. Working most jobs requires standing many hours and it's something you will have to work on. Working in a successful restarunt usually means busting your fucking ass like there is no tomorrow. Let me tell you, anything less than the best places to work, generally suck in this industry. At least in my experience. It's either fine or suck, mostly sucks.
[k37d2tq] (score 2, diepte 0) Go see a podiatrist and get yourself fitted for proper orthotics.
[k37mbcd] (score 2, diepte 0) Talk to a podiatrist. 

I actually broke my foot at work soon after finding out I was diabetic. 

Lo and behold you can find out you have a terrible foot condition called Charcot foot.  

(Only vaguely related to Charcot Marie tooth nerve disease) 

I wouldn’t google it unless you can handle pretty bad foot issues. 

My break hasn’t healed. It’s been 10 years.  I broke a metatarsal. I’ve had two surgeries so far and I’m walking and stuff without a device if I’m just running errands. I’ll need another surgery probably in the next ten years to reset my metal bits and realign my ankle as it’s collapsing. 

So, get healthy/lose weight. Go see a podiatrist. (Dr. Scholls isn’t one I’d recommend). If there is a diabetic doctor near you. Ask them about a podiatrist. 

Yeah I was a chef for 30 years. This injury ended my career and I’m on disability now. There are times the nerve pain is so intense it felt like I had barbed wire rubbing my nerves. 

Take care of your body and especially your feet.
[k387tvv] (score 2, diepte 0) Shoes, insoles, socks, water, potassium, stretching, inversions, mats, sildes at home and rest. 20 years in, knees, calves and feet are crushed around the 30th hour and debilitating 60+ hours these days.
[k38etuh] (score 2, diepte 0) Lose weight, not being mean just try it it'll work. I myself am heavy set but have started working on myself since this what I want to do. As chefs we only have our bodies we must take care of them. It'll suck but you must lose weight. ALSO GET A GOOD PAIR OF SHOES
[k38ey2a] (score 2, diepte 0) It could be plantar fasciitis - there are stretching exercises that help me with it. Of course, good shoes/orthotics/etc. are also part of the equation in dealing with it.
[k38i12v] (score 2, diepte 0) As a bigger dude with 26 years in the industry: Loose weight. Like, no fucking around. If you want to be able to deal with and learn to get over foot pain, loose a healthy amount of weight. Do it now so in 15 years your whole skeleton isn't so fucked that trying to regain your health is like an 80 year old trying to train for a triathlon. Loose weight and be very concience about your health and what your body tells you. 10+ years of standing on concrete and bending over will fuck you up; Doubly so for we, the overweight.
[k38n3wu] (score 2, diepte 0) It will get better with time, the pain is your muscles being overworked and they will get stronger, that being said if it is consistently the same areas then that indicates an imbalance in your posture, certain muscles are weak/ inflexible so you compensate by standing in a way that works down other muscles.
Kneesovertoes is a good starting point for flexibility but I'll do A quick rundown of lower body.

Hamstring - half front split stretch, forward fold (toe touch), Jefferson curl. Both the last two are more effective on a slant board.
Calves - I use slant board to stretch, can just do wall stretch make sure you do both straight leg and bent knee, they work separate parts. 
Quads - sit on knees ( lift knees to make harder). Couch stretch (push backwards)
Hip flexors - couch stretch (push forward), pigeon pose, front split.
Groin/adductors - butterfly stretch, frog pose, pancake stretch
external hip rotation - 90/90 (front leg), pigeon pose, that one where you put your ankle on your knee at a right angle and push down,
Internal hip rotation - 90-90 (back leg), reverse nordic curl stretch (can do each leg individually too).

Big compound movements are sitting in a deep squat flat footed and the middle split.
[k393l19] (score 2, diepte 1 OP) Mostly in the bridge and heel. Mostly in the muscles I think.
[k3aimho] (score 2, diepte 0) Better shoes is key, but what I haven’t read here is that you should get two pairs and rotate between them. 

Good luck brother.
[k3d2w5e] (score 2, diepte 0) Get really good shoes, this is key.  BUT you have to lose some of the weight.  If you’re hurting after 2 hours what’s 7 look like?  10?  Etc.   Start acclimating yourself by spending more time on your feet.  Walk more, if you play video games play video games standing, you just need to make yourself more used to it.
[k3eur8a] (score 2, diepte 0) Yoga with Adriene has different yoga videos for chefs, service industry and feet. Check them out! 10 minutes of daily feet up the wall also helps with the swelling that comes with hours on your feet daily. It also just takes time to build stamina. You’ll get there!
[k37gjce] (score 1, diepte 3) And save your toes! I deal with foot pain constantly; I refuse to heal a THIRD broken toe. I wear croc clones, but get kitchen clogs. They will keep hot liquids and granular/slimy/oily things out.
[k37g5d3] (score 1, diepte 3) I mean... I know what you mean on the good footwear. I always get a good pair of steel toes for the winter (I have to cook chicken outside in WNY. It's rough some days). But if I'm inside, I have a pair of Adidas slip-on workout shoes. I've had them for about a year now. Throw them in the washing machine every 2 months. Bingo, bongo.
[k390yf1] (score 1, diepte 2) Just curious. If you weren't looking for suggestions pertaining to footwear, what sort of suggestions were you looking for or expecting?
[k39170o] (score 1, diepte 4) Fair enough.
[k39tckw] (score 1, diepte 2) Be careful with Dansko shoes unless you have a great arch. If you are flat-footed, they really hurt after a while. Had to give them up.
[k36woqd] (score 1, diepte 1 OP) I would say that my fitness isn't actually that bad...  
I don't have the absolute best stamina, but I have no problem with working with my hands and arms for hours with the right pacing of course.

My legs and feet aren't too bad with movement, but... standing still has never been a strength.
[k3869ql] (score 1, diepte 3) What are they? Brand? Link?
[kua72w0] (score 1, diepte 1) im 245 atm. goal is 180. 2 weeks cook job, my feet are cryin.
[k37se03] (score 1, diepte 1) op this is the way. wear whatever you want to work. once you’re there you need shoes made for a kitchen and for your foot. if you ain’t got oh well but get them “what the fuck are those” in all black for work. put them soles in.
[k3d1ytu] (score 1, diepte 3) somebody get this person a bondulance
[k3b9g9a] (score 1, diepte 3) Totally worth the 180 price tag. I thought they looked a little "bulky" at first, but when you wear them, they actually look great and flow nicely with kitchen attire.

Never wore a better shoe for the kitchen when considering comfort. This is one of the few "pleasures" we've earned ourselves for a lifetime of dedication, lol  Grab em!
(44 reacties met lagere score weggelaten)

=== THREAD psq5gl ===
SUBREDDIT: r/bartenders
DATUM: 2021-09-21  SCORE: 21  REACTIES: 102
TITEL: Best shoes for tending bar?
POST (source_id=post):
I know this question has been asked a million times, but I'm trying to figure out the best shoes for me.

The place I work is super chill, so looks don't matter much at all. I don't need any sort of safety toe. Water resistant would be handy, but not entirely necessary, so if you have a great pair that aren't water resistant let me know anyways. Same with non-slip, potentially useful, but not necessary at all.

Basically I just want a pair that will keep my feet and knees from hurting by the end of my shift. I've been wearing my Stan Smiths for the last month at work and it hasn't been awesome, I really feel it when I get home.

Ideally something with little to no arch support. I have super flat feet, so shoes with high arches aren't comfortable. I'd also prefer as close to zero heel-toe drop as possible.

Basically I just want something with enough cushion and support to keep my feet and knees happy during and after a shift.

I was looking into the Van's Ultrarange line, does anyone have any experience with those?

I've also considered Nike Air Max, since they're supposed to be super comfy.

Thanks!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hdrifq6] (score 29, diepte 0) Greased Docs with inserts for the last 8 years. Only gone through two pairs in that time.

Doesn't hurt that they are a timeless shoe and look good.
[hdrbilz] (score 12, diepte 0) Any slip resistant shoe that is comfortable for you. I tried three, before I settled on a shoe for my high arch.
[hdrcia5] (score 11, diepte 0) The classic vans never went wrong for me. Then again I have very flat feet.
[hdriwq7] (score 8, diepte 0) Dansko non-slip
[hdrxfph] (score 7, diepte 0) Sketchers with compression socks.
[hds02we] (score 6, diepte 4) Get the Vans Made for Makers series. They are anti slip, cloud insoled, durable and waterproof.
[hdrwcgs] (score 6, diepte 1) This is the most correct answer. Great support, durability and material. Just make sure you buy their non-slip version.
[hdrbtmo] (score 5, diepte 0) I have boots by Danner that have lasted 3 years at this point bartending 50 hrs per week. They were expensive but 100% worth it. I have been in the industry for over 12 years and these are the only footwear I've found that stay comfortable and don't fall apart after 6 months. The slip resistance isn't that great, but they are waterproof with is a huge upside for me. Idk if I'm allowed to post links but the ones I bought are "Danner Women's Prowess Side-Zip Military and Tactical Boot"
[hdryvoq] (score 5, diepte 1) Seconded. Danskos for the win
[hdrhuy5] (score 4, diepte 2) In that case get the Vans Authentic. I always get the black on black ones.
[hdrn1ew] (score 4, diepte 0) I'd take lightweight over "support." Lugging heavy shoes around all day is exhausting.

My favorites are Saucony Bullet. About $45 and slip resistant (though not advertised as such).

Sadly they've been discontinued, so once I can't get them anymore I'll probably switch to the similar, but more expensive, Onitsuka Tigers.
[hdrclnn] (score 3, diepte 1 OP) I also have very flat feet
[hdri4oi] (score 3, diepte 3 OP) If I get Vans I'll probably get something from their cush line for the extra support
[hdrwg11] (score 3, diepte 4) Nah man, buy their non-slip. As a bartender you always want non-slip. Ideally also like waterproof.
[hds0in6] (score 3, diepte 3 OP) I've tried my Converse, but my knees and feet still hurt after a shift
[hdrdhir] (score 3, diepte 0) I have these black nonslip newbalence and they’re great especially for the really long shifts
[hdrlzcs] (score 3, diepte 2) [here ya go](https://www.shoesforcrews.com/product/22002-new-balance-arishi-v3)
[hdriv5l] (score 3, diepte 0) I really like Vans Ultrarange. They're light, comfy and breathable. My partner prefers a flat shoe as well and he has several pairs.
[hdrjg3d] (score 3, diepte 0) Birkenstocks clogs have done me solid for 6 years now. Cost around $200 for them, but they have held up better than any other shoe I have worn. I'm 12 years behind a bar now and 19 years in restaurants. Clogs have always done the best.
[hdrn7p2] (score 3, diepte 0) I am in love with my nautica slip ons. Stylish, easy to clean, lightweight, and GREAT support.
[hds7war] (score 3, diepte 1) Literally what I was coming here to say. But it's gotta be the ugly sketchers, not the cute ones that look loke regular sneakers.
[hdsa1b7] (score 3, diepte 2) Nah dude I have a sketchers warehouse down the street and shit you not, you can get any kind of shoe there and they're comfy as hell. I have had 3 different types of kitchen shoe, steel toe boots, waterproof hiking shoes, tons of sandals, and my bartending shoes. They're not like super cute but they're black, liquid resistant, slip proof, memory foam, and they are the type of shoe you can dress up or down.
[hdrjy6a] (score 2, diepte 4) Iv tried these and ended up liking the regular ones better. Maybe my foots just weird tho
[hdrlo20] (score 2, diepte 4) I got the comfy cush ones (old skool) and they’re such an upgrade from the non cush ones for my feet at least.
[hdrrdav] (score 2, diepte 7 OP) I've wanted some Docs for a while anyway, maybe I should just go for it
[hdryusr] (score 2, diepte 6) Vans is kind of shit for bartender. Anything fabric, really. But comfort and non-slip aren’t mutually exclusive; so don’t skip on getting non-slips my man. You never need it until you do, and that day you’ll remember why they matter.
[hdsv27k] (score 2, diepte 4) https://www.vans.com/shop/vegan-old-skool-black-black?utm_id=go_cmp-191532173_adg-26624222573_ad-95842386413_aud-473635133229:pla-866008078493_dev-m_ext-_prd-700053843554_mca-8181713_sig-CjwKCAjwhaaKBhBcEiwA8acsHCM4GmR2VxE7spriH2yKmQXaHFveuAM4BzLEhr8UL4XoPdtNaenv2RoC6wkQAvD_BwE&utm_source=google&radscid=191532173&gclid=CjwKCAjwhaaKBhBcEiwA8acsHCM4GmR2VxE7spriH2yKmQXaHFveuAM4BzLEhr8UL4XoPdtNaenv2RoC6wkQAvD_BwE my go to
[hdrcmvx] (score 2, diepte 0) I take anything with good ankle support and add quality ortho insoles. 

Currently using allbirds. Looking at getting a pair of on cloud for water proofing.

But I get 1 pair a year for work. I don’t mind spending any amount of money, I’d rather save my knees and back. My route is expensive.
[hdrctbj] (score 2, diepte 1 OP) I've looked at allbirds and oncloud, so maybe I'm on the right track already. I might just need to get whatever shoes I want and add some insoles.
[hdy0h9q] (score 2, diepte 1) I second this! Shoes for Crews NB are the way to go
Just make sure you don’t leak anything into the mesh lol
[hdrfc6k] (score 2, diepte 0) I would wear either pretty much adidas ultra boost for the comfort or a hiking shoe like from keen with better insoles
[hdrg81l] (score 2, diepte 1 OP) Does the boost hold up and stay comfortable over 6-8 hours?
[hdrfiz4] (score 2, diepte 0) Snibbs have saved my life. Have plantar fasciitis. They’ve been the best I’ve worn by a mile
[hdsmwnk] (score 2, diepte 1) I have a pair of snibbs that I got back in June. Can’t say anything as to their longevity yet, but I can confirm that my feet no longer hurt after work (nor the next morning). They’re still pretty much the same as they were when I got them, in terms of seams and sole, etc.

They’re pricey, but honestly if they last even one measly year I would still recommend them for how much better my feet feel. The non-slip isn’t quite as good as my shoes for crews were, but still much, much better than regular shoes.
[hdrg3bx] (score 2, diepte 0) Timbs
[hdrnmpq] (score 2, diepte 1 OP) Oh I agree. I was thinking something with lightweight cushion, something like New Balance's Fresh Foam or Adidas's Ultraboost.
[hdrnl46] (score 2, diepte 2) I believe they’re the casual slip on fashion sneakers!
[hdroa7f] (score 2, diepte 0) Honestly, bracing for the blowback… my Iron Rangers….. my slip on Docs are great, but the Redwings are honestly the most comfortable thing I’ve put on my feet.
[hdrsdcr] (score 2, diepte 3 OP) I've heard the break-in process is rough, but if they're really worth it I might do it
[hdron3q] (score 2, diepte 0) I only wear Nike Running shoes. Not cross trainers etc. Running shoes, doesn't have to be Air Max, but they are nice. Nike Zoom is cheaper.
[hdrowz6] (score 2, diepte 0) I just got a pairs of vans made for the makers and I love them. They are just so comfy and so nonslip.
Something unrelated that helps my knees and back a lot is compression socks from nurse mates.
[hdrulja] (score 2, diepte 0) I use the Birckenstock Boston slip on shoes. They’re great and will last forever. 

Hoka One One also have some pretty good non slip work shoes, though they are a bit pricey.
[hdrv49n] (score 2, diepte 2) They worked very well for me. The customer service is also really good.
[hdrxf4k] (score 2, diepte 0) I try to switch foot gear every other shift.  Boots one day, sneakers the next.  Gotta say I the boots because ng water proof is a big plus
[hds2ng8] (score 2, diepte 0) I picked up some of [these](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjU1feamZHzAhXuDa0GHRbkA7YYABAFGgJwdg&ae=2&ohost=www.google.ca&cid=CAESQOD2_nnhi-WJXc6rrpKBxBQB3g5WLcx40U5RsDBZDm6y_QxSbygdg45oihu_slHjT-oKzvEPhSrfCRXeO6gjdGg&sig=AOD64_1Q8JauWzpwBSN5t7uN0luZQgC28g&ctype=5&q=&ved=2ahUKEwiBhfCamZHzAhWGKDQIHSmdDPYQwg96BAgBECE&adurl=) because I was starting to get shin splints from the long hours. Super comfortable and non-slip.
[hds3fyg] (score 2, diepte 0) I bought [these](https://www.rackroomshoes.com/p/chuck-taylor-all-star-lugged-high-top-sneaker/431140?utm_source=google&utm_medium=shopping&utm_campaign=20210714_BTS_DigitalCoupon&gclid=CjwKCAjwhaaKBhBcEiwA8acsHDYLC7w6ZWXRh-8joet4RZxs0vWg1zrmD7xVERdNSfh7tYiFGUBZZBoC_8sQAvD_BwE) with no intention of them becoming my work shoes and I love them. Waterproof comfortable and good ankle support.
[hds4o8n] (score 2, diepte 0) I wear high top vans but not the classics. The newer designs still keep the old school look but the insole has been vastly improved. And I will die on this hill, get sole inserts for the love of god. I used to wear classic high top black and white chucks with inserts and my coworkers would dog me but with the gel inserts they felt like I was walking on clouds. Only reason I switched to vans is because they last much longer.
[hds8yy0] (score 2, diepte 1 OP) Doesn't seem super sustainable, but in a dire situation that would work 😂
[hdsa56p] (score 2, diepte 0) Brand new classic crocs. Been wearing them for 10 years. Get compliments all the time.
[hdsaun8] (score 2, diepte 0) I'll be the odd one and say I don't value slip resistant.   I find that after a few shifts my normal shoes are slip resistant as much as any other pair.   It's about knowing how to walk
[hdsbjkq] (score 2, diepte 0) Timberlands
[hdse0gz] (score 2, diepte 0) If you’re willing to suffer through the first two weeks of breaking them in, danskos 2.0xp are amazing!!! My legs don’t even hurt after a 12 hour day!!
[hdsjv49] (score 2, diepte 0) Nonslip new balances the best shoes I've ever owned for the restaurant by a long shot
[hdsnac7] (score 2, diepte 0) I put some more info in a response to someone else in this thread, but my snibbs have my feet feeling divine compared to almost every other pair of shoes I’ve ever used for work. The only other pair that came close was a pair of Ecco dress shoes that I found unused in a trashcan (don’t judge me). Used them for at least a few years. They were about as comfortable as my snibbs are, if memory serves me, but looked absurd outside of fine dining.
[hdsrahj] (score 2, diepte 0) I've been wearing a pair of non slip sketchers a d they're pretty comfortable
[hdswypy] (score 2, diepte 0) Hoka One One sneakers, buy a season or two back from sites like 6PM or Zappos. I've gone through probably 3 pairs of them and I love them so much.
[hdt127h] (score 2, diepte 0) I like Merrill’s triple black non slip. Awesome.
[jk2nr32] (score 1, diepte 1) i’m visiting this thread a year later because of my feet pain, what has worked for you with high arches?
[hdrcnoa] (score 1, diepte 1 OP) I'll look into them, thanks
[hdrk3xb] (score 1, diepte 5 OP) Oh really? I figured the regular style would be pretty similar to my Stan Smiths, but maybe not
[hdrmubm] (score 1, diepte 5 OP) Sweet, I might do that
[hdro7to] (score 1, diepte 6) Hi, just thought I'd give my two cents, I also have super flat feet and the old skool comfy cush vans gave me really bad blisters on my heels so if you do get them walk around the house for a bit to make sure they don't do the same to you
[hdrsg0g] (score 1, diepte 7 OP) Good to know
[hdrp77s] (score 1, diepte 6) I personally get the ones that have the extra sole... Like classic, but not the cheap ones. Idk what they are specifically. I swear by them though. No they are not comfortable long term, but they are the most comfortable I've ever found! Only thing more comfortable is a good, broken in pair of doc Martens
[hdrwqm7] (score 1, diepte 5 OP) I'd rather have comfort than non-slip, if those are mutually exclusive. There is little chance of slipping where I work, it just doesn't ever happen.
[hds057q] (score 1, diepte 2) I have flat feet and too and love working in converse
[hdstr50] (score 1, diepte 2) I have flatter feet and vans have never steered me wrong at work
[hdsu6fd] (score 1, diepte 3 OP) Any specific kind you recommend?
[hduq2ip] (score 1, diepte 1) I have to wear Vans or Converse as part of my uniform, Converse crush my toes together and they hurt my feet and Vans are only really good for flat feet unless you have good insoles, they also end up stinking after a while so I have to wash them regularly. What are the best Vans to wear? I just have the slip on ones and even with insoles they hurt after a couple of hours 

Sketchers are so comfy but my work doesn’t like us wearing “sports branded trainers” and apparently Sketchers fall under that but Vans and Converse don’t 😂
[hduvwca] (score 1, diepte 2) The vans authentic are the ones I go for every time. From dive bars to 5 stars in those and I haven’t busted my ass. There’s just the smallest tag and you hardly notice with the black on black ones.
[hdrgx7m] (score 1, diepte 2) I spend about another $120 in ortho insoles. Actually go to an ortho office to get them made. They easily last me a year.
[hdrdvwh] (score 1, diepte 1 OP) I do love New Balance. Which model are they?
[hdrggr4] (score 1, diepte 2) Pretty good. I would wear them bartending and serving sometimes walking 8-10 miles a shift. Did pretty well. I will say don’t spend 200 bucks on a paid of limited shoes just go to an outlet and grab something. Same material
[hdrgt8y] (score 1, diepte 3 OP) Right. I'll look into those some more, thanks.
[k9i6dgm] (score 1, diepte 1) What kind of insoles?
[hdrjiof] (score 1, diepte 1 OP) Okay cool, those are definitely on my shortlist
[hdrnb4w] (score 1, diepte 1 OP) Which model?
[hdrnoer] (score 1, diepte 3 OP) Cool, I'll check those out
[hdrokll] (score 1, diepte 0) They don't sell 'em anymore but I have a lifetime pair of Doc's that I tended and served in for 15 years, replacing them twice.
[hdrru3z] (score 1, diepte 1 OP) What's the best kind that they do still sell?
(24 reacties met lagere score weggelaten)

=== THREAD 1r1u4xt ===
SUBREDDIT: r/retailhell
DATUM: 2026-02-11  SCORE: 112  REACTIES: 102
TITEL: How do cashiers stand for 6-8 hours almost everyday without ending up with excruciating foot pain?
POST (source_id=post):
Just curious on how cashiers are able to stand for 6-8 hours or maybe more in some cases that too I'm guessing at least 5 days a week. 

doesn't the foot hurt after standing for so long and do cashiers notice any long term foot issue because of standing for long hours that too almost 5 days a week?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[o4s4vki] (score 189, diepte 0) We don’t.
[o4s1xgj] (score 133, diepte 0) I have decent shoes, two anti fatigue mats and very good insoles and it still hurts. The human body simply isn't built to stand for 8 hours in one spot, it's gonna hurt no matter what
[o4s1anq] (score 130, diepte 0) Anti fatigue mats are a thing, and you definitely get used to it after a while.
[o4s78t1] (score 48, diepte 0) You get used to it really quickly. Good shoes help but honestly it's time that's doing the most work.

When I went back to retail after covid, I'd been sitting around for like a year and a half.

I would basically collapse as I got out the door each day from 5 hour shifts. My whole body ached. I would go to sleep and when I woke up the first steps were torture. 

But after the first few weeks it gets easier. A couple of years later and I could easily stand for a 12 hour shift no prob.

When I was in my early 20s I went on a camping trip with some friends. All my friends were much fitter than me. I didn't exercise at all and was pretty overweight at the time. But I worked in a busy cafe running around all day and they worked office jobs. The trip involved a lot of walking and everyone was completely wrecked, but me. I didn't even feel it.

It's crazy what your body will become accustomed too.
[o4svna2] (score 36, diepte 0) The life of retail is a life of back and foot pain. Anti-fatigue mats help, but don't solve the issue.
[o4s7t7h] (score 31, diepte 1) Exactly right. Ask your manager to get you one of the mats to stand on, they make SUCH a difference. If I worked somewhere that wouldn't supply one - which is unlikely - I would buy my own on Amazon. They make that much difference.
[o4sb5lm] (score 28, diepte 0) We don't. You wear padded socks, memory foam shoes and stand on anti-fatigue mats and still end up with foot pain. Those Dr. Scholl's insoles commercials generally don't name cashiers, but they could.
[o4saim3] (score 22, diepte 2) I worked at a place that had them, but at times I’d work self check out for days in a row. Self checkout also had them, but corporate started getting all pissy and told the managers we weren’t allowed to stand at the little screw area anymore, which is where the mats were.
[o4s1etm] (score 17, diepte 0) Comfortable shoes, using orthopedic insoles, and anti-fatigue mats.
[o4s27sj] (score 17, diepte 0) I found I was fine till I was older in my 30s then it becomes an issue
[o4sbuth] (score 15, diepte 0) Move as much as you can! Walking is easier than standing! Anytime you're not checking someone out, move around. Face product near the register, restock bags or register stuff. Whatever, just MOVE! It helps so much.
[o4t0zjk] (score 12, diepte 0) Long term effects I've experienced: bone spurs, fallen arches, lower back issues, and numbness in my toes that last well over a decade after quitting retail.
[o4v952c] (score 10, diepte 2) We wanted a mat at my job. And my company won’t allow it. Cause of “cosmetic” reasons.
[o4sbzn5] (score 9, diepte 1) Was gonna mention this. I'm in my 50s & spent teens they early to mid 30s in standing/ walking jobs. It hurt then but now my feet never not hurt no matter what.
[o4vsftv] (score 8, diepte 1) Also, if this becomes your life, get ready for early knee replacement surgery.
[o4s3vn3] (score 7, diepte 0) You only get tired if you don’t do anything but after a while it gets easier. The trick is don’t be a slow cashier
[o4scsdn] (score 7, diepte 0) I didn't, it was absolutely awful for me. My left pinky toe likes to dislocate if I stand on it for too long so I constantly had to have my partner pop it back in every day. On my really bad days, or the days I'd have to cover a closing shift after opening and was there for 17+ hours with no actual break, I'd have to keep kicking my shoes off behind the counter to relieve some pain or I felt like I was standing on acid covered glass shards. Definitely one of the worst things I dealt with, I can still remember days I'd have to sit on the floor with my shoes off, just absolutely bawling my eyes out cuz the pain was so bad, thankfully my coworkers were awesome about it and picked up my slack till i could stand again.

I am absolutely of the opinion that cashiers should be able to sit while working, I would've also loved it if we were allowed to just sit for a few minutes in between customers (I worked at a gas station so it would have been a lot of up and down to get cigarettes and lotto for people). I have multiple health issues and corporate told me that even with a Drs note, I still wouldn't be able to sit while working so my options had been suck it up and deal or lose my job
[o4tflty] (score 7, diepte 1) Yes, but sitting would afford cashiers a small amount of dignity, and we can't have that. /s
[o4sg6tl] (score 7, diepte 0) Don’t have a choice I just deal with it, no matter what shoes, inserts etc I still have planter fasciitis. When I have to stand and run around for 8+ hours with only 30 minutes not even to rest it just hurts.
[o4ubynx] (score 7, diepte 0) Why are cashiers standing? That seems stupid. All of ours have comfortable chairs
[o4x13qb] (score 7, diepte 1) Because in America people have this weird mindset that if a cashier is sitting they're somehow being lazy and unproductive yet they don't bat an eye at people with office jobs
[o4s9wg9] (score 6, diepte 0) I don't sit except for break either. But I'm a stocker. The difference is I move around, kneel, etc. 


I have high arches (the shape of the bottom of my foot is very curved and doesn't touch the ground where it should). 


I've found that support matters more than squish. I have a pair of boots that nobody who makes this kind of money should have and for me they help a lot. 


I have had HOKA and Brooks and my ankles get tired. With my Nick's that cost more than I make in a week? Nope. But if you don't want those, Thorogood aren't bad.
[o4wr7vu] (score 5, diepte 3) Remind them of this next time they give you the “We are a family” line.
[o4sd9yf] (score 5, diepte 0) the long term foot issue thing is absolutely a thing with cashiers yeah. i usually feel it in my back at the end of a shift instead of my feet at this point though. when i first started it was so horrifying, i had 0 idea how people did that daily lolol
[o4t0ryz] (score 4, diepte 0) I stand 40 hours a week on concrete & my feet were not the best. Good supportive shoes, extra inserts for them (gel heel cups, etc), & my Chiropractor adjusting my feet weekly has helped tremendously. 

One thing that sucks though is that my feet sorta flattened or widened over the years & I went up part of a shoe size. I used to wear size 8 & occasionally 7.5, depending on the shoe, but now I’m at 8.5 for regular & 9 for anything that requires a sock (sneakers, boots, etc).
[o4ww8fv] (score 3, diepte 4) They don’t do that line with us lol
[o4z16fl] (score 3, diepte 3) Get a doctors note then revisit the question.
[o4vedgi] (score 3, diepte 1) I’m in my 30s and even my Dr laughed when I said my current nerve pain in my foot wasn’t the plantar fasciitis he thought it might be (cause I’ve had it and know what it feels like). I also get pain on the top of my foot too!

I got new shoes that do feel great but yeah even with compression socks and regular elevation when I’m at home my feet go through a lot!
[o4xr7l5] (score 3, diepte 1) This ^^ Exactly this.
[o5dnkrv] (score 2, diepte 3) Wow. That’s a pain when managers/corporate won’t allow that. Don’t understand it. I’ve seen Aldi cashiers have seats . I think that’s perfectly acceptable for a cashier at any store. We aren’t robots.
[o5et2pj] (score 2, diepte 4) It’s because they aren’t going through it. Managers are spending all their time sitting at their computer in the office, and corporate has desk jobs.
[o4vr01c] (score 2, diepte 1) These >>
[o4vsbsa] (score 2, diepte 1) Yeah but it still hurts.
[o4wr2cs] (score 2, diepte 1) I don't like the mats they are trash and fick up my posture.
[ollhua9] (score 2, diepte 1) I'm a retail closer/cashier too, and that appointment paralysis is real. If only I didn't "need" some food after work lol. I'd go straight to bed too. Probably best.
[o4sbzjt] (score 2, diepte 0) Hoka shoes and compression socks. Calve raises and stretchs when you get a moment without customers.
[o4sjswp] (score 2, diepte 0) I invest in my shoes. Hoka brand orthopedics. Also I complaon about taking a break every two hours
[o4smdg3] (score 2, diepte 0) Wear good shoes I had 10 hour shifts and only cover and where hokkas all day
[o4so730] (score 2, diepte 0) Mats are about as important as shoes.  I do 45+ hours a week on my feet.  Hoka shoes are amazing.  For reference, I'm 6 feet tall and almost 300 pounds.
[o4srfyz] (score 2, diepte 0) Adrenaline i think. I dont feel pain in my feet until i sit down for a bit, then i can hardly walk for a bit till it kicks back in
[o4ssf49] (score 2, diepte 0) Special insoles, having a stool nearby to get those CRUCIAL 5 mins of being off your feet.

Standing on one leg to relieve the other, leaning against the cash register etc...
[o4sv99j] (score 2, diepte 0) I’m 25 and it’s less my feet and more my hips and back if I don’t move enough. The slight twisting to move items from the counter to the bag, and I think because of my height and the way I have to pick things up, hurts after a few days 

I do as much busy work as I can, or feel like, because actual movement helps a ton
[o4sve1p] (score 2, diepte 0) New Skechers every 6 months- 1 year. I’ve had some days where my feet slightly ache but it’s always better the next day. The most I’ve done is 9 hours. I also don’t stay still and make sure I’m walking around amounting to something else when I don’t have a customer.
[o4swrlq] (score 2, diepte 0) Who does not have foot, knee, or back pain?

At the beginning of my shift, I'll be standing upright. At the end, I look like an old lady,  hunched over and limping, from back and foot pain. And that is from standing on anti-fatigue mats.
[o4syatr] (score 2, diepte 0) Anti fatigue mat plus better shoes. I bought Brooks and they help so much.
[o4t0iy7] (score 2, diepte 0) Your feet and lower back ache after a long shift.  After an eight hour shift, I’d go to my car and turn on the seat heater for my back — in Florida, when the outside temp was very comfortable, not chilly at all! — because I could barely move otherwise….
[o4t4850] (score 2, diepte 0) Good shoes are a must. I move as much as possible. Load the customer’s bags while I wait for their transaction to process and receipt to print, sweep as soon as it’s needed, just as much movement as possible. I have osteoarthritis in my back and standing in one place is hard. I’m lucky that although I’ve been working on my feet since 1981, my legs and feet are holding up well, with the exception of calluses.
[o4t5j5a] (score 2, diepte 0) The less weight I have the less foot pain I have 😩. I gained a few pounds recently so my feet were pretty sore yesterday.
[o4tax4h] (score 2, diepte 0) Because I have good shoe inserts that are made for standing and walking. Maybe you’re not wearing good shoes. Eight hours is pushing it but I make it through okay. Six is a walk in the park.
[o4ts14d] (score 2, diepte 0) Hokas
[o4vv98d] (score 2, diepte 0) My back ends up hurting more than my feet, but I have a bad back. Also anti fatigue mats at the registers helps a lot.
[o58jae6] (score 2, diepte 0) Our feet are tired
[o51uq19] (score 1, diepte 1) theyre needed but idk what the replacement would be for retail where ur walking around the store and not really standing at the register ugh
[o4s2wml] (score 1, diepte 0) I work overnights, so usually I cashier but I also have to do maintenance or cleaning, so I always try to stay busy as to not get feet pain, but I still feel it
[o4s544j] (score 1, diepte 0) Magic
[o4s5rdl] (score 1, diepte 0) If you have a sales floor you can move around on then you will get acclimated, especially if you have the ability to invest a bit into better, more supportive shoes.  If you are a cashier and have to stand in one place for 8 hours then you are fucked.

It took me months to get used to a more sedentary job to one that I had to be on my feet all day.  It probably took longer because I used lightweight walking shoes with thin soles.  Invest in shoes with thicker soles and even get insoles if you need further support.
[o4tb36c] (score 1, diepte 1) I’d rather walk around for 8 hours than stand in one spot for 8 hours so
[o4sk0rf] (score 1, diepte 0) You don't get used to it. 

When I cashiered my feet hurt constantly. I'd rotate my shoes regularly. And have a couple pairs dedicated just for work. After a while I started to have foot and back pain.

Almost every place that I worked had anti fatigue mats behind the registers. But almost every place I worked if you didn't have a customer you had to be out in front of the register and not behind it. Which makes your feet hurt more.

I don't have much foot pain anymore. But I had lasting back issues because of it.
[o4sr3ym] (score 1, diepte 0) Don't get me wrong, cashiers should be allowed to sit if they choose, but standing 8 hours a day and ending up in severe pain (rather than just a little bit of discomfort and fatigue) is an indication you've got a medical issue. That's not normal.
[o4tckb6] (score 1, diepte 0) My feet don’t usually hurt, but my back kills me.
[o4tcpum] (score 1, diepte 0) I developed ‘policeman’s heel’ after two years on the floor. Comfortable footwear is essential.
[o4tkyw3] (score 1, diepte 0) That's the neat part.

I have knee pain already and when I worked cash it was a million times worse. Those "anti fatigue mats" don't do a damn thing
[o4tnry4] (score 1, diepte 0) I retired as a Walmart cashier at age 70. I have wide feet with protruding pinky toe joints. I got by with OrthoFeet wide toe box shoes and compression hosiery.

After I retired, I had my right knee replaced.
[o50ejb6] (score 1, diepte 1) congrats on your retirement!
[o4ty2hp] (score 1, diepte 0) Floor mats and Hokas. I have plantar fasciitis from standing on my feet for so long. The Hokas help immensely.
[o4u0o5k] (score 1, diepte 0) In most developed countries cashiers are allowed to sit.
[o4u36x2] (score 1, diepte 0) They do.
[o4u6e2k] (score 1, diepte 0) 100% it’s just getting used to it
[o4u87p4] (score 1, diepte 0) I’ve been 40+years in the grocery business: If you work 6-8 hours where I’m from, you get two 15-minute breaks and a 30-minute lunch. May not sound like a lot but when taken strategically, it affords enough of a break to not feel fatigued. We also provide anti-fatigue mats and a chair/stool (if needed) at every register. 

If an employer is not allowing any breaks or needed accommodations for their cashiers during those shifts, it’s good sign of shitty, cheap management and you should quit. You  deserve better.
[o4ya330] (score 1, diepte 1) This infuriates me because I worked for a union grocery store and for an 8 hour shift we only got one 30 minute lunch and one 15 minute break. When a worked an 8 hour shift at nonunion store called Party City (RIP) I got a 30 minute lunch and TWO 15 minute breaks. The fact I would often stand 4 hours straight before getting my lunch meant my back and knees were in agony. I even asked my manager not to give me 8 hour shifts because of this but they refused. They haven't even given me any sick pay even when I requested it telling me I didn't have any which was impossible.
[o4ucp9v] (score 1, diepte 0) I move around a lot which definitely helps.
[o4ufdov] (score 1, diepte 0) Nah. First of all, those cashiers that stand aren't just cashiers. They do fill in stock from the warehouse, clean up the store, serve customers etc. When I was working as a cashier in a typical convenience store, I actually walked way more than stood. It's not like cashiers in supermarkets stand, as it would make no sense at all (what for if they are only cashiers? Besides, this could cost the company a lot), as I fail to see how a cashier that stands works faster than one that sits - at least at the cash register, because in a convenience store, yes sir! As you will be not only at the register, and need to move quickly.

So, maybe start moving? I'm sure that in the shop you work for there is always something to do. Feet hurt? Walk around and check if all is restocked. It never is, so do that. Afterwards check out several customers, and again. If by some weird luck everything is restocked, then clean up. It is also movement. The reason you feel pain is probably because you don't move.
[o4uk4wm] (score 1, diepte 0) I cashiered for four years during college - after a shift I would quite literally hobble and limp around my apartment. Thick fluffy socks gave a little bit of comfort, but it hurt a lot to stand and walk after a shift
[o4uoqon] (score 1, diepte 0) It hurts.
[o4uwiaw] (score 1, diepte 0) Good shoes are definitely an important aspect. If you can, I highly recommend finding a running store that will fit you for the right support type and recommend shoes based on your activity level/support type.
[o4uz6h6] (score 1, diepte 0) I left every shift in pain even though I had custom orthotics, and anti fatigue mat*s*. Allowing cashiers to sit is so humane
[o4uzm2f] (score 1, diepte 0) They don’t. I used to work retail 40+ hours a week and could barely walk sometimes when I got home cause my feet and legs hurt so much. And that was when I had good supportive shoes. I have ankle and knee braces for when pain days were super bad too
[o4v5d1o] (score 1, diepte 0) I know shoes and the mats help but im at a loss at my new job. We have the mats, I wear my comfy shoes but it’s still a lot. My old job I could just venture around the store before going back to my post but at my current one I gotta stay in my area unless I absolutely need to go and put something in receiving or go to the bathroom, break, or see a manager. It sucks it truly does because my feet kill me, but I think a big thing is also getting used to it. I’m not used to standing for that long of a period of time and not being able to venture around
[o4v8ybl] (score 1, diepte 0) Good shoes. 


Buy a pair that doesn’t bend easy. If it bends too easy you’re hitting the ground harder. Good shoes are expensive. Stay away from Sketchers they’re garbage for most people. And foot doctors even say stay away from that brand.  

If you need good insoles, look up PowerStep on Amazon. You might be able to find specialty shoe stores that sell them. You can google what arch type you have if you’re not sure.
[o4vg741] (score 1, diepte 0) Anti fatigue mat plus Skechers for Work.
(37 reacties met lagere score weggelaten)

