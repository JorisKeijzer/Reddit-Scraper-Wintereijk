# Label-batch batch_0003

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
Schrijf het resultaat naar `batch_0003.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(8 threads: 1n71dwy, 1n9clff, 1n73yc2, 1ngl3g2, 1n5vmpy, 1n6kqns, 1niitsr, 1n8x3b9).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1n71dwy ===
SUBREDDIT: r/PlantarFasciitis
DATUM: 2025-09-03  SCORE: 3  REACTIES: 16
TITEL: Absolutely nothing helping plantar fasciitis pain
POST (source_id=post):
I've had highly suspected plantar fasciitis that has given me severe, disabling pain to the point I was homebound for a few weeks now. It's been almost a month since the pain began. I'm just barely no longer homebound, but still cannot stay out for very long if I go out and still cannot do activities that would require me being on my feet for long, whatever I do I'd have to be sitting the majority of the time. They're actually not 100% sure it's plantar fasciitis, but it's pretty much their best guess since the x ray came back normal and I never fell or anything, I just woke up in pain one day and it hasn't gone away since. 

I guess during the past week the pain has gotten better, it no longer has me screaming and crying and homebound and falling unable to get up, like it was before this past week, but I'm still in pain and still have to limit my daily activities so it's still affecting my quality of life. 

I've tried everything I possibly can access. rolling my foot on a frozen water bottle (makes pain worse), heat, soaking in warm water and epsom salt (no difference) oral steroids (no change to the pain but gave me insomnia) prescription strength ibuprofen and tylenol (helped first few days then stopped working) alternating the ibuprofen and tylenol (no difference)  resting and elevating (no difference) shower chair, cane, walker, crutches (first three no difference, crutches makes it worse as it hurts my good foot then I can't really do anything at all) exercises + stretches (made pain worse) soles, strassburg sock, not going barefoot at home anymore and wearing special sandals specifically for plantar fasciitis around the house (no difference) 

I'm at a loss, I don't really know what to do. I can't access a podiatrist or even urgent care because there's none in my area that accept medicaid. I do have an upcoming appointment with the free clinic (the only kind of pcp I have access to, I don't get to have a private practice pcp on medicaid and medicaid assigned me to one specific free clinic and calls it my pcp. Other clinics won't accept me and tell me to call the one on my medicaid card) but I really don't know what they're gonna be able to do since they won't be able to refer me to a podiatrist since none I can get to accept medicaid.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nc4dj9q] (score 3, diepte 0) It sounds crazy, but try ductaping your feet. That's the only thing that helped me (medical tape and k-tape didn't seem to work for me as it's too flimsy). I wrapped a piece all the way around my foot right where the arch starts near the front and then one piece flat on the bottom.
[nci5m56] (score 3, diepte 1 OP) thank you, I'll try it
[nc4pms1] (score 2, diepte 2) It doesn't need to be professional. Just self massage. There are lots of youtube videos on it.

Just curious, what were some of the stretches you tried? Did it include the 2 I mentioned in bold?
[nc52pgh] (score 2, diepte 0) 500mgs of vitamin C daily helped my PF go from unbearable to barely noticeable. Vitamin C has something to do with collagen regeneration.
[nc5jbg5] (score 2, diepte 0) Man that sounds brutal. PF is usually slow and annoying, but what you’re describing is next level. Hope the clinic can at least rule out nerve issues too.
[nc482ig] (score 1, diepte 0) Arch supports, the ones from Wal mart work, put them in all you’re shoes that you wear, now get some Tevas for showering, never walk or stand without the arch supported, even when you get up to go pee in the night, you’re ligament/tendon has poor blood supply and healing takes time, first time you go un-supported you tear that tendon from the heel bone and you’re back square one, don’t forget those Teva’s in the shower, you cannot tear that tendon again during the healing period
[nci5pu9] (score 1, diepte 1 OP) thank you, I'll try that
[nci6zjg] (score 1, diepte 2) I hope you find some relief!
[nc4i7ky] (score 1, diepte 0) I had PF for about 6 months. I wasn't even able to walk over 5 minutes. I now do 10,000 steps daily as of just a few weeks ago. 

Are your calves tight? Does deep massage hurt? I'd start there, at least a few minutes of deep massage per calf. Personally, I was so fed up with it, I did a professional massage and they nailed into them for like 20 minutes each. But that alone wont fix it.

You also need to do non weight bearing stretches. I'm assuming all your stretches were standing, leaning against a wall, etc.

Try these 2 non standing stretches:

**Supine calf stretch with strap**

**Ankle Dorsiflexion Stretch (seated or other knee can be kneeling down)**

  
Let me know if you have any questions
[nc4jwdq] (score 1, diepte 1 OP) No, idk how to massage so idk.

Unfortunately I can't afford a professional massage. I have like $2

Nope, those weren't any of the stretches I tried. ALL of them were completely non weight bearing and they still caused more pain
[nci5kzl] (score 1, diepte 3 OP) idk I don't know the names I just looked up stretches for plantar fasciitis on google
[nckilib] (score 1, diepte 4) Got it, so you didn't even look up the two I gave you and deduce if you've done them before. Okay good luck.
[ncioq7m] (score 1, diepte 1) Really ? 
Wow … never heard that b4 … I’ll try that 
Thx
[nc5v29m] (score 1, diepte 0) Sounds like you need to get it healed enough to be able to start doing proper stretches (for lower back and achilles tendon) because right now the injury is stopping you from getting to that point. 

Imo get the brace boot and make it your business to be wearing it as often as realistically possible; never ever sleep without it, when you're sitting around, get that sucker on. It's a mental torture as well as physical to not be able to walk and to feel dread and pain at basic tasks like showering and cooking. I hope your appointment goes well.
[nc5v514] (score 1, diepte 1 OP) Oh I actually have the brace boot and it has made absolutely no difference so
[nc5zfvz] (score 1, diepte 2) how long are you waiting to see if there's a difference? It's easy to spend too little time/commitment to treatment when you're busy trying as many things out as possible to see what sticks - and then it's frustrating because nothing does and you just need releif asap.

But at your degree of pain and injury (especially if it's a fascia tear), "no difference" is the only alternative to "getting worse" for the time being. If you can spend as much time with you foot at "no difference" and that foot is held stable and unaggravated it *will* start healing, and in three or four weeks you may notice that it's taken the edge off, and then you'll start finding that when you try things, some of them make a positive difference. gl
[nc5zo3j] (score 1, diepte 3 OP) idk I've had my brace for like three weeks and everything else for like a month 

my main problem with the brace is that idk how to put it on, when I try it completely falls apart. I need someone else to put it on for me and that isn't always possible.
[nc610gi] (score 1, diepte 4) oof i'm sorry to hear that. I highly reccomend prioritising getting a good brace that doesn't doesn't fall apart.

If the reason why you need help putting it on is mobility, the culprit could be related to the lower back, so be sure to investigate that avenue for stretches. If the issue is weight, then that's almost certainly related to the ongoing cause of the foot pain unfortunatley.

As for why it's not made a positive difference yet, that's because the *cause* of the injury is still present, so you need to figure that out. The podiatrist should be able to help with that. (and also as you've said, the brace just falls off, you can't get it on yourself and it's not on properly then like why would it work?)
[nc61895] (score 1, diepte 5 OP) the brace I got was from the ER so how is that not a good brace

The reason isn't mobility or weight. It fits. The reason is I don't understand how.

You didn't read the whole post? I stated I can't access a podiatrist.
[nc68y6m] (score 1, diepte 6) If it's on properly when someone else puts it on and you don't have mobility issues preventing you from doing the same, then it seems clear that you just need to learn how to put it on the way they do. It would be pretty wild to remain in debilitating pain all because you didn't learn how to learn to put on a simple brace after all.

It's also possible the ER gave you a bad or weird one - a hospital will stock and hand out cheap stuff. I hope you're able to get your hands on one that works.
[nc6ag0i] (score 1, diepte 8) hmm, the ER one was probably too weird - there are many strange variations after all. I have one like [this](https://www.braceability.com/cdn/shop/products/10a0101-braceability-plantar-fasciitis-night-splint_1080x.jpg?v=1626989083) that's been a life saver. Three clasps and that's it.
[ncp4bjc] (score 1, diepte 0) I’m sorry that sucks.

Are you able to access a physical therapist on Medicaid? I think they could help tremendously if you can.

Hope you heal quickly!
[ncw9tad] (score 1, diepte 0) The only thing that finally worked for me was taking the time to finally see a podiatrist. I work on my feet and it was so bad it finally sent me to a professional. I spent crap loads of money on different shoes, inserts and everything you listed. First she tried injections twice with minimal effect. Then we went through my insurance for custom orthotics. Expensive as hell but 2 weeks after wearing them, I woke up with zero pain when stepping on the floor. That was 5 years ago. Now I have issues with my Achilles so I think I may need another appointment
[np30xh7] (score 1, diepte 0) severe PF that made even walking across a room painful and nothing else seemed to help. Switching to FP insoles made a huge difference for me; the Gamechangers mold to your arch and keep your foot aligned, while the Kingfoam Elite absorb a ton of impact without pressing on the arch. Unlike other insoles that went soft or didn’t give real relief, these stayed firm and let me finally get around without making the pain worse, even for short walks.
[nc6925i] (score 0, diepte 7 OP) So I have a learning disability and this is one of the things that just will not absorb in my mind I don't understand

=== THREAD 1n9clff ===
SUBREDDIT: r/flatfeet
DATUM: 2025-09-05  SCORE: 11  REACTIES: 16
TITEL: I finally scheduled surgery!
POST (source_id=post):
I’ve had flat feet my entire life but the past year my left foot has gotten way worse. It’s causing significant pain in my right knee and hip. I’m so freaking nervous that I’m making the wrong decision. My pain isn’t unbearable, but it affects my quality of life. I’m just terrified I’m going to be one of the ones whose arch fails or the hardware causes worse pain. 

I’d love some success stories. Especially ones where you were able to be active and workout after recovery.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ncmjgmb] (score 3, diepte 1 OP) The officially surgery is “ displacement calcaneal osteotomy and lateral column lengthening with allograft, possible FDL tendon transfer depending on state of posterior tibial tendon, reconstruction of the spring ligament, Achilles lengthening”

Basically, he is breaking my heel to realign it with my ankle. He will possibly do a tendon transfer, put a pin near the bone that runs along my big toe, and an Achilles tendon stretch.
[ncpsnu4] (score 3, diepte 0) I do not know that I am a success story as I am 5 weeks post op. What I will tell you is that surgical pain is bearable. The inconvenience of the surgery is by far the worse of it. 

Be prepared and have someone to assist you the first 10 days post op, search threads for recommendations on equipment (wedge pillow, commode, walker, lift chair, etc), start working on your upper body strength NOW if you don’t have any.

Start checking out YouTube videos for navigating stairs, etc. If you have stairs to get in and out of your home begin figuring out how to navigate them and practice in advance.

Know you won’t be driving yourself for two months, have a plan.

My biggest hurdle was not being aware, prepared for life during recovery and it has been a challenge.

Good luck with your recovery.
[ncp2gg2] (score 2, diepte 2) What are they saying the recovery process is?
[ncmudws] (score 2, diepte 0) Oh wow so almost exactly what I had done! Now that I’m a few weeks into recovery, it’s so worth it! Proud of you for making that appointment! I’m feeling pretty much no pain already!
[ncp1j83] (score 2, diepte 0) Cheer up. You're right about the pain. Undoubtedly it is not extreme pain because otherwise we would all be wearing morphine patches, but it is disabling pain. Unfortunately, my arch has already fallen and I want to have surgery at the beginning of the year. I hope everything goes well for you.
[ncq8vrp] (score 2, diepte 1 OP) Thank you! I could probably live with the pain a little longer but the fact that it’s affecting my knees and hip on my good side is what driving me to do it. I’m 43 and walk like a 90 yr old when I get out of bed
[ncqhrf1] (score 2, diepte 3 OP) I will absolutely do an update post! I’d love to know when I will be able to workout again. I work out 6 days a week, so I think not doing that will be the hardest part
[ncr073r] (score 2, diepte 5 OP) I can’t train like I used to. Def can’t jog even and the slowest level. If I walk more than 2 miles, my foot is out of commission for the next 24 hrs. I can squats and slow foot things but no jumping ever. Like i def can’t do a calf lift on my bad foot. Not even if someone offered me $1000. It’s physically impossible.
[ncr4x60] (score 2, diepte 0) Im 7 weeks out of surgery, no more cast and started physical therapy. Its a tough process but as long as youre prepared you'll get through it!
[ncm2trp] (score 1, diepte 0) Are you getting flat foot reconstruction? What does the surgery involve?
[ncpwlnr] (score 1, diepte 2) That’s awesome. Good luck
[ncq9kjf] (score 1, diepte 2) Me too. I have decided on that, I look like a grandmother and the pain has increased and spread to other areas of the foot. My good foot is also starting to hurt and that makes me cry with worry. Keep us informed and have a good recovery 😘
[ncqk711] (score 1, diepte 4) Just like me. I also train practically all week. I have a lot of pain but I can train, that's why I'm afraid of the operation and that I'll never be able to play sports again 😔
[ncrczrq] (score 1, diepte 6) Hahahaha hahahaha I read you and I think I wrote it. Squats, deadlifts and all that, perfect. Jump, I get chills just thinking about it. I used to walk a lot, eight-hour mountain routes. Now taking the dog out is a pain. To make matters worse, I work standing and carrying a lot of weight. I leave work as if I were wearing two skis. Calf raises if I hold on to the wall and with both feet. With the bad one, unthinkable. When I have to pee during the night, I just want to drink the entire box of lorazepam that I have on the table. Everything wonderful.
[ncq9fma] (score 1, diepte 1 OP) Thank you! Yes I am starting to think about how to manage being immobile for the first months. Luckily I have one of those scooter chairs and my bedroom is on the first floor. Im getting it done in December so Christmas might be a bit of a bummer. But I’ll be all healed up for the Spring/Summer!
[ncrudvq] (score 1, diepte 1 OP) Are you able to walk/put weight on it? Do you see a light at the end of the tunnel? LOL
[nd0k1z5] (score 1, diepte 2) Not yet :( My next doctors appointment is on Sept 29 so hopefully my surgeon will approve to start weight bearing. Ah the light, idk cause my next surgery is in December cause of insurance 😭 as soon as this is healed, I have to do it again.
[nd0phrp] (score 1, diepte 3 OP) What do you have to do again? The other foot?
[nczzplc] (score 1, diepte 0) I had the surgery done 16 months ago and have made a full recovery. I am activiely playing pickleball, walking golf and working out every day. I'm F 68 year old. It's a brutal recovery but if you follow doctors orders you will have a successful outcome and resume life as you want. I was 6 weeks bedrest and 3 months non-weight bearing but after that, I started slowly walking in a boot then progress to shoes. I did 8 months of PT 3 x per week. It does take alot of work but the outcome is worth it. You do have a choice on the anesthesia - I was given Experal which is a nerve block and it lasted 7 days for me. Total numbess in my leg for 7 days so no pain meds, no oxy. Talk with your anesthesiologist and ask what your choices are. There are quite a few with different lengths of duration. Good luck! It's a long road but worth it.
[nd0r39r] (score 1, diepte 1 OP) What was the moment you knew you needed to have the surgery? I struggle with the thought of “do I really need this?” Sometimes my foot isn’t that bad. I’m 43 F and I can’t walk long distances and my knee and hip hurt on my good side, but it’s not unbearable at all times.  I know this will never improve and could get worse. Do I deal with it now, or wait until it’s an emergency. PT 3 times a week for 8 months seems exhausting
[nd2fq7x] (score 1, diepte 2) I was interviewing alot of doctors at the time and still playing alot of sport. They consistently said that my ankle would degrade slowly or it could degrade really quickly. Well it degraded quickly and I was in a big Cam boot. My arch had completely collaspsed at that point and the arch tendon was torn.  It still took 4 months to get the surgery scheduled. There is never a good time to carve that much time out of your life. But I do have my active life back and I was running into the same issues you are experiencing - with a hurt foot, you throw off the alignment of your body and other things hurt. That is another reason for the long PT as you have to fix the entire posterior chain.
[nh80rgr] (score 1, diepte 0) I had surgery 6.5 year ago and don’t regret it in the slightest. Had daily nerve pain and wore an ankle foot orthotic for 2 years prior to surgery. I was in my late 20s when it was done and it is a very significant and painful recovery but I have virtually no pain in that foot now. I had a tarsal tunnel release, first metatarsal fusion, and lateral column lengthening done. 1 plate and 8 screws that do cause some discomfort in the winter but nothing like before. Don’t wear orthotics at all anymore but I do lean towards supportive shoes.
[nh8msth] (score 1, diepte 1 OP) I love to hear this! I go back and forth every other day like “do I really need this? I’m not THAT bad!” But then I always go back to the fact that it’s never going to improve and my knees and hips will only get worse. I walk like an 80 yr old and I’m half that.

My goal is to do a single calf raise on my bad foot. That to me seems impossible right now.
[ntsakds] (score 1, diepte 0) Congrats on scheduling the surgery! Many people find that using FP Insoles after recovery can make a huge difference in managing flat feet and protecting your arches, knees, and hips. They absorb up to 90% of impact and provide stable arch support, which can make returning to walking, workouts, and daily activities much more comfortable. Even after surgery, adding FP Insoles inside your shoes can help reduce strain and support long-term foot health.

=== THREAD 1n73yc2 ===
SUBREDDIT: r/PlantarFasciitis
DATUM: 2025-09-03  SCORE: 8  REACTIES: 15
TITEL: Can’t do my job
POST (source_id=post):
I have intense tender pain along my arch. I’m seeing a PT but it hasn’t been improving. I work in a warehouse that requires a lot of walking. I had to clock out early today because every step on my foot felt so tender.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nc4s2yl] (score 5, diepte 0) Best I can tell you is to try some kuru shoes. They got me from not being able to stand for short periods of time to being able to go to amusement parks for 6 hours.
[nc57coa] (score 4, diepte 0) This has messed up my money, life and relationship. Just asked my dad for some money to help cover my rent because I can barely stand up at work and don’t do overtime anymore. I’m starting to get better after almost a year but I can imagine this still being a problem 6 months out. Mannnn ever seen I’ve been dealing with this I notice has well other people walk, the small things we used take for granted.
[nc7532a] (score 4, diepte 0) I had this experience when I first developed PF. In the early stages, PT won't necessarily be a good first step because fascia tissue has been damaged and being told to do exercises can be doing the opposite of healing. I went to PT instead of a podiatrist and that was a mistake. You got to rest the feet and not aggravate them, if something hurts, stop. Its telling you that you're putting on too much load. A night splint/boot really helped me at the start. You can look up the reason this helps but it basically puts your feet in a neutral position as the fascia heals. Taping your feet with KT tape or medical tape helps a lot and it can support your long walks in the warehouse. I personally use KT tape and there are variations of the taping methods. You can get them cheap at Target. Lastly I don't see or hear enough about the calves, but stretching and massaging them helps a ton. I stretch them every morning before I go to work and it makes a difference. Your calves are very much connected to your fascia. If there's anything about shoes for PF, be aware of its shape. I am no longer wearing shoes that squeezes my toes together. Size up or get wide toe box shoes (not the same thing as the wide shoes).
[nc6oxl0] (score 2, diepte 1) They helped me, too. I can walk 3 miles a day, now. I still have pain first thing in the morning, but walking in the Kuru shoes seems to actually reduce the pain. I have no idea how that works, but it does.
[nc53bns] (score 2, diepte 0) Radical sleep. You’re damaging fascia more than its healing. Aim for 10-12 hours in bed, lots of protein, and be patient
[nc61klt] (score 2, diepte 0) Ask your PT or doc about diff shoes/inserts or even temp light duty.. pushing thru pain usually makes it worse..
[nc6602w] (score 2, diepte 0) You can find some decent orthotics and cushy shoes to make things more comfortable during the day. I have Brooks Ghost Max and they are super comfy. The 2’s are on sale right now most everywhere. You can get a night splint to help healing at night off Amazon for under 30$. Do you have a low med or high arch? Figure this out before you buy orthotics or go to a shoe store that does em. Take ibuprofen to deal with the pain and keep the inflammation down. Ice it at night. Lots of people like the frozen water bottle. Massaging it can feel good, but don’t smash. Also don’t start doing extreme stretching right away. Take some time to let it heal. Spend the weekend watching TV in your boot. Then start your stretching and exercise.
[nc79clb] (score 2, diepte 0) Hoka running shoes work for me as well. I have tenderness on the medial aspect of my left arch, my heel rarely hurts. Calf stretch’s and raises really do help
[nc9k93n] (score 1, diepte 2) I so wish that had worked for me. They help but my pain still increases throughout the day and gets unbearable toward the end
[nccvhy6] (score 1, diepte 1) I picked up a pair of casual dress ones and they were great. I saw improvement immediately. So I thought I'd try some sneakers for the gym. these did not work and made my PF hurt. 

in my experience even the shoe type makes a difference. I am replacing the sneakers for a slip on walking shoe to see if I can get the same results as the dress shoes.
[nc50hp4] (score 1, diepte 0) I hate working at a desk, but the past couple of years I have been thankful. This exact boot is really helpful https://a.co/d/14wBxcT. The boots that come up higher are better. You can wear a toe guard if your job requires it. Try to find another shoe with a bit of a platform so your other foot is even.
[nc6ijq6] (score 1, diepte 0) Has anyone tried The Good Feet Store? I've seen the TV commercials where the customer feels immediate relief in the new shoes.  Google shows all of the locations in Chicago Area have 4.9 stars.  No I don't work for them.  I just like to spread information in case someone wasn't aware.
Locate a Store | The Good Feet Store https://share.google/CMBzJWQpquxAOxh4n
[nc7cppw] (score 1, diepte 1 OP) I have it in both feet. One more than the other. I think I developed it from wearing steel toe shoes all day
[nc7mg07] (score 1, diepte 1) I agree completely about going to a podiatrist first before any PT. Rest, stretching, and proper supportive shoes and orthotics are the best thing you can do in those early stages of damage. If you have a Good Feet store or anything like that near you, they can suggest good shoes and orthotics before you get in to see a podiatrist. My personal experience is that I made everything so much worse by hiking and running and being in denial that I had plantar fasciitis.
[ncalll7] (score 1, diepte 0) Try getting your PT to show you show to tape your feet. You need that additional support, and it may help keep your PF ligaments stable and tight.

=== THREAD 1ngl3g2 ===
SUBREDDIT: r/Mortons_neuroma
DATUM: 2025-09-14  SCORE: 1  REACTIES: 15
TITEL: High heels
POST (source_id=post):
I get this incredible burning discomfort on one foot at toe 4 when I wear heels.

So I dont wear them much...once in a while. An event is coming up and I would like to wear heels
 Does anyone have advice or trick or accessory that works for them?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ne4whcl] (score 5, diepte 0) Don’t wear your highest heels. Choose a lower pair. Make sure you have a pad under your foot, those sponge make up pads will do and put it not on the hurt but just behind it towards the heel and towards the instep. Stick it with tape on to your foot. Don’t wear high heels at all or pointy toes. It sucks having this.
[ne4xluf] (score 5, diepte 0) I get most relief from separating my toes. Toe socks that only cover the toes might help, if your shoe has a closed toe. I found some online. 


Alternatively, you could try the gel toe/finger separators that come as a tube which you trim to size - I've seen them at pharmacies.
[ne9f22b] (score 5, diepte 0) If you must wear heels, look for shoes with a wide toe box.  They won't look as cute or dainty, but they also won't destroy your feet quite as much.
[ne7xmu1] (score 4, diepte 2) Yes! Life changing. And yes I can even run long distance now without pain
[ne4sg9n] (score 2, diepte 0) You can buy little pads that go under the ball of your foot and reduce the pressure on the neuroma! I got some on Amazon
[ne7n4ky] (score 2, diepte 0) No I had to get surgery and couldn’t wear heels for a year 😭
[ne8ztdz] (score 2, diepte 0) Nope. The only thing that helped for me was a neurectomy. I literally could not walk or stand for 5 minutes or more without being in excruciating pain. Had my surgery in March. My foot has never felt better. Literally no pain and I can go back to wearing my highest heels
[ne97ur6] (score 2, diepte 0) I’m 26 days post-neurectomy and was able to wear heels yesterday for an event without issue and it was amazing! My incision is still healing, so I did wear a bandaid over it so my shoe wouldn’t rub against it.

My neuroma was 1cm in size and it is so wonderful to be able to walk without pain and that popping sensation with every step!

As others have mentioned, I would buy metatarsal foot pads from Amazon and use them as they do help cushion the ball of the foot.

I’m going to be re-evaluating my shoes and making sure I buy only ones that have wider toe boxes and will still to mostly flats or only tiny heels for dressy shoes.
[ne9q747] (score 2, diepte 1) Could you walk after surgery or do you have to be on crutches?
[ne9qr65] (score 2, diepte 2) I was able to walk out the day of surgery, but was in a protective shoe that looked more like a sandal with a really firm sole for two weeks to keep the foot flat (as opposed to bending it while rolling through a step).

I got my stitches out two weeks later and in regular shoes at that point.
[neaaf2f] (score 2, diepte 0) I live in heels. 
After my podiatrist found my MN, I bought a pair of birkenstocks and wore them for three weeks. Pain dissipated and I slowly started incorporating low heels back into the rotation. 
I’ve now gone back to heels and haven’t had an issue with pain since. 
I know I’m probably not the norm, but it worked for me.
[neacqhx] (score 2, diepte 1 OP) Good to know. I just ordered spacers 🤷‍♀️
[nef1rgo] (score 2, diepte 0) I’m 6 weeks post neurectomy. My neuroma was 2.5cm in diameter a the size of a 5cent piece, with a bursa around it too! The largest one the surgeon has removed, he was shocked. Iy was excruciatingly painful. At 6weeks post off I still have swelling and nerve pain. I will never wear heels again.
[nej3lvp] (score 2, diepte 0) Can you wear flatforms instead?
[nekoqc9] (score 1, diepte 1 OP) I just ordered these. Fingers crossed
[ne7q5gh] (score 1, diepte 1 OP) Did the surgery help? Do you wear heels again
[nekosn8] (score 1, diepte 3 OP) Amazing. Did insurance cover
[nemdiya] (score 1, diepte 4) Yes!
[ne8yfg9] (score 1, diepte 0) What type of surgery did you have?
[necwfi3] (score 1, diepte 0) strangely enough, when I had foot pain years ago it would only manifest when I was flat footed. when I would put on high heels it would relieve the pain in my toes. it turns out the reason is because the high heels immobilizes the toes whereas walking flat footed uses the full range of motion of the bones, muscles, and toes. so it took a long time to get a diagnosis since I would have never suspected that my high heels were actually causing the mortons neuroma. I had it surgically removed in 2014 and have not worn high heels since then.
[nekouh9] (score 1, diepte 1 OP) I can. Sigh.

=== THREAD 1n5vmpy ===
SUBREDDIT: r/bunions
DATUM: 2025-09-01  SCORE: 1  REACTIES: 14
TITEL: Can orthotics make bunions worse?
POST (source_id=post):
36F I’ve had bunions for almost as long as I can remember. My mother claims they are a consequence of ill-fitting orthotics she got me at one point. (My mother is not the most reliable with medical stuff, so I’m unsure how true this actually is) She then consulted with someone else who fitted me with new orthotics. I wore them for a couple years, but then I stopped for about 20 years. 

Fast forward to now. I decided to start running, but I had severe tibial pain. I consulted for custom orthotics. The issue I have is my feet tend to rotate inward and almost lay flat (even though I don’t actually have flat feet). Now this issue seems resolved as I don’t feel any pain anymore when running. I did have to go for adjustments 2-3 times because the correction was too intense and was causing me pain in the arch, but now this part seems fine. 

I’ve noticed however that I have more « comfort » issues related to my bunions. Some shoes felt tighter around the toes and I feel pain when I used to barely notice them. I initially shrugged it off, but now I think I’m noticing the left bunion is more prominent. I did ask the doctor initially if what my mother claimed sounded plausible, and she said it was unlikely. 

I’m freaking out a bit and now I don’t want to wear the orthotics anymore except for running. So what do you think reddit - can custom orthotics be worsening my bunions? Is that even possible?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nbvs476] (score 3, diepte 0) Hey there! Podiatrist medical assistant here with 6 years of experience. 
Bunions are genetic, sometime they can formed due to wearing unsupported shoes like high heels or  wearing narrow shoes. Since you mentioned that you are flat footed, then your deformity is genetics. Custom orthotics do not worsen your deformity, it’s the running. The more pressure you apply on to your feet the more stress you are applying onto the joint causing the deformity to worsen. (If the skin around the bunion area, then they are growing) custom orthotics will slow down the growth process but it will not fix them. The only way to fix bunions is surgical intervention. If surgical intervention is not possible at this time, I suggest getting  custom orthotics from a podiatrist!
[nbw2uyu] (score 3, diepte 1 OP) Thank you for your response. I did get my custom orthotics from a podiatrist. Yes maybe running is the issue. :( it’s a shame, I had finally managed to get in better shape.
[nbwhn1l] (score 1, diepte 2) I feel you babes! I was in track during high school and my bunions were bad. I had MIS done (not everyone is a candidate for it) and i do not regret it at all. I am 27 and the healing process was quick for me.
[nbwzvk8] (score 1, diepte 2) I had to give up running bc of bunions, I have a stationary bike now. Also swimming. I need to get some weight bearing exercises in too.
[nbwirfv] (score 1, diepte 1) Are you saying running is a no go for bunion sufferers? Any impact exercise?

I do crossfit and also took up running in the past 4 months. Unfortunately it’s within the last 2 weeks I’ve discovered I’ve got bunions because of the pain I’ve been feeling recently. 

I really hope I don’t need to quit one or both of these things? 😔
[nbxyj93] (score 1, diepte 2) You can continue to run, but always keep in mind that the running is making your bunions worse. Custom orthotics will make a huge difference while running and depending on what company your podiatrist works with you can get athletic custom orthotics. Unfortunately the only way to fix it is surgical intervention. I had my surgery two years ago and I’m running around pain free.
[nbyxqih] (score 1, diepte 3) I got my left foot done 12 weeks ago and healing is going well, but I took up the stair master so as not to worsen the right like running did. Am I just making it worse with the.stairmaster too?!

The shit we go through to stay healthy, I swear lol.
[nc53qj0] (score 1, diepte 3) Respectfully, running itself doesn’t make bunions worse — *how* someone runs, the shoes they wear, and the strength of their feet do. If running alone was the problem, every culture and every runner worldwide would have bunions, and we know that’s not the case.

Orthotics might bring temporary relief, but they don’t correct the underlying mechanics — they just shift the load. And surgery should always be a last resort, not the default solution. I’ve seen plenty of athletes reduce bunion pain and keep training hard by improving foot strength, mobility, and mechanics — no scalpel required.

Running doesn’t have to be the enemy. The way we prepare the body for it makes all the difference.
[nc53l2g] (score 1, diepte 2) Not at all — having bunions doesn’t mean you need to quit running, CrossFit, or any impact exercise.

The pain usually comes from how load is being distributed, not the activity itself. Shoes that squeeze the forefoot, weak foot muscles, and limited mobility can all make bunions feel worse. But with the right approach — wider toe box shoes, strengthening the foot/ankle, and good movement mechanics — plenty of people keep training hard without things getting worse.

You don’t need to give up the things you love. You just need to take the pressure *off* the bunion and put it back where your body is designed to handle it. That’s a solvable problem — not a reason to stop moving.
[nc2mhkp] (score 1, diepte 1) Don't men to hijack here, but after two separate surgeries 7-8 years apart, both my feet are ragged even with orthotics.  I work in food service so I'm on my feet 8-9 hours day, never mind walking my dogs or doing yardwork.  My current podiatrist says that I'm slowly "undoing" both surgeries from being on my feet for so long.  

For the record, I genetically intoe and have flatter than flat feet.  The orthotics help some but it's really the shoes you wear.  Feet aren't static.  I've got about a half dozen pairs of sneakers in different sizes, some of which I can no longer wear with the orthotics.
[nc539n7] (score 1, diepte 1) Labeling bunions as purely *genetic* and prescribing orthotics as the only solution is what keeps people stuck. Genetics may play a role, yes, but only a very small part of lax joints — but environment, footwear, and mechanics are 99% contributors. If it were purely genetic, we wouldn’t see such differences across cultures that live and move barefoot.

Orthotics don’t “slow the growth” — they mask symptoms while the underlying mechanics continue to be unaddressed. I’ve worked with plenty of athletes who’ve improved foot strength, mobility, and gait — and seen bunion pain reduce dramatically without surgery or orthotics.

Surgery should always be the last resort, not the default plan. And orthotics should be a *temporary tool*, not a lifelong prescription.

We don’t need to brace the body more. We need to train it to function the way it was designed.
[nbxsoev] (score 1, diepte 0) I had bunion surgery 21 years ago. Last week I had a bone spur removal from top of big toe plus both little toes. I’ve not had any issues up until getting custom fit orthotics in March to help with some tendonitis in my ankle. I’ve run many marathons since my initial surgery but training for my most recent with the orthotics they caused terrible blistering and burning. I started to get inflammation on top of my foot and at the sides. Eventually the skin on top of my foot broke over what became a massive inflamed bone spur, that became infected and I’ve had to stop all activity and even wearing shoes for several weeks. The orthotics elevated my foot in the shoe and changed my foot mechanics when running causing excess pressure on top and forced my feet outwards causing inflammation on the sides. . I’ve now missed a major race sitting at home post surgery having got all this fixed. I doubt orthotics cause your issues from years ago but I know mine aggravated a mild issue and made it much, much worse.
[nbxyrg6] (score 1, diepte 1) Hey! Depending on which company your podiatrist works with, he should have gotten you athlete custom orthotics. In my clinic we work with Footmaxx and the athletic custom orthotics are the best! I have no issues with them while running. I’m sorry that they are not working out for you!
[nbxzhso] (score 1, diepte 2) I’m in Australia and went to a sports podiatrist attached to sports academy, however, anyone can go there athlete or not so not sure what changes, if any, could have been made. I did get them modified to have some blister patches added which have a shiny surface under the toes where the most pressure was. I’m a forefoot runner. They were better for running and less burning but felt very slippy when walking and foot would slide off with each step. I didn’t get to use them much after they added those as the damage was already done and now been out of wear I g shoes for a handful of weeks while the ulcer healed so could proceed with surgery. It’s been a long and expensive process!!
[pacnk6v] (score 1, diepte 0) Je ne suis pas médecin.

Les orthèses modifient la répartition de la charge sur le pied. Cela peut apporter un soulagement, mais aussi créer un nouveau point de pression.

L'apparition de frottements, de sensations de brûlure, d'ampoules ou d'un manque d'espace dans la chaussure doit vous inciter à cesser temporairement d'utiliser cette paire. Apportez les chaussures concernées ainsi que les orthèses au spécialiste qui les a prescrites.

Un inconfort passager ne signifie pas nécessairement que l'oignon (hallux valgus) s'aggrave sur le plan structurel. Une vérification de l'ajustement permet de le déterminer bien plus efficacement que des suppositions sur Reddit.

Les jours de course, observez si la douleur survient pendant l'effort ou plusieurs heures plus tard. Cette précision aide à ajuster l'orthèse ou la chaussure, et pas seulement le programme d'entraînement.

=== THREAD 1n6kqns ===
SUBREDDIT: r/PlantarFasciitis
DATUM: 2025-09-02  SCORE: 4  REACTIES: 14
TITEL: Are you more prone to getting plantar fasciitis again once you develop it?
POST (source_id=post):
It feels like once you develop plantar fasiciits, it tends to come back later out of nowhere

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nc10rmh] (score 4, diepte 0) Not in every case. I had it for seven long years, and ever since I got rid of it in September 2023, I've had zero issues.
[nc0rrf2] (score 3, diepte 0) Yes, generally speaking. I think if you are younger and/or develop a minor case of PF that resolves quickly, then you are not necessarily at greater future risk. But if you're like 40+ and you develop a case that takes months to resolve, then you are probably at greater risk of getting it again in the future. That's certainly been the case with me.
[nc21ibl] (score 3, diepte 1) That’s mighty long. And forgive me if I’ve asked you before, what helped you beat it?
[nc14cjt] (score 3, diepte 0) Yes, based on the general view regarding any soft tissue injury wrt sport. 

Makes sense as well. We heal after damage but it’s never the same as it was prior. Anyone who’s ever injured anything can attest to this. 

But at the same time, if your level of tolerance/strength was much subpar or below your true capacity, you could probably strengthen to a point that you minimise or eliminate the risk of reinjury.

Interesting question though with some nuances. Thanks for asking.
[nc6p5bw] (score 2, diepte 2) I (6'0") lost weight (at the recommendation of my podiatrist), plain and simple. I tried everything; every stretch, exercise, and insole on God's green earth.

In July 2023, I was at my wits end; my feet hurt ALL the time, and I was the heaviest I'd ever been in my life (213 pounds; I've averaged between 180-185 for the majority of my adult life). I thought I'd end up on disability, as I could barely walk anymore. I decided to go back to my podiatrist to seek out surgery, as I could no longer take my feet feeling like I had a 10,000 degree railroad spike rammed in them. My podiatrist agreed that I'd be a good candidate for surgery, and wanted me to get an MRI. On my way out the door, she (podiatrist) told me that she once had PF, and knew how bad it is. When I asked her if she had the surgery, she said no, that her PF went away after losing weight from having twins. I decided right then and there to eliminate ALL sugar from my diet, minus a small glass of pop at dinner. I also began drinking a full bottle of water immediately after dinner to really fill my belly up, so I wouldn't crave snacks later.

It took a couple weeks, but I noticed I was getting lighter on the scale. By late September 2023, my weight dropped down to 187 pounds (I had NO idea how bloated I was); this is when I told my fiance that I noticed my feet were hurting a little less every day for around two weeks straight, until they simply stopped hurting. I maintained my clean eating habits, and now weigh 175 pounds. 

I never made the appointment for the MRI, and I never went back to my podiatrist, as my feet have now been completely pain free for two years. Even with a decent sized bone spur on each heel, my feet are fine. All I did was clean up my diet, as I did not increase nor decrease my exercise whatsoever.
[nc728ks] (score 1, diepte 3) I do remember your story now. Sorry for having to rewrite it again. Thx.
[nc75ce0] (score 1, diepte 4) All good. I know what it's like, and am in this sub because I don't like seeing others living with PF. 

I bring up weight loss often because it worked for me (at the recommendation of my podiatrist), and that the fact that 75% of Americans are overweight, and 45% of Americans are obese. Literally everyone I've ever met in my life that has PF is overweight.
[nc7m1vs] (score 1, diepte 5) Lol. I’m approaching over weight as a result but wasn’t like this before getting it. But get your point and appreciate the good faith.

Just wish there was an easy way to drop the pounds once you get to a certain level which is where I am now
[nc7pkbl] (score 1, diepte 6) >Just wish there was an easy way to drop the pounds once you get to a certain level which is where I am now

It's all about CICO (calories in, calories out). I dropped 25 pounds from July 2023 - September 2023, just by cleaning up my diet. I absolutely LOVE those Hostess coffee cakes, and I decided to get a bunch of Wrigleys Doublemint gum to substitute with, as it has that sugary taste. I also had a huge problem with snacking after dinner, so I made it a point to chug a whole bottle of water immediately after dinner (10 minutes max) to really fill my belly up. 

My brother has PF, and is 5'8" and 196 pounds. He complains that he "doesn't have time to lose weight', because he doesn't have time to exercise. I told him that it's a LOT easier to just not eat 400 calories than eat them and then walk for for hours to burn them off.
[nc7rz5c] (score 1, diepte 7) Thanks. Especially like the end quote about about 400 calories as I remember I hit this at around 30 - 40 mins of running on the treadmill.
[nc2750v] (score 1, diepte 0) I think it happens again because tissue capacity can’t handle the load leading to overuse or it was never adequately healed in the first place before you go
stress it out again.
[nc2v9bt] (score 1, diepte 0) I think it depends on what caused it.

I still always recommend people go see a physiotherapist and have your gait analysed.
[nc5iotr] (score 1, diepte 0) Yeah, PF can flare back up if you go back to the same habits too quick. Consistent stretching and not ramping up mileage suddenly helped you avoid relapses.
[nc5x4ct] (score 1, diepte 1 OP) It’s frustrating. I wish I never developed plantar fasciitis in the first place

=== THREAD 1niitsr ===
SUBREDDIT: r/Mortons_neuroma
DATUM: 2025-09-16  SCORE: 29  REACTIES: 14
TITEL: It's been a year since I figured out the silicone insoles with a hole 'trick'
POST (source_id=post):
I'm posting this because whoever is still struggling with MN might want to give this a go. I can't guarantee it will work, but it's worth a shot IMO. 

For me, this year has been pain-free in this regard. I've walked long distances, hiked, danced. 

I've made two posts about this: 

[https://www.reddit.com/r/Mortons\_neuroma/comments/1g8k7qj/this\_is\_how\_i\_can\_walk\_painfree\_i\_hope\_it\_helps/](https://www.reddit.com/r/Mortons_neuroma/comments/1g8k7qj/this_is_how_i_can_walk_painfree_i_hope_it_helps/)

[https://www.reddit.com/r/Mortons\_neuroma/comments/1hrpzlc/a\_few\_people\_have\_asked\_to\_see\_my\_diy\_insoles\_and/](https://www.reddit.com/r/Mortons_neuroma/comments/1hrpzlc/a_few_people_have_asked_to_see_my_diy_insoles_and/)

  
The short version: cut a hole in a silicone insole where the neuroma is, and insert it in your shoe (you might need to size up the shoes, or get shoes with removable insoles). That way, you don't step on the neuroma. 

For the summer, I bought a cheap pair of slippers from the supermarket (material similar to Crocs) and completely cut a hole in one of them where the neuroma is, and those have been my house slippers since May/June (I live in a warm country). It has worked perfectly. 

Let me know if it helps! It would make my day!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nel97ni] (score 3, diepte 0) There are insoles called "dancers pads" that come shaped with cutouts under the big toe ball of foot, if that's where your pain is.
[nekdo51] (score 2, diepte 1 OP) Check out the link for my previous post, it includes pics. 

Trial and error. I put my foot on the silicone insole (without a shoe) and I stepped (flexed my foot, lifted my heel) and where I felt the neuroma pain, I marked the place on the insole. 

Best to start with a smaller hole and build up if necessary. 

For me, once I got the right spot and size, I got a template essentially. Any new insoles are easy to create with the previous ones. 

You can also try with the cheap foam insoles (layer them), so that you find the right spot in a more affordable way than ruining silicone insoles. For me the foam ones were not enough, because my neuroma was very painful, and I had to have something thick and solid enough to be able to not step on it at all.
[nekcvto] (score 2, diepte 1 OP) There are pics in my previous post which I have linked. Hope they help.
[nenp11v] (score 2, diepte 2) Aha, fab thank you
[nensin6] (score 2, diepte 3 OP) You're welcome!
[neu806z] (score 2, diepte 1 OP) I think so, my silicone insoles have metatarsal bumps, that's why I originally got them. Unfortunately, they didn't do anything for me. But the hole is after the metatarsal bump, so it doesn't interfere.

I also have some silicone metatarsal pads (just for that part of the foot), which also haven't helped me. 

I'm really glad they've worked well for you, I know they do work for many people. 

How are your inserts?
[neujszi] (score 2, diepte 3 OP) I don't have a specific brand. I have two types that I got from local pharmacies and stores in Greece. But check out the picture in my previous post, and you will see the type, I think there are many such silicone insole brands. 

The hole in mine is around 2cm wide and 3cm long. You can try a smaller hole first and cut more if necessary.
[nejdg1p] (score 1, diepte 0) How big of a hole? How do you know exactly where to put the hole?
[nejykg7] (score 1, diepte 0) Can you share a Pic?
[nekpcce] (score 1, diepte 0) That is a good idea. But it dont know "exactly" where it is. I get intense burning pain at the 4l3rd and 4th tow and they go numb. I think the MN is just below but indont actually feel a lump
[nennygl] (score 1, diepte 1 OP) Interesting, I can feel the clicking thingy, like I'm stepping on a pebble. 

You could try layered foam insoles instead of silicone in the beginning, in case you need to destroy a few before you find the actual spot. It would be cheaper.
[nennsco] (score 1, diepte 1 OP) I Googled them and they look like a potential good solution for people who need the extra cushioning there! Have you tried them? 

I don't think they would work for the MN in my right foot, because any stepping on the neuroma hurts. My MN on my left foot would probably be quite happy with these.
[nep2kei] (score 1, diepte 2) I have a different forefoot pain condition called "sesamoiditis" which is when you injure the bone in the ball of your big toe. Dancers pads work well for this, though since it's a fairly permanent injury I also got custom orthotics (insoles) from a podiatrist. The insoles have a depression where the sesamoid bone is to relieve pressure on. They were $20 annually with insurance and $500 without.
[nepajn5] (score 1, diepte 3 OP) Wow, I'm glad you got yours with insurance. Wild price!
[nepu0u0] (score 1, diepte 4) Yeah it's absolutely bonkers. If my insurance doesn't continue, I think the solution you propose (manually cutting out a hole in a regular insole) is a fine way to go. I did this while waiting for my orthotics and while I don't think it'll last as long, several of these over time will still be cheaper than $500. I recommend forking out for slightly better than Dr. Scholl's-- something rigid like Superfeet with serious arch support also reduce the pressure on the forefoot.
[net2jxr] (score 1, diepte 0) Have you ever tried inserts with metatarsal pads? They've worked fairly well for me, not sure how I would combine it with this.
[neuhex0] (score 1, diepte 2) Mine are just the regular kind with metatarsal and arch support. I still have some old pairs somewhere that I can experiment with cutting holes in.

What brand do you use? How big is the hole you cut in yours? I wonder if too big would let my foot kind of sag/slip down and touch the bottom of the shoe.

=== THREAD 1n8x3b9 ===
SUBREDDIT: r/flatfeet
DATUM: 2025-09-05  SCORE: 1  REACTIES: 13
TITEL: Need sandals for around the house
POST (source_id=post):
My feet are flat as can be. My doctor recommended that I avoid walking barefoot whenever possible. 

So I'm looking for something comfy to wear at home. I currently use crocs but doctor recommended Oofas or Brikenstocks. 

My flat footed brothers and sisters. What sandals or options for home use have you found to be the most comfortable and supportive?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ncif780] (score 3, diepte 0) I got these a few months ago and they’re really comfortable  https://www.keenfootwear.com/products/mens-newport-wide-bison
The heel support really helps.
[ncjgnby] (score 3, diepte 0) I just got Oofos slides.  I had surgery and walking barefoot is not fun.  So far they seem great. I needed something for when I get up to go to the restroom in the middle of the night.
[ncl7q6n] (score 3, diepte 0) I live in Birkenstocks. They aren’t squishy at all but the have this arch support  that makes my arch actually feel supported and not feel like it’s collapsing. Plus they are super in style!

*pro tip: don’t buy the knockoffs! They don’t have the arch support
[ncmpbvt] (score 3, diepte 0) I'm from the Netherlands and live in the UK since 2016 and I've been a loyal user of Merrell sandals for years. I believe they're an American brand. I'm currently sporting the [Women's Terran 4 Post Wrap](https://www.merrell.com/UK/en_GB/terran-4-post-wrap/59120W.html?dwvar_59120W_color=J006404#cgid=womens-footwear-sandals&prefn1=isOnSale&prefv1=false&start=1)" in nutshell/bracken (brown), but they only have that colour for the backstrap version now. I've been wearing different Merrell models for a good decade+ now, and I wear them almost daily for probably 3-4 years before I have to replace them. When I lived in NL I'm pretty sure I had to pay import on them.
[ncigtww] (score 2, diepte 1 OP) Thank you for the reply, I’ll check these out!
[nckmrzc] (score 2, diepte 0) Archie flip flops help my flat feet!! Also they are so cute 😊
[ncqa5of] (score 2, diepte 2) I have the Arizona’s, Madrids and just bought a pair of the clogs. They’re expensive but it’s worth it!
[nclixor] (score 2, diepte 0) I got some fake EVA Birkenstock sandals off Amazon for $15 and five years later I still love them. I say this as a former service worker who was always searching for comfortable and supportive footwear and rarely found anything that suited my needs.
[ncncss2] (score 2, diepte 0) OOFOS Ooahh slides = instant “walking on clouds,” great for sore flat feet; Birkenstock Arizona (soft footbed) = firmer support that lasts longer. YMMV.
[ncjq1e6] (score 1, diepte 0) I love my doc martens, i also wear crocs, & i recommend tevas.
[ncoz6ug] (score 1, diepte 1) Which model are best for you?
[nco43gs] (score 1, diepte 1) Link?
[ncjjktg] (score -1, diepte 0) Try Crocs! They make some cute ones that are a more sleek. They also double as shower shoes when you go on vacation. They have built in arches. Super comfortable. My feet are the flattest. You will love them.

