# Label-batch batch_0150

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
Schrijf het resultaat naar `batch_0150.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1ioh0ze, i97c63, 1kvbl9g, 78a49w).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1ioh0ze ===
SUBREDDIT: r/physicaltherapy
DATUM: 2025-02-13  SCORE: 15  REACTIES: 61
TITEL: Shoes that you can recommend
POST (source_id=post):
So I need some of your suggestions about what shoes you find comfy and versatile that you can use during longs hours of standing in the rehab and can be used at the gym as well. I have no arch, both feet pronates, and knees have genu valgum. I sometimes ask for a moment from my patients before I show them exercises that involves the LE because my ankles and knees hurt. I can’t use shoes with heels (eg. Ultraboost) because I have recurrent B ankle sprain. I just want to somehow alleviate these things because I don’t usually sit while handling a px because it doesn’t seem professional to me. But hey that’s just my opinion and I am in no way pushing this thought on others. Looking forward to seeing your suggestions!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mcjgxcu] (score 30, diepte 0) I use brooks due to the discount
[mcjevm3] (score 18, diepte 0) Recently switched to Brooks. Happy so far. 
PT/OT also get a 40% discount at Brooks.
[mcj8t7r] (score 13, diepte 0) I can't recommend minimalist shoes enough. I have two pairs from Xero currently. I've heard good things about flux, vivobarefoot and Lems. If you want to try minimist shoes first without breaking the bank you could look at Within brand on Amazon. My guess is they are cheap Chinese knock offs but they do look nice. I have not used them before though.
[mcjsny0] (score 13, diepte 1) As someone who worked at a store that performed gait analysis, it’s more of a sales tactic than anything. I wouldn’t put too much weight in it.
[mcjioxy] (score 11, diepte 0) Shoe needs and preferences are very personal but I have TopoAthletic Terraventure 4s and love them. They’re wide-toe box trail runners with a stable sole and a very low heel drop. I think they would be a good foundation to add inserts too as well to address more specific foot issues if needed. 

I work in acute care and am on my feet all day. I don’t like squishy shoes because I do a lot of lifting and want firm support.
[mcjbja9] (score 9, diepte 0) Sounds like stability shoes would be good for you - my advice is honestly to go to a running store and try a few pairs out.
[mcjsyep] (score 8, diepte 2) Just so you know, most brooks have as much or more of a heel (10-12mm) than ultraboosts (10mm) so they may not be perfect for you.
[mcjglfd] (score 7, diepte 1) I’m on my second pair of Whitin’s after over a year. I’m still in school so $100+ for shoes is not reasonable. I’ve found Whitin’s to be solid quality. I plan on getting Vivo hiking boots as a graduation present to myself after I finish my PTA program in May.
[mcjr49k] (score 5, diepte 1 OP) I do agree that I need stability shoes and I’ve tried running shoes from stores but idk maybe my feet aren’t used to them like it feels weird standing. Will keep checking out stores tho. Thank you so much!
[mcjrk4n] (score 4, diepte 1 OP) I’ve been hearing a lot of great things about Brooks and I didn’t even know that they give discounts to PTs/OTs but idk if they offer discounts in my country tho 😭 (or I just don’t know how). Thank you for this!
[mcjkgsf] (score 4, diepte 0) Do you exercise?
[mcle0dz] (score 4, diepte 2) Maybe try more prolonged single leg exercises (aired balance, RDLs, squats) to improve foot/ankle endurance. In combination with good shoes or inserts it might help!
[mck1l8r] (score 3, diepte 2) I’m flat footed and I switched to the xero neo prio and love them. I thought it would be rough on me due to having no arch, but they are the most comfortable shoes I’ve ever had. I think having that ground contact actually helps. I have of course tried other “arch support” style shoes in the past and there’s just no comparison. If you’re in a clinic and standing a lot, then you need to be changing posture and sitting periodically anyways. The best posture is not being in one position all day. I would get rid of your definition of professionalism. Do what we teach our patients and show them that you do it.
[mcmqo2z] (score 3, diepte 1) The Brooks booth at CSM San Diego a couple of years ago looked like Black Friday LOL
[mcjw9aj] (score 3, diepte 2) All of their models are wide-toe and low/no heel drop! I usually lean toward trail-runners as they’re a bit firmer vs running shoes. 

Altras is another brand to check out that’s similar. Good luck!
[mcjt3f7] (score 3, diepte 1 OP) Yes! Mostly weight focused and a little cardio (I hate cardio! Hahaha)
[mcjsv0m] (score 3, diepte 0) I have hypermobile feet with pronation and was doing Orangetheory Fitness so I needed a great stability shoe. I went to be fitted out a running store because they know what they’re doing, and the shoe that worked best for me was Mizuno. I’d always worn Ascics and wasn’t even familiar with this brand, but I tried on a bunch of shoes and these are awesome for my feet
[mcoo0ct] (score 3, diepte 1 OP) I’ve tried Mizuno before when I was still playing volleyball. I loved playing in it but idk but my pinky hurts when I use it. Maybe the fit wasn’t that accurate but nonetheless I really liked using it before. Thank you for this!
[mckchia] (score 3, diepte 0) With all your issues go see a podiatrist.
[mckg9tt] (score 3, diepte 0) Honestly, I recommend finding a shoe store that lets you try them out and if they don't work bring them back. If you're only using them in office, you won't dirty them up in the time you'd need to figure out if they work for you. 

I also recommend different shoes for different activities if you work at a general population outpatient clinic like I do. My coworkers like to throw friendly jabs my way for having more shoes than them, because I'm the only guy on staff, but I keep five pairs at the clinic (and then I also have several shoes in different colors that I keep at home and wear into the office that match my outfits). Not only does this let me customize my shoe to better match what I plan to do with my patients, but it lets me have options to show patients how big of a difference shoes make in how you interface with gravity.

Lifting: Nike Metcons, I love a loud shoe. They start a little snug because I have wide feet, but they loosen up, after that it's like lifting barefoot on concrete, you feel ridiculously stable. Also great for confidence with fall risk patients.

Treadmill Running: Nike Pegasus, they're a great compromise between weight and support for shorter distances (5-10k) and have the same foam as the fly series that Olympians are running 2 hr marathons in (no CF core tho). Bonus: MSU, my alma mater usually has a branded option so I can wear my Spartan shoes on Game Day. 

General purpose: starts with what I wore in that day, but if I'm feeling anything less than great with that shoe I switch over to a pair of Topo's (have also used Altra's and don't have much of a preference) because they fit my wide feet like a glove. 

Standing: if I'm gonna be up for a while writing notes (my preference to desk work) or providing in service, internal marketing, etc. I like Hokas because it's like standing on a could.

Desk work: if I'm gonna be sitting for a while, usually I throw on some moccasin style slippers because if I'm gonna be miserable, (paperwork is soul crushing) Imma have a treat. 

External marketing: I wear dress shoes from home.
[mcjtjci] (score 2, diepte 2) With Xero they might not have your size in stock on their site. You can try and Google search it to see if other places are selling that shoe in your size. That's how I've had to order some of the ones I own.
[mclxh0b] (score 2, diepte 2) Ah damn that sucks. In the US, I had to log in with my IDME info so that it can be verified. Worth checking out, though!
[mcjrtg2] (score 2, diepte 1 OP) Been seeing a lot of good feedback on Brooks. Thank you for this!
[mcoo7qq] (score 2, diepte 3 OP) Thank you for the heads up! This went down on the rank of shoes I’m considering now 😫
[mcoqsho] (score 2, diepte 3 OP) I’ve been doing this in my rotation of workouts. So far no difference in symptoms but just getting stronger. Thank you for this!
[mcjyv5o] (score 2, diepte 2) Our profession’s discount makes brooks worth it even just to try, you pay like $90 for a pair! I have the gel Kayano 30 and 31s! Asics also gives our profession a discount, I think 25% off!
[mcoqh2t] (score 2, diepte 1 OP) This so informative! I’ll surely check out your recommendations. I couldn’t ask for a better response.

I was actually thinking about getting the Metcon 6 (the only available in stores in my city together with the 9s) but I don’t know if it’s good to use during work. I just want ta be on the go all the time that’s why I’d like to use it in the gym too. What are your thoughts on this?

I aspire to get to change my shoe for every purpose but my funds cannot handle it as of the moment that’s why I’m finding something versatile. Also, we can’t return shoes in stores from where I’m from (I know customer service sucks here) we can only replace them with a different color way and model with the same price point. I’ve tried it a lot of times but nope they don’t allow returns.
[mcltq8c] (score 2, diepte 0) I think a lot of it is trial and error. There are a lot of good shoes but you have to find what works best for you and the daily activity that you do. For me I do better Asics than anything else. If I had to pick a second choice - Brooks.
[mcoqxzw] (score 2, diepte 1 OP) Thank you for this! Heard a lot of great stuff about these brands
[mcmjnnk] (score 2, diepte 0) I wear allbirds almost exclusively for work. They’re comfy to stand in for hours on end and easy to show exercises while wearing them. I actually don’t like them for working out on my own, but I love them for work!
[mcmulj0] (score 2, diepte 0) Try Nike Pegasus
[mcn3l4h] (score 2, diepte 0) Flux footwear
[mcn6d4f] (score 2, diepte 0) Brookes Glycerins!! This years new model just dropped so last years are on sale $30 off if you can’t get the PT discount!
[mcnhbh4] (score 2, diepte 0) Every foot is different. My husband, a podiatrist, has experienced that if his clients love New Balance, they can't wear Asics. I agree.  I find the most comfortable shoe for me is the QC running shoe for all day. So you just have to find comfortable shoes for you and buy a couple pair. And every 6 months. I have bilateral (and bad) bunions, but they've improved so much with swimming and manual stretching. I need shoes with a lot of give and good cushion. and my feet don't bother me anymore.  Go to an REI or Jax or some athletic store and spend some time trying them all on with an experienced shoe guy.
[mcj7t3o] (score 1, diepte 0) Thank you for your submission; please read the following reminder.  

This subreddit is for discussion among practicing physical therapists, not for soliciting medical advice.  We are not your physical therapist, and we do not take on that liability here.  Although we can answer questions regarding general issues a person may be facing in their established PT sessions, we cannot legally provide treatment advice.  If you need a physical therapist, you must see one in person or via telehealth for an assessment and to establish a plan of care.  

 Posts with descriptions of personal physical issues and/or requests for diagnoses, exercise prescriptions, and other medical advice will be removed, and you will be banned at the mods’ discretion either for requesting such advice or for offering such advice as a clinician.    

Please see the following links for additional resources on benefits of physical therapy and locating a therapist near you

[The benefits of a full evaluation by a physical therapist.](https://www.choosept.com/benefits/default.aspx)    
[How to find the right physical therapist in your area.](https://www.choosept.com/resources/choose.aspx)     
[Already been diagnosed and want to learn more? Common conditions.](https://www.choosept.com/SymptomsConditions.aspx)  
[The APTA's consumer information website.](https://www.choosept.com/Default.aspx)  

Also, please direct all school-related inquiries to r/PTschool, as these are off-topic for this sub and will be removed.


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/physicaltherapy) if you have any questions or concerns.*
[mck60ry] (score 1, diepte 2) same, ive been [These Whitins](https://www.amazon.com/WHITIN-Barefoot-Minimalist-Training-Weightlifting/dp/B0C737RJ3Y?crid=25KGO46UC5KQC&dib=eyJ2IjoiMSJ9.E4O_1ZLcubZlfiwKnu2sERbCWNtELiD8qBVWxoQ7BRHoIS_ez3VZ70aLwt4YfZxUJfm9rnXw64o3YYSiUsNKsti10-5c1Nldvg_1yJ8FJPLetwZctUc54bof3sVlMMX7E6tWzizbS7on8gqrfF9ttjPlPunsftdeNDsdwyfzX1yximMw_sitEbMbwXLYG9GJwI0K3l50owwN6CRrz8-WOY8eF4-9PiK-5nhhBVW_bpQ_GjbSZoXI5illSERlO8cx--lDox-W4DKnsyvY6_FB_mpv8DmE94WEVhuIa2sNAIPy5nFNhTjUm5HMS4-kCjplkPypSEaKd2fAWJxqPyM9h-um_L7HJfXVK-GJ-4b-ZdEyus-qsfSQoB1tRYjFXGHygDQ61-NPvWiAF82OkuGQJxLVdO9FmU6ML8ifWh0xAtahHkybOZWlZ9LqFdixz5gq.2dDfxl7IdH6djH0TQPlreE3CQ_ieHWDHB09iIYmJh_c&dib_tag=se&keywords=whitin+shoes+for+men&qid=1739459285&sprefix=whitin%2Caps%2C135&sr=8-11) for about a year in acute care.
i bought [these pair of Nortiv yesterday for running, looks like HOKA ripoffs](https://www.amazon.com/dp/B0D1C77C3N?ref=ppx_yo2ov_dt_b_fed_asin_title) , super comfortable and its like im walking on a cloud lol. Also went on a run with them this morning and felt great, didnt even need to break it in.
[mcjqis8] (score 1, diepte 1 OP) These are great suggestions! I looked them all up and I’m leaning more on Xero and Flux based on what I saw. Thank you for this!
[mcooxxr] (score 1, diepte 3 OP) The Xero shoes are currently top on my list! Also, I do change posture every now and then. I can sit down when I personally don’t have a px and during breaks too. I was just influenced by my CIs about the professionalism thing and have brought it up until now but I get your point. Thank you for this!
[mcqisnh] (score 1, diepte 2) r/unpopularopinion
[mcjsw71] (score 1, diepte 1 OP) Yes, it does come down to one owns preference. I like this tho especially because it has a low heel drop. I think I’ve seen one.m of my CIs (he worked in the middle east for quite some time) wear this. Thank you!
[mcl6t3d] (score 1, diepte 2) What led you to your heel drop preference?
[mcprl1e] (score 1, diepte 4) Im not a huge advocate but I have a coworker who swears by foot intrinsic exercises
[mcjtaq5] (score 1, diepte 2 OP) Thanks for the heads up!
[mco61rt] (score 1, diepte 2) The stores I've seen that do it look at pronation vs supination, how your foot hits the floor, etc. They recommend the type of shoe but didn't push you to buy from them.
[mcjt8nf] (score 1, diepte 1 OP) I’d love to but I don’t think we have it here in our area. Thank you tho!
[mcjm73t] (score 1, diepte 0) I have absolutely no arches either and I overpronate as well. Granted my feet don’t bother me except when I run, but still. I LOVE Asics gel kayanos, and the brooks adrenalines are also great!
[mcjtz4a] (score 1, diepte 1 OP) Wow Brooks really is a crowd favorite. Speaks a lot how good their shoes are. Also, what specific variant of Kayanos do you recommend? I swear I just saw this a min ago on my tiktok
[mcooklk] (score 1, diepte 3 OP) I didn’t know about the discount Asics gives! I really hope the discount works in my country. Gotta research more on that
[mcjs13o] (score 1, diepte 0) I have custom orthotics I can use in some shoes, but I have also used wool scaphoid pads from Hapad to support my arch. You just stick them in and they live there for the life of the shoe. Also, super helpful if you are wearing shoes that won’t accommodate an orthotic. https://www.hapad.com/product/scaphoid-pads  We get a discount as PTs.
[mcopeha] (score 1, diepte 1 OP) Will do if the time permits because we don’t have much podiatrists in my city so I have to travel to another city to see one. Thank you!
[mcqq1tj] (score 1, diepte 2) If I was only picking one shoe I'd pick an anatomical shoe like topo or altra as it gives good support and won't warp your foot, plus serves the purpose of demonstration for patients who need it. Build out from there. I only buy a new pair a few times per year, my supply is from years of being a PT. If you're only using them in house they'll last several years
[mcormjj] (score 1, diepte 1 OP) Thank you for this! The tree dasher and glider are so cute! Do you think they’re good?
[mcorqo7] (score 1, diepte 1 OP) I have one! But I always trip when I use them 😭
[mcorww3] (score 1, diepte 1 OP) Checking them out rn. Thank you for this!
[mcos5nj] (score 1, diepte 1 OP) Was told that brooks had more of a heel and it plays a big factor with my ankle sprains 😫 was considering this tho. I’ll still check them out. Thank you so much!
[mcoswa8] (score 1, diepte 1 OP) I have B bunions too and it deviates my 2nd distal phalanges outward. Been manually stretching it for more than 4 years now but still no progress. Can I dm you about your program?

Anyway, I haven’t tried QC but will try them when I get to a store. I’ll keep searching for the best shoe because I can’t stand it anymore (both figuratively and literally). Thank you for this!
[mjxdf89] (score 1, diepte 2) I just stretch to keep the range as far as I can one to two times a day for about 5 minutes.  You might not see progress, but you might have kept it from getting worse... arresting the degeneration. Of course, I always also use counter stretching (resistance both ways to assist with keeping the range good.  My joints there look like golf balls... lol. They're quite calcified and obviously have had a lot of inflammation, but I rarely have pain in them. (I do recommend resistive extension and flexion with 5 second holds X 3  of your great toe along with the manual stretching. )
[mcq7zff] (score 1, diepte 0) New balance 990v6
[mcuemto] (score 1, diepte 0) Give Altra a try! They have the wide toe box so your toes can start to work how they're supposed to!
[mcxtkme] (score 1, diepte 0) What really helped me was going to a podiatrist who examined my foot and wrote down exactly what I needed and told me what store to go to. I went, tried on the shoes and it was instant relief. Haven’t looked back since.
[md0w5qp] (score 1, diepte 0) ASICS are my favorite, but I have also had great experiences with Altra/zero drop shoes.
[mcpq6it] (score 0, diepte 1) They have perfected the art of making ugly shoes
[mcqjxzp] (score 0, diepte 3) Yeah maybe, I just dont vibe with them at all
[mck0daf] (score 0, diepte 0) I also have pronatated feet and collapsed arches. I find many of the running shoes that even I recommend to be kinda ugly. I have nike zoom pegasus the 40s and up are stylish and I can wear them all day for my 10+ shifts no issues compared to other shoes I have tried.
[mcjlixp] (score -1, diepte 0) Your best bet is to go to a store that does gait analysis. They will let you know which shoes best fit you

=== THREAD i97c63 ===
SUBREDDIT: r/AmazonFC
DATUM: 2020-08-13  SCORE: 69  REACTIES: 61
TITEL: Update: So I threw $$$$ at my foot pain problem with shoes fitted by a specialist at Fleet Feet and insoles from the Good Feet Store
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[g1dbrkr] (score 28, diepte 0) Just bought a pair of ultraboosts after my vans ortho shoes wore out. Trust me your feet are gonna be feel so much better at the end of the day
[g1dp423] (score 16, diepte 4) Please tell me you meant $120 and not $1200.
[g1dhwgy] (score 15, diepte 0 OP) I just got a new pair of shoes/inserts in today... I've been dealing with foot pain for longer than my time at Amazon. I might have to check this out if my new stuff doesn't work out. High arches + wide feet + wide-splaying toes = hell.
[g1dmrqa] (score 12, diepte 3) So this is the question right... the Good Feet insoles were $1200 - which I definitely initially felt my stomach turn at. I was desperate to find a solution to my foot pain though. I was able to arrange a payment plan.  There's also guaranteed refund (minus a fee because they can't be resold) if the insoles still aren't helping after the month long trial period. 

My mom walks very slowly and with a limp and she's only in her 50s. I didn't want that to happen to me. And with half the country out of a job right now, I'm trying to do everything I can to succeed at this job.
[g1dq7is] (score 11, diepte 6 OP) You have good reasons to do it, thank you for posting, I think I will look into this. I've seen other stuff that's cheaper but when I look at it I still don't believe much is put into them.
[g1dcoya] (score 9, diepte 0) I’ve been using the good feet insoles for 20 years. They are life changing
[g1dpdbw] (score 8, diepte 5) I wish. I realize that is like a ton of money but my feet have been hurting so bad and I can't afford to not work. Also, I have scoliosis which was corrected with a spinal fusion when I was 12 and I broke my ankle last year so I thought investing this kind of money would be worth it.
[g1dcupn] (score 7, diepte 1) I hope so!
[g1dd8v5] (score 7, diepte 2) Don’t push it too much at first. I was dumb when I first got mine, worked a 10 hour shift on my feet, the next morning my feet hurt so bad I could barely walk. Wear them a few hours at a time until your feet adjust to them. After a week you should be able to wear them all day long
[g1dds60] (score 6, diepte 3) Good advice for sure. Mine actually came with a "wear" schedule that says how long I'm supposed to wear each pair and it increases a little everyday
[g1e72hf] (score 6, diepte 2) I am surprised you went with Asics, when I tested them against Nike, NB, Sketchers, etc they didn't feel very cushioning. The shoe I picked, which is nearly impossible to find in stores now was the Nike Tanjun (comes in wide sizes). The part of the shoe below the insole actually has some give to it, so combined with the Dr. Scholl's they are very cushioning. The downside to the Tanjun is that the upper is basically a mesh sock and your toenails will wear holes in it within a few months. They also require a minimum couple days of break-in before wearing them on a shift.
[g1dcxx9] (score 5, diepte 1) That makes me feel better about the amount of money I just paid for them lol.  I will say that the ankle that has healed from being broken last year does feel better as I'm walking on the insoles now ~~then~~ than without them.
[g1dr6qk] (score 5, diepte 7) Thank you. There are definitely less expensive options. And those may work for some people and if they do that's awesome. Superfeet and PowerSteps are two of the other less-expensive options I looked into. I just didn't want to waste time buying those and trying them and going another week having to wait for days off to get something else if those also didn't work. If these don't work, I'll collect my partial refund and...see a doctor or reconsider this job. I definitely wanted to make sure that I know I have tried everything I could before I give up though.
[g1dy26c] (score 5, diepte 4 OP) SWEET JESUS CHRIST. Okay, I wish I could afford that, but newwwwwp.
[g1disj3] (score 5, diepte 0) I got hoka one as well. It really felt good, better than my sketcher.
[g1dlx8p] (score 5, diepte 1) I just got them both today and so far I like them but I will really see how they do when I go back to work on Sunday. So I will keep everybody posted. I am optimistic!
[g1dyomn] (score 4, diepte 5) I know. I think I literally said "oh my God" at the store when she told me. I definitely double-checked my balance sheet before I agreed to anything. Also I don't have kids. So ultimately I decided it was worth it but it's definitely not something I took lightly. It's a lot of money.
[g1dz0sj] (score 4, diepte 6 OP) No kids for me, either, but my savings are kinda tight right now, so guess I should do some saving up for a while before I go for it... hmm. This could mean VET. Welp. For my feet!
[g1djbpc] (score 4, diepte 0) And????? So how they working out for ya??
[g1dpnw6] (score 4, diepte 0) Hoka's are amazing
[g1dqk6j] (score 4, diepte 0) And for anyone else reading, I bought an 8 1/2 *wide* instead of my normal 8 1/2 to allow room for the insoles and for a little bit of swelling (just from being on my feet so long) during my shift. Buying Asics without thinking of this first was an expensive mistake. 

So I definitely recommend having your feet, arch, and pronation measured at Fleet Feet or somewhere similar to get a good size and fit and advice from people who specialize in shoes.

edit: update - also you can buy just 1 pair of insoles from The Good Feet Store instead of the whole set. I am going to return 2 of the 3  myself which will reduce the cost.
[g1duy36] (score 4, diepte 0) The part of true irony is I may have picked those if ordered through Amazon...
[g1dzb9f] (score 3, diepte 7) Yeah, if these work and I don't feel like crawling out at the end of my shift then I see some VET in my future lol
[g1ei9sb] (score 3, diepte 1) Runners World recommends the Clifton 7, I am considering that for my next set of shoes since they come in wide sizes. Since they are a road shoe they should have good lateral support. They are a bit pricey at $130, but if they can last 2x as long as a pair of Nike then it's still a fair price.
[g1l2zpd] (score 3, diepte 2) Idk how big the toe box of the Clifton 6 is compared to the Bondi 6, but my feet had problems adjusting to them. I'm a picker and I developed pain in my pinky toes in the original Bondi 6. I returned them and got them in wide and changed my lacing method to open up the toe box. This was unusual for me because I have never gotten shoes in a wide before. If you do deveop discomfort with your Hoka, I would also recommend changing the method of lacing your shoes.
Here's a link to different types of lacing.
https://runrepeat.com/top-10-running-shoe-lacing-techniques
Hope all goes well!
[g1eb4xl] (score 3, diepte 3) I went with Asics because they came up on the list of shoes that doctors and nurses prefer. Saucony, Hoka, and Brooks were also on that list but I chose Asics because they were on sale. I bought a Gel Kyano pair and they were listed as having the most cushioning that Asics offers.  The Hoka pair has waaaaayy more cushion though. I actually avoided Nike intentionally because my last pair ran narrow. But Asics also run narrow as it turns out. Honestly, I should have had my feet measured and tried shoes with a specialist to begin with. I made the mistake of thinking I could get by with just reading customer reviews and researching preferred brands.
[g1eh9k4] (score 3, diepte 0) I'm really glad you did this for yourself. I am almost positive you will see the results you're looking for. And it's nice to see you went above and beyond just buying proper shoes for your feet, working on your feet all day there are only two investments that matter: good shoes and a good bed. Please keep updating this, I'm really curious to know how you make out after your second week with them!
[g1f74nc] (score 3, diepte 0) The secret of less whole body pain is...........











HEEL CUPS.  Along with a good pair of inexpensive inserts your body, from the tips of your toes to the base of your neck will feel better.
[g1dlrtr] (score 2, diepte 1) I just got my insoles today and so far I like them. The real test will be when I go back to work on Sunday.
[g1dm00b] (score 2, diepte 2) How much were they
[g1gttps] (score 2, diepte 6) im sorry that you have foot pain.but damn you got ripped off bad lol
[g1dlubq] (score 2, diepte 1) I really like them so far. Of course the real test will be when I go back to work on Sunday but they seem to have great cushioning.
[g1dmk9g] (score 2, diepte 2) I work 10hr shift. on my sketcher i last 4-5hr when my feets starts to hurt. on hoka’s my feet last 7hr.
[g1dp2yb] (score 2, diepte 3) Yeah, the Asics I had were starting to hurt my feet after just a few hours.
[g1ftqkx] (score 2, diepte 2) The shoes are so worth it though!
I have the Bondi 6. I saw a review on youtube between the Bondi 6 and the Clifton 6, and the person said they were very similar to each other. I believe the large differences are the cushioning (Bondi 6 is more plush) and the heel drop. 
I'm considering on getting a pair of the Clifton 7 so I can rotate the shoes out every other day.
[g1idbqc] (score 2, diepte 1) This is my first pair! I have heard great things though so I am feeling optimistic about my next shift!
[g1dqk2l] (score 2, diepte 0) I just use my old shoes that are starting to fall apart but I use the Dr. Scholl’s inserts and they work great.
[g1dwco5] (score 2, diepte 0) I bought an insole set as well as a pair of Brooks at my local good feet. 10/10 no regrets
[g1e2fyj] (score 2, diepte 0) What worked for me was one of the cheapest solutions, Dr Scholl's Memory Foam insoles in Nike running shoes. The Dr Scholl's cost about $4 at Walmart, and I tried the more expensive insoles and they didn't work nearly as well.
[g1e3wc2] (score 2, diepte 1) Nice, that's really fortunate.  This expense wasn't my first choice. I started with a Asics and no insoles. Then I tried a pair of Spenco insoles. And then a pair of memory foam Dr. Scholl's on top of and then underneath the Spenco insoles (not both on top and underneath). Then I tried just the Dr. Scholls. It just didn't work for me. I think I would have ended up buying insoles all the same but starting with Asics in a regular 8 1/2 instead  of wide was definitely part of the problem.
[g1eg6cj] (score 2, diepte 4) I agree 100% about customer reviews, nothing beats going to a store trying them on and walking around in them. Of course this whole virus thing has made that much harder to do, plus many stores are out of business now.

Most stores stock Nike primarily in standard width, and I also wear a wide shoe so often have to order one I want to get right combo of size/width/color.  I am wearing Nike Revolution 5 now and they are good but have the same mesh upper as the Tanjun so I will be shoe shopping in a few months.
[g1e2hb5] (score 2, diepte 0) Nice!!!!!
[g1e37o5] (score 2, diepte 0) Lmk how it goes I was curious about trying good feet but heard they’re pricey shoe wise I fuck with ASICS
[g1e4fm2] (score 2, diepte 1) Definitely pricey. I liked my Asics. I just should have gotten a wide or a larger size. The Hokas definitely have more cushion on the sole but more/less cushion is a personal preference. I'll post an update at the end of my next work week.
[g1ej55v] (score 2, diepte 0) Use your FSA account to pay for them.
[g1el0to] (score 2, diepte 0) I hope it gets better! I had tendonitis when I was running XC in hs and when I got insoles it healed in like two weeks!
[g1eqkib] (score 2, diepte 0) How much did it cost was it worth it
[g1ictyf] (score 2, diepte 1) I have heard others recommend those as well.
[g1iavm6] (score 2, diepte 1) I stole a chandelier.
[gl5tt27] (score 1, diepte 2) Revival of old thread but I just got fitted by good feet, want to sleep on it before I drop 1200 between the three inserts and a set of brooks. How are you feeling about your purchase now? 

I have really bad daily foot pain even standing for short periods of time looking to finally out that pain behind me.
[g1iatyr] (score 1, diepte 5) So it turns out I can return two pairs of the insoles, which will reduce the amount to $400. So I feel better about that lol. I'm going to keep the mid level pair.
[gjgisnk] (score 1, diepte 2) And?
[g1drbd7] (score 1, diepte 1) You are a lucky person and I'm envious of you. I definitely believe that is true though for you and for a lot of other people. I'm just not one of them, apparently.
[g1dyefl] (score 1, diepte 2) Thanks!
[g1dvxa5] (score 1, diepte 1) lol! I bought my previous pair of shoes and insoles online but they didn't fit correctly and my feet were hurting so I went to the actual stores to get these.
[g1dzknd] (score 1, diepte 1) This gives me hope!
[g1e3wxx] (score 1, diepte 1) Thanks!
[g1id1jq] (score 1, diepte 1) Thanks! I figured investing in preventing the pain now could possibly save me a knee or hip surgery later.
[g1f3bbv] (score 1, diepte 1) I only just started at the beginning of August  so I wouldn't have a balance yet.
[hwtifzz] (score 1, diepte 2) You can do that for good feet inserts?
[g1ib7x2] (score 1, diepte 1) Thanks! I hope it does. They seem to be helping so far.
[g1icr14] (score 1, diepte 1) The whole set of 3 insoles is $1200. I agreed to that at first and then had second thoughts but I can return 2 of the 3 so my cost will end up being $400. I find that much more worth it.
[g1fvpvo] (score 1, diepte 0) Question, where did you get the money?  Amazon ain’t payin enough
[g1h9j5k] (score 1, diepte 0) forced to wear safety shoes all day
[g1ib09l] (score 1, diepte 1) Safety shoes at my fc are optional. I did get a pair of Timberland Pro sneakers through the Zappos/Amazon safety program though. (paid for by Amazon)
[g1vg8o3] (score 1, diepte 1) Redwings. Go try them on.  Some of the most comfy shoes in the world.

=== THREAD 1kvbl9g ===
SUBREDDIT: r/AmazonFC
DATUM: 2025-05-25  SCORE: 17  REACTIES: 61
TITEL: Does anybody use the free insoles? Are they comfortable?
POST (source_id=post):
title

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mu8b8x3] (score 27, diepte 0) I think putting sand and rocks in your shoes would be a better insert than those I have no idea how they’re retailed at 65$
[mu8r1pa] (score 8, diepte 0) It took about 2 weeks for my feet to adjust, but they absolutely help with my hip, knee, and joint pain.
[mu87dso] (score 6, diepte 0) For free they’re okay been using them for 2 years now
[mu8axsd] (score 6, diepte 0) I enjoy them I have terrible feet and I can survive the full week in them.
[mualm7m] (score 3, diepte 1) Insoles should be replaced every 6 months up to a year, depending on how much you walk in them. 2 years is crazy, especially for the Amazon ones.
[mu87rib] (score 3, diepte 0) They wouldn’t fit in my free safety shoes
[mu8yb3z] (score 3, diepte 1) it’s like college tuition, “state will pay for x so would you look at that our tuition costs exactly that”. They don’t cost that much they just know amazon will pay for it.
[mu8dwq1] (score 3, diepte 0) Absolutely terrible. I don’t know how anyone uses them.
[mu8mr1r] (score 3, diepte 0) I usually just get them to cost the company money for them and them give them away. Absolute trash
[mu8yzqb] (score 3, diepte 0) It’s free insole twice a year. It’s better than nothing and comparable to the $20 ones you buy at the store. I feel the $65 price tag is just so they can write it if as a greater expenses because they give away so many. Probably $2 to make
[mu8f6s4] (score 2, diepte 0) Those insoles messed up my feet for months. 

Every now and then I see someone say they work great. I'm guessing you have to have a very specific foot shape for them.
[mu8mot5] (score 2, diepte 0) I got them and I have no problems. I’d say try it out and see.
[mu8n0gd] (score 2, diepte 0) Honestly they don't hurt my feet , I have plantar faciitis in my right foot and they are the only insoles that don't totally kill my feet .
[mu8v21w] (score 2, diepte 0) Before joining Tom I would just wear my comfy regular shoes and bought my own steel toe covers.

https://a.co/d/eHNAE1C

You just need to get safety/LP to sticker them so they know you aren't stealing them.
[mu8wrjz] (score 2, diepte 0) They are terrible, they make your feet so hot. I do not recommend
[mua8rv3] (score 2, diepte 0) those protalus ones are good 

https://preview.redd.it/9a538x32q13f1.png?width=463&format=png&auto=webp&s=80b5c7a820a398c97cf31b76853796f3072e5680
[mu86asr] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.com/invite/t7jARCs) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[mubvvha] (score 1, diepte 2) Maybe he meant that he started using them.  Not that he has actually worn them for two years.
[mud99d7] (score 1, diepte 3) Yeah, I hope that's the case. 😂
[mu9l5sv] (score 1, diepte 2) Amazon owns Zappos. So yeah lol
[mu9smfu] (score 1, diepte 1 OP) LMFAO
[mu8f5lo] (score 1, diepte 0) They're free so yes...
(No they're trash)
[mu8l8na] (score 1, diepte 0) I absolutely hate them. They are hard af. I prefer the ones they had in the machines before, so I just buy my own
[mu8mnbh] (score 1, diepte 0) Just get em and try it urself. It's free. Some ppl like then some ppl don't
[mu8p840] (score 1, diepte 0) About to get my 3rd. I “use” then by putting them in one of my old shoes that are completely worn out, then I go walking for a couple hours and add them to my rotation
[mu8qv91] (score 1, diepte 0) I didn't trust them, so I got the compression socks instead. Idk if it works, but my feet do hurt less
[mu8rxg7] (score 1, diepte 0) Find the insoles that work for YOUR feet. Everyone complaining didn’t do their research. I’m flat footed and I never had a problem with the ones I bought.
[mu8slwf] (score 1, diepte 0) Free is free.. but yes they do suck
[mu8tumw] (score 1, diepte 0) Yes and yes
[mu8u85a] (score 1, diepte 0) I can't even figure out how to order them
[mu8un2m] (score 1, diepte 0) i have flatter feet so they make me feel like i'm waking on concrete barefoot😭 literally went into the bathroom and chucked them 😭
[mu8uqoi] (score 1, diepte 0) I do they were fine for me. My shoes had 0 support.
[mu8wgxh] (score 1, diepte 0) They’re crap, but I still order them and pitch them in the garbage. It’s my way of saying fu to Amazon lol
[mu8yjz6] (score 1, diepte 0) I do, but honestly don’t feel any difference
[mu8zysm] (score 1, diepte 0) I genuinely have been using the protalus green inserts since like 2015 long before I worked at Amazon.  Here's the thing: the green ones are specifically designed to protect medium to high arches.  There are other colors for different types of foot shape and different foot support.  So it's wild to me that Amazon/Zappos seemingly only offers one specific type of protalus for free.
[mu90o2l] (score 1, diepte 0) They tore the living daylights out of the edges of my heal and the sides of my big toe. They suck.
[mu90rva] (score 1, diepte 0) It depends who orders them. People who care order the good ones.
[mu90x8e] (score 1, diepte 0) Our safety lead gave us Dr. Sholls insoles but I haven't put them in yet cuz they are too long for my shoe and he told me I had to trim them down
[mu916do] (score 1, diepte 0) They didn’t last too long
[mu9a8v6] (score 1, diepte 0) A lot of the safety shoe options litterally have like attached insoles so I couldn’t even fit them in my shoe and I wasn’t going to rip out the bottom of my shoe lol
[mu9ablo] (score 1, diepte 0) I got some that were supposed to fit a 10 sized shoe. They would barely go in and then my foot didn’t fit inside the shoe. It felt like they needed to me like 4 sizes smaller
[mu9bk60] (score 1, diepte 0) I have Planters I use them they are extremely good in my boots.
[mu9d7bb] (score 1, diepte 0) I was recommended to try akusoli insoles. I haven’t got any yet but I hear they’re better than the free ones.
[mu9es6z] (score 1, diepte 0) Used them for about 3 months, but because of how thick the insole is with the hard plastic bottom, they caused bruising on both big toes. Took about 9 months for the bruising to go away. I wouldn't recommend them if your boots or shoes don't have much room in the toe cap.
[mu9eukc] (score 1, diepte 0) It took me a week to break them in and wearing them everyday for several months. I got new shoes and they were awful in them so I quit wearing them. Now if I try to wear them in my other shoes they hurt my feet so bad because I probably need to break them in again.
[mu9f0sn] (score 1, diepte 0) They're better than the paper thin doctor shol's ones
[mu9fcp6] (score 1, diepte 0) I hated them. They're hard as rocks, and sometimes, I wanted to cry from the pain. I tried a different set, and they're a ton better, plus, they're cheaper. They advertised on Facebook, so I was skeptical, but they live up to the hype. They're called cloudsoles
[mu9h9vk] (score 1, diepte 0) I have two pairs and they are just sitting in the box 🤷🏻‍♂️
[mu9l6vk] (score 1, diepte 0) I personally think they made things worse for me and gave me blisters
[mu9ogww] (score 1, diepte 0) I didn't know we get free insoles. None of the work shoes available fit my unfortunately wide as fuck feet, so I had to buy my own work boots out of pocket.
[mu9p81u] (score 1, diepte 0) I just bought my own good ones because we are on our feet all day
[mua099h] (score 1, diepte 0) Honestly yes cause I was cursed w no arches.
[mua6ite] (score 1, diepte 0) Couldn’t tell the difference
[mubwhpf] (score 1, diepte 1) Yeah I have them and they're actually good and came free 😁. Like they're supposed to be.
[muagd8h] (score 1, diepte 0) Honestly not too bad, and ive got mega arches. I still use those "custom" dr sholl's ones. Everyone says theyre a scam, but they are the only ones with enough support for my diva ass feet.
[mub8l90] (score 1, diepte 0) Fire at my feet
[mud4bqi] (score 1, diepte 0) I just spend the money on functional insoles.

Find out your arch type then buy the right insole.  Just grabbing anything off the shelf doesn't work
[n2sspuh] (score 1, diepte 0) the $65 free insoles do not work for me well
[mu8s19w] (score 0, diepte 1) You mean discounted lol
[mu8skp7] (score 0, diepte 0) They are not comfortable for me.  I'd rather spend extra and buy quality ones from Amazon
[mu90ch2] (score 0, diepte 0) Honestly they're Hella uncomfortable but what did you expect from a tax write off... 🤷‍♀️
[mu95sir] (score 0, diepte 0) they are useless, i swear it’s some kind of fraud deal amazon has. lmaoo

=== THREAD 78a49w ===
SUBREDDIT: r/army
DATUM: 2017-10-23  SCORE: 183  REACTIES: 61
TITEL: You guys gotta go invest in some good PT shoes.
POST (source_id=post):
I hated running, partially because it hurt so damn much. I was in the market for some new shoes after wearing my last pair for a solid year plus. I decided to drop the cash to get some good, high quality shoes.

I went to a specialty running shoe store. They tested my feet by where I rest on them and then they recorded my feet running on a treadmill. I had always thought of myself with flat feet and ran on the outer edges of my feet. Turns out I've actually been over pronating like crazy for years and have a normal arch. So I asked the guy for some top of the line shoes to correct this. I trusted him, tested out Brooks and Asics and Saucony and went with the Brooks Adrenaline GTS. I also bought some real nice moisture wicking socks, and some bungee laces (one of the GOAT inventions).

Holy shit. It's life changing. I went on a test run on a tank trail that was supposed to be two miles but turned into five. My knees felt great. My pinky toenail wasn't black. I *enjoyed my run*.

That was about two months ago. I haven't stopped. I've actually upped my running to 20 miles a week from 10. I run on my lunches or after work. I fucking love it. And did I mention my run time? Down two and a half minutes. I'm down 12 pounds, quit smoking, just happier and healthier all around.

I've been going back to the store more. I signed up for a weekend running club and I'm hiring a running coach to help on my form and build a half marathon program so I can target a 1:30-1:45.

Guys, go do it. Don't buy some cheap off brand shoes. Don't buy some bullshit flashy nikes. Don't even settle for the first pair of Asics you see. Get properly fitted, tested, talk to a proper salesman that could damn near BQ in their sleep. You'll thank me later.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dos75la] (score 188, diepte 0) I try to tell people this all the time. 

"But $120 is so much to spend on tennis shoes". Bitch I watched you drop $200 at the bar yesterday, sit down and take care of your body for once.
[dosb4ix] (score 83, diepte 1) I'm taking care of my body by feeding it the beer carbs it needs for all the stupid running.
[doscawy] (score 56, diepte 0) > quit smoking

something tells me that had more of an impact on your run time than the type of shoes you wore
[dosdmrq] (score 31, diepte 2) I also need to eat a large pizza and 12 wings to ensure my body is fueled for the grueling pt I have to do.


I lied I’m stationed at Fort Couch. I don’t PT.
[dosbxah] (score 17, diepte 0) This is a lesson I learned the hard way too. While I always bought "decent" shoes (nikes, etc), I wore them far too long and ended up with some really terrible shin splints. It wasn't till I finally sucked it up and bought new shoes that they got better and eventually went away. I ended up having to replace my shoes every 2-3 months and I could always tell when I was due because my shins would start flaring up again. 

So it's not only important to buy good shoes, but to also replace them periodically.
[dosecjz] (score 16, diepte 2) Yissss. Though I will say your heel probably should touch the ground when not sprinting. Just, at the same time as the midfoot instead of first. Keeps momentum better. 

But yes form is such a big issue that I see. People are just killing themselves struggling against their own body. 

Shoes, form, and pacing are 90% of the issues I see when people have slower two milers than I would expect.
[dosk9xl] (score 15, diepte 3) Fort Couch has the best on post strip club this side of the Atlantic. *Results may very*
[dosdyrz] (score 14, diepte 0) LPT:  if you have the correct shoes but running is still giving you problems, get a referral to your posts physically therapy office and talk to them about getting orthotics. They'll fit you for custom orthotics fo freeee
[dosjo8x] (score 13, diepte 0) Til hate running = 10 miles / week
[dosi2dj] (score 12, diepte 1) There was a period of time where a couple guys in our platoon had 2nd jobs at a shoe/athletics store so the platoon got nice discounts on new shoes.  I got mine for $20.
[dosca25] (score 9, diepte 0) I wear retro style Saucony Jazz’s because not looking like a retro cool kid would make me die
[dosezhd] (score 8, diepte 4) I think you'd be surprised if you filmed yourself running (in the middle of a long run, not the quick sprints they do for gait analysis). It's pretty rare to do forefoot strike for long distances. 

But you might be one of those, idk. If it works for you it works for you.
[dosap3n] (score 8, diepte 0) Brooks Launch 3's are the shit. About 70$ a pair.
[dosra29] (score 8, diepte 1) Smoking will hurt the lung capacity but shoes will affect everything about the stride, foot strike, knees, ankles, etc.
[dosdz2s] (score 8, diepte 1) Recommending just one shoe is a waste of time and money. Different people have different preferences and form. 

Most local small business running stores offer free gait analysis nowadays. Shit most of them I've been to even have knowledge of the shoes they don't carry and offer to order them for you if none of the ones in store are a good fit.
[dosxzvx] (score 7, diepte 2) You could have gotten them for $0 through theft
[dosd1eb] (score 7, diepte 1) I can usually extend the life of my running shoes by switching out the insoles. I got one of my pairs to 3400 miles like that.

I don't recommend going that far but it might be an option if you want expensive shoes but don't want to keep replacing them. I used to get mine custom made at Road Runner Sports for like $50-60, but off the shelf options have worked too now that I'm away from any RRS.
[dossgnd] (score 6, diepte 1) A lot of runners loathe themselves. 


Am runner.
[dosox6l] (score 5, diepte 8) It's not so much not landing on your heel, although a mid foot to forefoot strike is preferred, but what's more important is making sure that when your foot does strike the ground that it's under your body, not stretched out in front of you.  That is when heel striking will give that braking effect and fuck up you ankles, knees, and hips.
[dosqs3f] (score 5, diepte 1) My husbands favorite shoe.

I will say though that sauconys were some of the best running shoes I’ve had
[dosmdb1] (score 5, diepte 1) I've been saying that for years. I like Salomon trail running shoes for pt, and I've got a pair of Merrells I wear in uniform right now. My feet love it.
[dosjljx] (score 4, diepte 1) 4s are out. Don't think they changed much other than the upper
[dotcmkt] (score 3, diepte 9) http://northstatecrossfit.com/wp-content/uploads/2017/02/pose-stride-pjm.jpg

I remembered it wrong, it's not a mid foot strike, Pose is what I was thinking of. So you're doing it correctly for long distances.
[dosir66] (score 3, diepte 3) Whenever I felt the shoe breaking down. For lack of better description, when it felt like I was beating pavement instead of running and my ankles would start to get sore. For *me* personally it usually ends up being around 1000 miles but Im more on the extreme end, most people I know usually have to change shoes/insoles around 300-400.

It also really depends on the quality of shoe. The ones I had that lasted 3400 were great (some old Mizuno model I can't remember the name of) and I've had trouble getting anywhere near that with any of my new shoes. Build quality just isn't the same. My current ones have *maybe* 1000 miles on them and I'm honestly probably gonna just buy new shoes soon, cause the shoe itself is so broken down it's not worth salvaging.

It also very much depends on your own personal level of injury tolerance. My husband, for instance, is suuuuuuper prone to shin splints and the insole trick has never worked for him.
[dosj7jo] (score 3, diepte 5) Well I'm a princess when it comes to shoes meant to do work and my running shoes are generally $120-150 so...it takes a while for me lol. I usually get a good year or two out of them.
[dosdm5o] (score 3, diepte 0) I cant believe how many people dont get good shoes.  I became a geek when it comes to running shoes.  I love finding new ones that work well.

Id recommend the altra escalante for most people (EDIT: to try.  If your local store carries it check it out).  It has zero drop from heel to toe, which helps you run more mid foot. takes some getting used to.  The main thing is the lightness, the great cushioning for how little material is actually there, the upper material which just feels like wearing a sock, and the fact that its shaped like an actual foot so your toes are not being pinched in any way at all. seriously its like wearing a sock.  just dont do sprints in them.

https://www.altrarunning.com/men/escalante


I used to love saucony shoes.  This years iteration is really nice.  Problem is I went through 3 of them in 6 months.  The outer sole kept falling apart after less than 100 miles.  Brooks are seriously hit or miss depending on the model.  Hoka One One are really great depending on the model also.  Probably my second favorite shoe right now.
[dospqgp] (score 3, diepte 1) Why bother when u gon die?
[dossz4o] (score 3, diepte 0) I buy whatever is on the PX shoe clearance rack for PT
[dot1qb7] (score 2, diepte 7) Lean forward, push your chest out a little and keep your back straight. Basically it's gonna feel like you're falling forward and it's gonna help with hitting midfoot. I find it nearly impossible to do on a treadmill without smacking into the bar.
[dotcg59] (score 2, diepte 8) Maybe I do it already, but I'm almost positive that I roll my heel to toe because I stride as far as people whom are six feet tall. It's not like I run slow or this would improve my run time though. I just focus on falling forward, swing my arms, breathe, and pick my knees up as far as I can to swing my feet out.
[dostl8s] (score 2, diepte 1) not to mention probably 300 on a pair of white jordans.
[dosiwo3] (score 2, diepte 4) I guess I'm coming from a cost/benefit analysis side. At some point it would have been cost effective to get new shoes compared to insoles though, right? And 3k miles is insane!  Mine do usually get replaced around 500 or so.
[dosee0r] (score 2, diepte 2) I agree with what you are saying with some caveats

The problem I have with gait analysis is most stores will tell you "oh you have some pronation you need support shoes" when pretty much everyone has some level of that.  I think a lot of stores are really just not educated enough on what kind of shoe is best for the customer.

I had gait analysis done, ran with support shoes, and got injured.  I switched to neutral shoes and the pain is gone after 2 weeks.  Im not saying this is what happens to everyone or even most people but that's just my experience.

Im also just recommending that shoe as one to try on in a store, because its a seriously cool and comfortable shoe.  Should always take shoes for a test run before you buy
[doshjqc] (score 2, diepte 0) Can confirm: I run/ran cross country. Properly fitted shoes help avoid shin splints and other injuries. And they overall just feel better.
[dosjd85] (score 2, diepte 0) Things like this should be common knowledge. 

Treat anything that separates you from the ground like an investment. 
So shoes/boots, mattress, tires.
 you get the point. 

Garmont T8 boots, Red Wing boots and a good pair of Asics running shoes for me. 
Ironically for daily casual wear/lifting my feet tend to like cheap Converse more.
[dotkbhz] (score 2, diepte 0) I realize this is not going to be a viable solution for the majority of r/army, but my solution to my hatred of running is not running.  I run a couple times a week for the month leading up to the PT test so I can make sure I've got some good cushion on my time, then slog through the test and blow off running for another 5 months.

I love going to the gym and lifting, and I even make sure to incorporate pushups and situps into my daily routine.  But fuck running.

One of the perks of being a perennial staff officer, I guess.
[doskczg] (score 1, diepte 6) I'm confused by this whole thing you have going on here...

  Yes I do not run with my heel when sprinting, but I cannot sprint 2 miles. I run pretty much rolling from my heel to toe. The biggest thing is just getting people to pick their knees up and make a longer stride.

  How the fuck do you run 2 miles without your heels? I run in 11:38-12:20s and not using your heel sounds like you'd die.
[dosfv2f] (score 1, diepte 2) Since when? Somebody has been lying to me.
[dosl3lb] (score 1, diepte 4) We might have known pointy was good before we were us.

Homo Sapiens wasn't the first to use weapons.
[doswcia] (score 1, diepte 2) > my 2mil dropped from 15:25 to 13:05

Holy shit!
[douhdgx] (score 1, diepte 4) If you watch a highlight reel of fast marathon finisher's, you'll see a wide diversity of foot strike patterns. Most heel strikers have their foot strike the ground forward of their center of mass, and that's where the problem lies. You can strike with the heel first, as long as your foot makes contact when it is below your center of mass. There are a lot of good pictures and videos that explain it if how I word it doesn't make sense.
[dos99w1] (score 1, diepte 0) Yeah I got some asics. Been walking around with them, i rotate out to in with my feet when I run 

$70 but I can run well now
[dos9mf3] (score 1, diepte 0) Word
[dosk23z] (score 1, diepte 1) I’m all about the 1s, but they’re hard to find now. The 4s aren’t bad at all either.
[dosi5uf] (score 1, diepte 2) How often did you change insoles?
[dosu5pp] (score 1, diepte 2) Damn right.  Made in America too.  I ran in New Balance 992's for years, but you can buy Saucony's off Amazon for a third of the price and look twice as stylish!  

Trust me, the bright ass sneakers or gasp, the running shoes from Basic Training, are the athletic equivalent of wearing a Grunt Style t-shirt to a unit function
[dot23j2] (score 1, diepte 2) As if you're making the argument that better shoes are a better solution to someone's running time than the cancer sticks
[dotoa68] (score 1, diepte 3) It would be less painful
[dosemz8] (score 1, diepte 3) Ah yah I guess there are some stores out there where their employees don't know much. I guess I've been lucky.

Fleet Feet affiliated stores have always been good to me and the people I recommend to them.
[dot1tif] (score 1, diepte 1) My old LT was like "I don't want to see any of you wearing shitty shoes and then complain about how much your ankles hurt."

Yeah
[dosjmv4] (score 1, diepte 0) is there any one of those stores near hood?
[dosld4q] (score 1, diepte 0) Well, perfect timing seeing this post. I went for a long run today with my worn out, under armor, clearance shoes and my knee did not want me to finish. Now it’s throbbing. I think you’ve convinced me to see a specialist.
[dosmoke] (score 1, diepte 0) I’m a mizuno fan.
[dosr7mp] (score 1, diepte 0) Shoes are important. Glad your running. Check out r/running for stories, advice, and stuff
[dosr8f4] (score 1, diepte 0) Just got a pair of Brooks: Beast 16s. The sole is 2" thick and they're kinda heavy, but I'm flat footed like a motherfucker. Support is everything.
[dosz7rl] (score 1, diepte 0) Any good stores like these near Carson?
[dot9dqg] (score 1, diepte 0) Incredibly important. I had a soldier that had a huge issue running when I got to the unit, first thing I checked was his shoes... same ones they made him buy in basic.
[dota8qj] (score 1, diepte 0) This post influenced to buy me a new pair.

Thanks OP
[dotahsc] (score 1, diepte 0) Yup.  I DO have flat feet, like so flat on my West Point physical it almost dq’ed me and my mom took me to a running store for my running shoes for inserts and shoes.  Life changing.
[dotfyik] (score 1, diepte 0) Run the grass on the side of the road.  Don't have to replace my shoes nearly as often due to the natural padding.  Probably slows you down a little, but it really helps with that feeling that you are just smacking the pavement with your shins/knees.
[dotqa2v] (score -1, diepte 1) Bro this comment is fucking gold. A+

