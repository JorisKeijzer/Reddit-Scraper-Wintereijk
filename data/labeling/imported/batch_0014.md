# Label-batch batch_0014

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
Schrijf het resultaat naar `batch_0014.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 2tbby9, 1c6rpth, 192s4jz).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 2tbby9 ===
SUBREDDIT: r/ChronicPain
DATUM: 2015-01-22  SCORE: 2  REACTIES: 38
TITEL: Anyone else with chronic foot pain? My doctors are saying there's nothing else to try.
POST (source_id=post):
I've been dealing with debilitating foot issues and pain for the past two and a half years. I had no initial trauma or injury, and I'm not an athlete. I've run through the gamut of treatments and seen a handful of different doctors with different diagnoses. When I first started experiencing it I was diagnosed with tarsal tunnel syndrome and given hard orthotics and three steroid injections into my fourth metatarsal area for a possible neuroma. These things did not help. 
My second podiatrist diagnosed me with myofasciitis, plantar fasciitis, and cuboid syndrome. Treatments included new orthotics, physical therapy, night splints (3 different kinds - traditional boots, straussburg socks, and dynasplint), shockwave therapy (causing microtrauma to induce healing), dry needling (to get muscles to relax), massage, oral steroids, chiropractor to adjust foot bones, and the latest is that I've spent the past six weeks in an air boot and crutches to stay off my feet. 
Nothing has helped and I am not a candidate for surgery because releasing the fascia in my plantar area would increase the mechanical load on the lateral fascia and irritate my cuboid area. I've had a regular checkup and bloodwork is all fine, even worked with a nutritionist to see if there was anything I could do to help my body heal. I can't really function with this pain because standing and walking sometimes bring me to the point of tears. My doctors have said they don't know what else to do. I don't know what to do.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cnxkwj6] (score 4, diepte 0) Just wondering what scans and things you have had?
Also, foot problems not from trauma can be notoriously difficult to treat because they are often caused from a lifetime of poor biomechanics and constant loading. This means that anything you do try you need to give a long time (and be really contentious with) to see if it does work. I'm not saying you haven't, just can't tell from your post so wanted to check. A lot of docs will try something for 1-2 months and then give up if you haven't noticed a change. 
Also have they actually given you a diagnosis or are just trying different things?
[cnxhlqd] (score 3, diepte 0) Have you tried Indocid (generic: Indomethacin)? It is an anti-inflammatory NSAID that I have used for over 30 years for my various types of arthritis. Without it, I would be in constant agony, and would be barely able to move. Ask you doctor if you haven't already tried it.
[cnxtd6e] (score 3, diepte 1) if your problem is plantar fasciitis you may find this site helpful:  
http://www.plantar-fasciitis.org/

the things they recommend that helped me the most were:

keep sandals with support by the bed and never walk barefoot ( except the shower)

Ice the foot -- rolling Ice treatment ( frozen bottle) even better

the towel stretch --use a rolled up towel or something like it to pull back on the area below the toes to stretch the plantar fasc. muscle -- repeat several times a day -- It can take many weeks to help --keep at it!

I am just finally recovering from an 18 month bout of p.f. that returned with a vengance after being "cured" for the past 10 years.

~~~~~~~~~~~~~~~~~~~ edit

I just read the rest of your comments below and the "hurts most when off the feet" is not consistant with my experience with p.f. -- I also have very arthritic feet, I learned that after an X ray for a suspected broken toe.  Not much to do it seems except lose weight.  Tumeric , MSM, glucosamine, Chondroitan (sp?) are all said to help -- i take them all, but no miracle in them for me.  good luck, foot pain sucks!

~~~~~~~~~~~~~~~~~ another edit

If you try the towel foot stretch it may be diagnostic for the plantar fasciitis. You really feel the problem ( the heelspur and muscle spasm) when you do this stretch
[cnxhq97] (score 2, diepte 1 OP) I haven't heard of it. I think that since I didn't respond to steroids, they are thinking it's not an inflammatory issue. I've had regular NSAIDs and even tried Vicodin for the pain and nothing has touched it.
[cnxirdi] (score 2, diepte 3 OP) Thank you - I will ask about it. I am very much of the mindset that I will try anything and everything.
[cnxjfmw] (score 2, diepte 5 OP) That would be amazing. Sleep can be very uncomfortable with the night splints.
[l21ccr5] (score 2, diepte 5 OP) It's kind of hard to describe after all this time, but it starts in the center of my heels, then moves up through the arch. When it gets really bad it will also move up my calves. I just walked three blocks tonight, and when I got home my feet felt hot and tingly, for a long time after I sat down and got off my feet. It aches and can feel like I've been standing for 12 hours after just 10 minutes. It feels like I am standing on the bone, it's a constant pain that can feel like both nerve and muscle pain. The aches can last for hours, and if I do too much one day, the next few days my pain is higher and I am more sore. Not sure if that helps?
[cnxmoow] (score 2, diepte 0) My feet have hurt for more than a year. I've never seen a doctor about it. I've tried various shoe inserts and orthotics, etc., and none of that helped at all.

I'm on my feet a lot, in a garage setting, on a concrete slab. I've destroyed them and it's pain 24/7. I wear multiple pairs of socks with sandals. Walking around in just shoes with one pair of socks is quite painful and I only do that when I have to.

I lost about 20 pounds and that didn't help. I'm not sure what I can do about it.
[cnxmse0] (score 2, diepte 1 OP) Definitely see a podiatrist - there are options at least depending on what's causing your pain. How do you cope with the constant pain?
[cnxqxlr] (score 2, diepte 7 OP) The pessimism is par for the course with pain. I struggle with it too. That's what prompted me to post at all, that maybe someone has something to say or suggest that is different because I feel like I've tried everything.
[cny3xvv] (score 2, diepte 8) Thanks for posting. This subject matter is why I subscribe to this subreddit.
[cnynh2x] (score 2, diepte 0) They're sure it's not peripheral nerve pain from your back?
[cnyuhfq] (score 2, diepte 0) I have had chronic foot and ankle pain, left and right, my entire life. I really do understand what you are going through. Walking is excruciating. For the longest time I thought it was normal to hurt while walking or running and since no one ever complained about it, that I was just weak. Turns out that I was born with congenital deformation in both feet/ankles. I have developed tendonitis and arthritis. I have really weak ankles and I fall ALL OF THE TIME because my ankles just give out. It's pretty awful. 

My podiatrist said that I probably need surgery, but that had to be put on hold because I had to get back surgery first. I've tried inserts, NSAIDs, ankle braces, narcotics, heat, ice, etc. I also had steroid injection, but am extremely allergic so that's a never again thing.

Anyway, you are not alone. I wish I could think of something that would help you, but other than surgery, I'm in the same boat.
[cnz8q89] (score 2, diepte 0) I've had plantar fasciitis, at least twice, but it looks like you're getting way more treatment, and the other comments seem to be covering everything possible.
[cnzvran] (score 2, diepte 1 OP) Thanks for replying anyway!
[co19q9f] (score 2, diepte 0) You need a second opinion and a new doctor.  Have you ever gotten a Nerve Conduction test to evaluate if you have Tarsal Tunnel, or an MRI to get a definitive diagnosis
[cocdgtf] (score 2, diepte 0) My professional advice as a footwear and orthotic specialist:

The simplest thing you can do is get professionally measured and fitted at a reputable shoe store. Start with ANY shoe in the correct size. There's a 75% chance that you are wearing the wrong size. Try something simple: a running or walking shoe with a generous toebox, and add a gentle arch support, like a Pedag Viva. Human bodies need arch support in the concrete jungle, period. It may not be a miracle cure, but it'll help at least a little.

Follow all the standard plantar fasciitis advice: no bare feet, good supportive slippers or your shoes around the house, stretching.

Go see a massage therapist. Get an hour or two strictly from the waist down, particularly your calves, and on a regular basis.

Start yoga. Downward facing dog is great for such issues.

If you're in a large enough city that has any pro sports teams, or a significant college sports environment, find out which orthopedic team sees the athletes, and go see them. Not sure whether you have actual fasciitis, but it's a more and more common reason for pro athletes to go on the injured list, and their doctors are motivated to get them ready for gametime again quickly. If you were here, Portland, I'd send you to Rebound Orthopedic, who treats the Trail Blazers. Whatever it is, I'm guessing that a sports medicine-focused group could be of some assistance.

Best of luck.
[cr8t2m1] (score 2, diepte 0) you need to have an MRI or Nerve Conduction Test to find out specifically what you have

http://podpost.us/issue/february-2013/article/tarsal-tunnel-the-five-best-treatments
[l7y5zix] (score 2, diepte 0) Hey if you check out my chronic foot pain post, i am in a very similar situation to you, have seen every specialist and had every test and procedure and still no diagnosis. My doctors and people that I’ve seen have also been baffled.
[cnxii6e] (score 1, diepte 2) It might be worth a try. Ask your doctor about it. 

My arthritis started when I was 11 (50 now) so I went through a whole range of treatments as well, including steroids and gold injections, yet this medicine was the only thing that seemed to control it enough for me to function 'normally'. My wife also uses it for any flair-up of the gout in her feet (prescribed by her doc). I've been advised many times by doctors to try something more modern, but it terrifies me because I don't want that pain back in my life while in transition. Warning: it is very hard on the stomach but if you eat when you take it and drink milk constantly, it shouldn't be a problem. 

I hope you can find a way to deal with this. Good luck and be well.
[cnxj6kk] (score 1, diepte 4) One more warning: it will knock you out within 30m. 

I have given out samples to other people to control pain from broken bones, bad backs, toothaches, etc. Never more than 1-2 pills, just to help. But, in every instance, they tell me they are out in short order, they get a very deep, satisfying sleep from it, and wake up feeling much better. I hope this is what happens if you get a chance to try it.
[cnxl3al] (score 1, diepte 1 OP) Good question, sorry I didn't mention it. I had MRIs and three different sets of Xrays. They found the cuboid bone issues through ultrasound. When the Dr. saw my bone he said it was sharper and lower than most people, and it was irritating the fascia. They hoped the chiropractic adjustments could move the bone upward, and then have it be supported by my orthotics to stay up. The bone did not look displaced on any of the xrays, and a couple months of chiropractic adjustments did not help. I'm going for a second opinion soon. I have been off my feet as much as possible for the past month and a half to see if the boot cast helps. Since my symptoms just started one day and seem to have changed a little over time, it's hard to find a definitive diagnosis. Myofasciits, plantar fasciitis, and cuboid syndrome are the latest diagnoses.
[kshw7p8] (score 1, diepte 2) Did you ever find a resolution to this?
[kskvm3w] (score 1, diepte 3 OP) Sadly, no - still here over ten years later with the same exact pain. I've tried more things, but nothing has worked. Wish I had better news!
[kszydf7] (score 1, diepte 4) Hello, brother.


Read the book Healing and Recovery by David Hawkins, it could be what you need.


Cheers!
[l211cfe] (score 1, diepte 4) I can possibly help you, can you describe how your foot pain feels to me?
[l21g8qr] (score 1, diepte 6) Your pain sounds extremely similar to what I dealt with for the last 9 years,  you can see my descriptions in previous postings as well.  I have good news and bad news.  My pain disappeared completely overnight 4/24 and as of 4/30 still pain free aside from trying to build the muscle back in my feet from all these years of sitting…there was no gradual getting better it was Instant!  The bad news now is that I have been strengthen my core for the last 6 months very disciplined.  I can’t say 100% this was the cause that made me feel better but I am not sure what else could’ve made it magically disappear.  It seems as if I had a nerve stuck in my back that was producing pain in the feet and it somehow got free’d.  I would be more than happy to share the routine if you’d want to give it a shot.  I really think you could benefit and we have had this pain for about the same amount of time so I have a pretty good idea how many times you’ve heard that ;)
[mp5rfs1] (score 1, diepte 7) How are we doing a year later? Did the core strength help?
[mploa5c] (score 1, diepte 8) It significantly helped with low back pain, a ways to go from perfect but completely worth it.  My feet pain regressed a little over a month after that post.  They also are still better than before but nothing like that year ago mark..  I may have tried to get too active too fast and retriggered but honestly no clue :( I took the last few months off my core exercises, but plan starting up again soon.
[no43i5j] (score 1, diepte 7) I have very similar sounding foot pain since two years and would love to hear your routine for the core. Thank you so much!
[no6whhm] (score 1, diepte 8) Hello friend, sorry to hear ya going through it.  I will say what I did for core, but my foot pain did end up coming back, I had a solid month or so where it had completely vanished! Such is life!  Anyways work up to as needed but I did:
1 set
50 birddogs (left and right count as 1)
50 dead bugs
50 glute bridges
50 side plank hip dips
20 Mackenzie method
20 supermans 
Wall sits as long as you can I got up to around 4 min
band work 2 sets:
10 Clam shell 
10 sideline glute kick backs
10 sideline toe taps 

Kinda realizing you’d probably have to look these up to get a visual if you have questions on any I can try to describe,  I did these 5-6 days a week for around a year but started seeing huge improvements in my lower back after about 3 months… to this day I am not sure of the feet temporarily healing was related or what… I personally believe I have a trapped nerve in my lower back that is effecting my feet.  Again I really hope any of this can help you or anyone else! Good luck!
[np0kinz] (score 1, diepte 9) So sorry to hear that it came back. Your story was kind of my ray of hope. Maybe one day we’ll get better still ♥️ 
Random question: you don’t by any chance have endometriosis? Because I do and I was wondering if there could be any relations. 
All the best and thank you for your long answer!
[lo2jwbz] (score 1, diepte 6) I have also had constant pain for 3 years. Its gradually become worse since I started seeing doctors for it 10 years ago. I have no diagnosis, but I have also done every single test you mentioned and a few more. Its so defeating. Do you have any advice for how to live life in such dependence and confusion?
[l69d57y] (score 1, diepte 4) Are you a smoker or use nicotine?
[l69f1jy] (score 1, diepte 5 OP) Nope, never have - what makes you ask?
[l69vzwk] (score 1, diepte 6) Because I've had foot pain in the metatarsal area of my right foot and I'm hoping the pain was caused by the nicotine gum I bought around the same time the foot pain started. If not, I would just have random foot pain for no reason. I do have Crohn's though. Could just be more inflammatory noise in my body. :(
[l6eee7f] (score 1, diepte 6) Never mind. It looks like it's just my monthly PMS completely random symptomatic pain. :(
[cnxnc45] (score 1, diepte 2) I can't afford doctors. I have a few other chronic pain problems I deal with. I'm not sure what my coping mechanism is, to be honest. Seems like I've had it for so long I can tune it out somewhat. But I try to stay off my feet as much as possible. Funny thing is they hurt worse when I'm not on them. They pretty much throb with pain when I'm laying down.

Soaking them in hot water and epsom salt offers relief, but it's only for about ten minutes.
[cnxnjb2] (score 1, diepte 3 OP) Some doctors offer reduced fees or even pro bono work for clients who cannot afford visits. Or there might be a clinic associated with a university that sees patients for very low cost to free, because the students are learning and are supervised. If it's something like peripheral neuropathy, that can be treated with medication (that you can also get for very low cost by participating in their medication assistance programs). It's worth looking into, because living with pain impacts so much of our life.
[cnxnmkt] (score 1, diepte 4) I'll look into it. I just stopped caring about things ultimately some years ago, so I don't bother seeking help too often.
[cnxo5k7] (score 1, diepte 5 OP) That apathy and depression are definitely part of dealing with chronic pain. It's at least worth spending time searching on Google and making a few phone calls or email inquiries. Even if you have to work up the energy to make a phone call, it's movement forward in taking care of yourself. I have to say the same things to myself.
[cnxofkp] (score 1, diepte 6) Thanks. I've done a lot of googling and tried a lot of things. Rolling my feet nightly on a frozen water bottle, going barefoot, soaking them, different kinds of shoes and inserts. Everything I've tried was of no help. Sorry for sounding so defeatist, I'm a bit overly so because I'm drowsy. I've had numerous chronic pains for about three years though, and I've gotten used to it I guess.
[cny3xbk] (score 1, diepte 2) Thanks very much.

I always wear sandals when I'm on my feet, because I wear 4 pairs of socks at a time. I've worn them out and need new ones though. All the weight I lost, a gained back, and I'm starting over with that. And I do need to get back into nightly frozen water bottles.

I hear taking breaks and elevating your feet helps also.
[cnyqymz] (score 1, diepte 1 OP) Yes I've had no back issues at all and Xrays look clean. My pains also aren't burning or nerve-type pain. It's frustrating not having a clear cause!
[ka7z5f2] (score 1, diepte 2) Nerve pain is weird though. I had ankle pain misdiagnosed as Peroneal tendonitis that turned out to be sciatica. No pain up the chain, just a pinched nerve in the sciatic nerve chain that improved drastically with nerve flossing
[cnzvti1] (score 1, diepte 1 OP) Thanks for saying this. It gets really lonely, because I'm young (31) and everyone I know is off living their lives without any issues. How do you function (ie grocery shopping, cooking, chores, commuting, even standing in the shower)? That's the part that really gets me down. Right now I am using a walker to sit and roll around the house and kneel when I need to cook or wash dishes or something. It's gotta be scary to fall all the time :/
[cobv83m] (score 1, diepte 2) I'm sorry I'm just now seeing your reply. 

I'm lucky that I have my husband to help me, but there are times when I'm alone and I've literally had to crawl to get around the house. I have a walker from my back surgery, and I admit that I've used it a few times because of my feet. 

I have this fear that I'll have a really bad fall down the stairs when no one is home and that I'll just have to lie there for hours. 

Mostly, I just have to take it slow and be very careful.
(20 reacties met lagere score weggelaten)

=== THREAD 1c6rpth ===
SUBREDDIT: r/ChronicPain
DATUM: 2024-04-18  SCORE: 141  REACTIES: 38
TITEL: Angry at my parents for ignoring a completely avoidable deformation of my legs and feet as a child that has caused full body pain that is now disrupting my life
POST (source_id=post):
When I was a child my parents made notice of the fact that I had flat feet that were pigeon toed (feet that go out).

They still forced me to do sports I didn’t like because it hurt to do, they called me lazy if I didn’t want to do it or otherwise belittled me and made it seem like it was purely just me being an asshole or having the wrong mentality about it. 

Come highschool PE class time I am ready to kill myself due to the constant pain and feeling like nobody is listening. 

I get in trouble with the PE teacher and get suspended for like a week and finally when it becomes inconvenient to my parents, at the recommendation of the school, they take me to an actual foot doctor for the FIRST TIME EVER. 

The doctor doesn’t even sugar coat it, I’m like 15 at the time and he said he didn’t know how much good he could really do beyond some custom orthotics that might be able to reduce the stress in some of the points but won’t be able to help correct anything anymore since my bones are so fully deformed by that point. 

If I put my feet together straight like they’re meant to be, my legs bow and with how I have developed I cannot crouch with my feet pointed like that because it causes my knees to lock. 

Now I’m 27 and not much helps, drugs don’t help, chiropractor only helps a little bit. My body is basically fucked and idk why I am still here. 

I find myself unreasonably upset with my parent’s neglect of me as a child, maybe it’s reasonable idk but other kids had gone through much worse. 

I just wonder if it wouldn’t have been so bad if they’d have helped me when I was a toddler like the foot doctor said they should have. He said they should have brought me in the moment they noticed my feet going out. 

The pain, the feeling hopeless and neglected like nobody cares is a lot to deal with in a day to day and I have to constantly battle bad thoughts. 

It’s made it kinda impossible to hold down a long term job because physical work hurts my legs and feet and working in an office chair makes my back hurt. 

I’m in the “anti-depressants are bad” camp because I don’t like the way doctors use them and how we really don’t know the effects of a lot of them. 

Besides it’s not really depression if I could just stop being in pain 24/7 I could probably keep a job and enjoy life. 

I had aspirations in life, to be a writer, to maybe possibly if the gods permitted it own some land, to have a son and take him hiking and show him the world. 

But I don’t think those things are gonna happen because I’m being held down by this pain.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l03590v] (score 79, diepte 0) I have a similar deformity in my feet but my feet turn in. Even though my parents did what they were supposed to for turning my feet straight,  there are associated comorbidities that just come along for the ride. I have tibial torsion where by tibias turn 13 degrees inward from my lemurs, I have hip dysplasia just because the heads and sockets of my hips aren't correctly shaped (the sockets are too shallow), and my feet are twisted with unstable ankles.  I also have Ehlers Danlos syndrome,  so my joints are inherently unstable and dislocate for funsies all the time, and I've torn my PCL and dislocated my kneecaps a bunch of times because of how twisted my legs are.  

So would it have helped if your parents did the exercises and had your legs casted when you were 6 weeks old like mine did? Yes,  but it wasn't going to fix everything.  You'd still have problems,and you'd probably still be in some pain,  to honest with you. I certainly am not saying this to excuse your parents' negligence, but more of to temper the blow. 

Exercises and casts can't change the shapes of joints, and you are going to need orthotics.  You're probably also going to need to start up with physical therapy and start strengthening the muscles that support the joints that are affected so that you're more comfortable and can live a better life. A chiropractor is not going to help. I look at what they do as reactive,  not preventative.  For example,  your back hurts. So they pop it, it feels better for a short time but it goes right back to how it was. That's because they aren't addressing the source of the back problems, which is musculoskeletal weakness and imbalance, they're just popping your back and releasing some tension temporarily. Don't waste your money and time.

Go to a physical therapist and an orthopedic surgeon, get a full assessment of what's wrong with you,  understanding that you have many joints involved,  and make a plan with physical therapy to strengthen your muscles and support your joints. 

As a person who has had chronic pain for decades, and am now living with a broken back too, the best advice I can give you to keep you sane is to go ahead and live your life in spite of the pain.  You're going to hurt laying down, you're going to hurt walking. Might as well enjoy life either way.
[l034x23] (score 42, diepte 0) "i find myself unreasonably upset" "maybe it's reasonable but idk other kids has gone through so much worse." BUDDY. YOU ARE IN SO MUCH PAIN. it's not unreasonable to be upset at this, it's fucked up of your parents to say that to you. I'm sorry about your foot :(
[l03bzqi] (score 25, diepte 1) ehlers danlos with femoral anteversion and tibial torsion here also, high five.

for what it's worth op the general theory towards stuff like this now is more that most kids grow out of it so there's not a lot of use in casting/bracing/orthotics for kids. i never got any of that because my doctor promised us i'd grow out of it... except now im 24 and getting diagnosed with a genetic disorder. even if your parents Had known something was wrong, doctors might not have done anything anyways.

physical therapy is a good idea to try and prevent future damage, and build up muscle to lessen the pain over time. but it sucks and i'm sorry you're dealing with this.
[l03i752] (score 15, diepte 0) It sucks that attempts weren't made to help you way back in childhood. You have every right to be pissed, and you have every right to pursue every avenue that might be of benefit to you.

I'd like to encourage you to explore seeing a therapist specializing in chronic pain. Also if you think you're depressed along with the pain (I have chronic migraines.), I am in the pro-getting assessed along with taking meds if necessary camp. I remember worrying about possible long term health impact of Zoloft when I first started on it in 1990-something when it hadn't been around super long. For me, I had to decide that if it blew out an organ 15 or 20 years from then, I'd deal with it at that time. For right then, I needed what I needed to survive.
[l03ban5] (score 14, diepte 0) I am so sorry that you are going through this, but I must let you know 1 thing. Even if you are able to find a doctor who would/will prescribe pain medication, you will NEVER be without pain. 

Pain medication will only ever bring your pain to a hopefully manageable level to function. Your pain will still be there, but at a level that you can somewhat ignore it. You will still have flare-ups, bad days, and days that nothing will work.

If I were you, I would be looking for orthopedic doctors if you haven't already and a doctor willing to help you into a pain management clinic.
[l03clkp] (score 12, diepte 2) Ya, I should also mention that I'm 42, so I honestly haven't really kept up on what the current treatment is for  metatarsus adductus, which I what I have. My actual feet are C-shaped too. Hi fellow zebra!
[l03eqyd] (score 12, diepte 0) I don't think there's anything unreasonable about how upset you are. I'm upset on your behalf!
[l049x4v] (score 11, diepte 2) That's what my parents were told back in the '50s, that I'd grow out of it. Stunning the progress medical science has made in 60+ years. /s
[l043c0w] (score 9, diepte 0) I have scoliosis. It's left me in constant agony. Could of treated it when my bones were still developing as a child but just got told that I shouldn't be in any pain and was never diagnosed. It's basically ruined my entire life and was completely preventable, but alas no-one listened.
[l03p3oh] (score 8, diepte 0) My parents were told they should brace my legs when I was very young but they refused bc my father was supposedly worried it would cause me social trouble. Turns out walking, and especially running, with your knees turned in and your feet swinging out strangely gets you picked on a LOT in adolescence. It also causes ongoing pain for me too. I empathize!! If I turn my knees so they are pointed straight ahead, my feet are majorly turned outward.
[l068yle] (score 7, diepte 1) Also, feelings do not need to be reasonable. Feelings have their own rules completely separate from reason sometimes and that is valid. The way you speak, OP, it sounds like you have been put in a position to have to justify your emotions because others didn't want to deal with them. If that's the case, I'm really sorry, because that's fucked up. Pain causes bad feelings and you are just allowed to be fucking pissed about it. Obviously what you choose to do about those feelings is a different matter and yes you do need to be conscious about the way that you express yourself, but at its core, your feeling is completely normal and completely valid in and of itself.
[l03yvt8] (score 6, diepte 0) Besides the medical neglect that caused the physical damage, you are also a victim of emotional neglect and abuse that is still causing you to feel significant anger and pain. The unresolved emotional pain is most likely adding to your physical pain. I use an energy psychology technique to process emotions and it often helps reduce pain. Here's a link to a video demonstrating the technique, which you can do on your own (or seek out this type of help from a therapist): https://www.paintreatmentdirectory.com/articles-videos/do-this-to-quickly-reduce-stress-and-pain-naturally. I also recommend finding a rolfer, who does very deep body work that corrects structural imbalances in the muscles and fascia. You can find a practitioner here: https://mms.rolf.org/members/directory/search\_rolf\_FAR.php
[l049c6k] (score 5, diepte 0) Why the hell the pediatrician you saw growing up miss this? 

If they weren’t being horribly negligent, they probably had doctor/nurses telling them your development was normal.

I had pediatric doctors screw up too. I wish I could go and screen in their faces for delaying my health problems being treated for 15 years due to dismissiveness.

But my parents? They aren’t doctors, they took and time and money to take me to several doctors and regular checkups in my childhood, they could only have the info they had and quality info wasn’t a quick google search away back then 🤷‍♀️

Your grief is entirely valid, you were screwed and ifs not fair. You should seek grief counseling because this is very serious and is going to be difficult even with help.

As for the “I’m in the “anti-depressants are bad” camp because I don’t like the way doctors use them”… I get the concern, they get over prescribed by people who talked to you a mere 5 minutes in many cases. - But some of them do help pain and it does do so in ways we understand fairly well (I think one used for this might be Wellbutrin) You can probably ask a doctor about this and explain you heard it’s a thing and you were wondering if they think it would help you.
[l03z9yq] (score 4, diepte 0) I am sorry that your parents neglected your health and that you’re in pain. You have some great advice about orthopedic doctors and therapists. You mentioned back pain. A good physical therapist will help you more than a chiropractor.  Mine has changed my posture and has made a difference in my tension headaches.
[l04aapd] (score 4, diepte 0) i hear you. my pain was ignored as a child too, and i am resentful as an adult. i no longer speak to half of my family. i have had disabling chronic pain since i was about 10, but the acute pains started before i can remember. 

on top of not getting the medical care i needed, i hated how my parents mocked me like, "your legs aren't broken, are they?". it molded me into a person who doesn't feel like i deserve help. it made me believe that my pain was not worth relieving. i've been in therapy for 10 years, and am still just scratching the surface of my issues tbh.
[l04a8hz] (score 3, diepte 0) Christ this is all too fucking familiar. 

There has been a lot of exposure of child sexual abuse and its damage, but psychs are also aware that emotional abuse and neglect can do that much damage and more. You are not "unreasonably" upset, and you don't have to minimize/trivalize it as "others have it worse". [rant deleted re gratitude & "count your blessings" keeping people from getting needed help]

You've gotten excellent advice from everybody and I would definitely pursue it.

/u/Warmheartplus is astute in recommending a rolfer. Be sure to find a real one who knows the true Ida Rolf technique, not just someone who does similar deep tissue massage and calls it rolfing.
[l04k2eg] (score 3, diepte 0) Your emotions about your parents are not unreasonable. They are valid. Your pain is valid. Do some people have it worse than you? Yes. Is this a contest? No. You hurt. That’s valid.
[l04tsjc] (score 3, diepte 0) Antidepressants can help with chronic pain
[l04u820] (score 3, diepte 0) I had a car accident when I was 18, ended up in a coma for a few days, stayed in the hospital for a month before they let me out.  I could barely walk it hurt so much and the doctors forced me to walk a bit everyday once I was out of my coma.  My parents forced me to go back to university not even 2 month after the accident.  Still had trouble walking.  8 Months after the accident, I finally got an appointment with a specialist that told me I had broken my back (L4 vertabrae) but it had since healed crooked.  To fix it now would involve breaking it again but that came with a risk that I would never walk again and might not even fix the pain.  

My parents were mad at themselves for forcing me to go to University, I was mad at the Radiologist that missed the diagnosis in the beginning, mad at my family doctor that didn't put enough pressure to get proper tests done.  

It's been 28+ years since the accident, I am still in pain 24/7 but I am no longer mad.  Being mad doesn't do any good.  It was not my parents fault, they didn't know better.  I could still be mad at the incompetant radiolgist (who got fired 10+ after my accident) but what does that bring me.  

What's done is done, I now focus on what I can do to make my life better.  I took me 27+ years to be at this point.  I just never realized I was majorly depressed, once that was more under control, I was able to take my life into my own hands.  Although the pain is not gone and will never be, I am in a great place mentally and physically now.

I am sorry you are going through this, I hope one day you can get passed the anger (which is fully justified).
[l0b74g4] (score 2, diepte 2 OP) >the way you speak, OP, it sounds like you have been put in a position to have to justify your emotions because others didn’t want to deal with them

Yes beyond physical pain my parents utter neglect for mental health too, has caused this.
[l07ep3t] (score 2, diepte 1) I, too, had my feet turn inward and was casted as a baby.  As an adult, my feet are straight but I've had moderate, chronic pain in my feet, knees, legs and hips for most of my life (I'm 56).
[l05yjyg] (score 2, diepte 0) That condition can be fairly painful if not treated correctly. I would be very angry too. You have a right to be. However, i am a chronic pain patient and a healthcare provider and I really think you should seek another opinion NOT from a podiatrist but from a foot and ankle orthopedist. They can do entire reconstruction these days, basically nothing is impossible. 

AND if they say it's impossible then ask for a refferall to pain management or palliative care. Because if it isn't surgically correctable you need compassionate pain management. Normally the referral would go to pain management but if you have something structurally wrong like that and it can't be fixed, you're essentially asking for palliative management.
[l06zbz8] (score 2, diepte 0) I hear you and your feelings are valid I’m pissed on your behalf because you were forced to compete in sports that hurt, well all of it pissed me off but that stuck out to me.
I wanted to comment on your anti anti-depressants comment, your feelings are valid “hey we can’t fix your pain so let’s throw pills at it so you feel better about the constant pain!” I have felt the same way and I’m going through a similar thing with gabapentin. It does make pain less but it also makes my brain fuzzy. I wanted to say that anti-depressants can be helpful. Cymbalta can lessen chronic pain and I do think it helps my mental health overall I would ask you to consider it just to make things a little easier on you. Mentally it doesn’t diminish your pain. It doesn’t make you weak. It just makes all your problems seem less steep and more manageable or at least that’s the opinion I’ve come to believe.

I have cerebral palsy and it’s common for me to trip and I’ve been in constant pain since I was 13 but what struck me recently is when I told my pain management team I fell just oh by the way I tripped, just FYI, they would all be like oh my God, you fell are you OK , and it occurred to me that they seemed more concerned about a single fall and my years of pain and this is happened more than once!
[l076kdm] (score 2, diepte 0) Just an FYI, some antidepressants help with pain. Get over your hangup about prescription medications and avoid quack chiropractors, they are not real doctors.
[l07barx] (score 2, diepte 0) I think you’re actually, quite reasonably angry with your parents. It’s fair for you to be angry. You may choose to forgive them (or not) but you have every right to feel what you feel.
[l07prce] (score 1, diepte 2) Matatarsus adductus team in the house! Are your feet still c-shaped on x-rays?
[l04eqwt] (score 1, diepte 0) You are not unreasonably upset. You are very justifiably angry. A lot of your suffering and pain could have been avoided. 

You may want to check out your state Vocational Counselling for people with diabetes. They may be able to help you find employment more in line with your disabilities.

Hugs.
[l04koy1] (score 1, diepte 0) Honestly I don't think it's unreasonable to be upset, put it this way, if I met you as a child at work I'd be raising a pretty serious safeguarding concern about your parents right now. I'm sorry you've had to go through this.
[l04vi7e] (score 1, diepte 0) They probably just didn’t know any better.

Depression from chronic pain is still depression.
[l052p46] (score 1, diepte 0) That really really sucks. I would be super angry too. I don’t have advice or a similar story, so I want to sit here and make space with you. 

I’m in grad school to become a chaplain, among other things, and I’ve learned that sometimes people need to just be allowed to express what they’re feeling without worrying about others’ reactions or baggage. If you need someone to talk to, I’m not working right now (on FMLA for my own pain) but I have time and energy that I’m happy to use to make space for you. Feel free to DM
[l055g61] (score 1, diepte 0) Pigeon toed = feet that turn inward at the toe
[l05kzby] (score 1, diepte 1 OP) That’s what I meant yes. Sorry.
(9 reacties met lagere score weggelaten)

=== THREAD 192s4jz ===
SUBREDDIT: r/Shoes
DATUM: 2024-01-09  SCORE: 22  REACTIES: 38
TITEL: Shoes as comfortable as sketchers that don’t wear out as easily?
POST (source_id=post):
I walk a lot and the only shoes I’ve been able to find that are comfortable enough are SKETCHERS, I just need something with a decent grip on the bottom that’s durable and doesn’t hurt my feet 👍 Im willing to pay more as long as it lasts a long time

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kh4qae0] (score 10, diepte 0) Go check r/buyitforlife they have opinions about durable shoes!
[kh5hlw9] (score 6, diepte 0) Asics Gel Kayano.
[kh5xtjx] (score 6, diepte 0) Adidas boost. They are kind of expensive but the comfiest shoe I’ve worn and has a rubber sole.
[kh6difr] (score 5, diepte 1) The nimbuses are the most comfortable shoes I’ve ever had. Owned a pair each year for 13 years. Like clouds
[kh5s93z] (score 4, diepte 0) Danskos, even the tennis shoe versions are comfortable. My clog style last for years.
[kh4o7q4] (score 3, diepte 1) The soles of my new balances (574s) wore out really quickly so wouldn’t recommend that particular style. Not sure about the rest though
[kh4xuje] (score 3, diepte 0) I like Merrells.
[kh5c7bd] (score 3, diepte 0) Vionic. I got a foot injury and was recommended these. They are the most comfortable shoes I own, and they are cute as hell. I've had them a few years.
[kh6hnco] (score 3, diepte 0) Replace the insoles and any shoes can become your most comfortable shoes
[kh7zy3n] (score 2, diepte 1) I have a pair of cloudfoams that are 6 yrs old. I wear them "around the yard' and they still are insanely comfy, and still have tread.
[kh57g0h] (score 2, diepte 0) Hoka’s are made for downhill running and have an extra thick sole. They don’t suit everyone’s taste and are on the pricey side but are worth it for the comfort.
[kh4gkrp] (score 1, diepte 0) Air max, air vapor max, addidas Yeezy boost. Those are the only similar feel off my head. For longer lasting maybe get something from new balance in whatever style you're looking for. They're nice for longevity.
[kh4y5ns] (score 1, diepte 0) I got a few pairs of Guess platform gym shoes. They are great for a job where you're standing all day. My black pair lasted 4 years and my white ones are going on 4.
[kh572he] (score 1, diepte 0) Adidas cloudfoam QT, very comfy and last awhile
[kh5pw83] (score 1, diepte 1) I second Hokas so hard! They're so expensive but way more durable than most other brands of running shoes and just so, so comfortable. I've thrown mine in the washer a few times and they come out looking brand new. They're pretty miraculous, totally worth it if you can spring for the significant cost.
[khbvpor] (score 1, diepte 1) after a wedding that had no seating (passed apps all night) hokas were the only shoes i was able to wear for about a week. a year later i wear them every.single.day. wearing my dunks or jordans feels like walking on cardboard now so i really wear the hokas as much as possible and after many washes they are still in amazing condition
[kh5dspj] (score 1, diepte 0) NewBalance are my go to brand for comfort without breaking the bank
[kh5e6dh] (score 1, diepte 0) Hokas
[kh5p6hp] (score 1, diepte 0) Kuru
[kh5q2iw] (score 1, diepte 0) On Women’s Cloudrunner. If you look them up, they have a bunch of other shoes. But I’ve heard nothing but great things.
[kh5r437] (score 1, diepte 0) Hokas
[kh7zhna] (score 1, diepte 1) Adidas adizero are also very good. Have had good luck with boost as well.
[kh8tw4n] (score 1, diepte 1) Yeezy Boost 350s are even more comfy but also more expensive. All I wear now is boost soles
[kh5yehn] (score 1, diepte 0) Ryka
[kh62a7y] (score 1, diepte 0) New balance.
[kh62gnq] (score 1, diepte 0) I think Hokas wins the trophy as its mentioned the most on the thread.
[kh6dsf3] (score 1, diepte 0) Brooks Ghost
[kh72wzd] (score 1, diepte 0) Allbirds. They're 100% the most comfortable shoes I've ever owned. They're like walking on clouds.
[kh77irg] (score 1, diepte 0) Asics

Wear them wayyy too much and put them through work just about daily. Still holding up and I haven't had any comfort issues. I tend to get shoe rubs easily but haven't with these.
[kh7las4] (score 1, diepte 0) Gel nimbus
[kh89ixx] (score 1, diepte 0) Skora Fit
[kh8mxu3] (score 1, diepte 0) Gel nimbus ASICS lastest as a server running through a concrete beer garden for years
[kh8tia0] (score 1, diepte 0) Keen
[kh8u2cd] (score 1, diepte 0) Hoka’s
[kh8y0xj] (score 1, diepte 0) Get a pair of Lebrons. It sounds dumb but I have been wearing mine for 5 years and I can dunk like him if I tried with these on. They are so comfortable and the inside of the soles are smooth like silk, padded all over seriously look at them. 

https://www.nike.com/w/black-lebron-shoes-7y57xz90poyzy7ok
[kh8zjy2] (score 1, diepte 0) Byrdies if you can afford it, for work/corporate environments. 

New Balance for a lot of walking off the clock. I hit 10k steps a day, and my new balances have outlasted skechers by 3 pairs and counting.
[kh9tfoh] (score 1, diepte 0) All birds
[khbgbw4] (score 1, diepte 0) Hokas
[khbhp5n] (score 1, diepte 0) On Clouds 👍🏻
[khd0tss] (score 1, diepte 0) Clark’s
Vivobarefoot
[khgonfd] (score 1, diepte 0) I see a lot of votes for hokas and I want to say that while I love mine for comfort, I’m definitely a little testy about how fast they wear out.
[m3ng1r7] (score 1, diepte 0) Yer sketchers the soles are garbage
[oj1yfh3] (score 1, diepte 1) Yeah, the only thing worse are any brand "sock-shoes."
[oj1yc5u] (score 1, diepte 0) I'd guesstimate something from Clarks or Naturalizers.

