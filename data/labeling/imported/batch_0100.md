# Label-batch batch_0100

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
Schrijf het resultaat naar `batch_0100.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1ws3t0f, dzhuum, 15gclyq).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1ws3t0f ===
SUBREDDIT: r/BuyItForLife
DATUM: 2026-09-28  SCORE: 97  REACTIES: 74
TITEL: I feel like I will never find comfortable shoes that are actually cute for plantar fasciitis.
POST (source_id=post):
I have one pair of shoes that works for me: the New Balance Fresh Foam X 1440. I own so many more pairs of shoes but when I wear them and walk around for even a half hour my feet hurt so much. I have worn these shoes so much they have holes in both the toes. I have always dreamed of being able to wear cute shoes , especially fancy ones for events, but now I don’t think I would be able to. Do you guys know of any shoes that would work? The first photo is the shoes I have and the rest are shoes I would love. Also, hard shoes do not work for me. The only reason these do is because of the foam and how far my foot is from the ground

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[pci9s48] (score 447, diepte 0) Physical therapy will help more than shoes
[pcikqf4] (score 182, diepte 1) Listen to this, OP! Took me a few months of going to PT weekly (it has been going on for 6+ months) and doing the exercises daily, but it’s completely gone for me now. The longer you live with it, the harder it is to cure — tissue death will start to occur. Your body is the only truly BIFL item, take care of yours.
[pcih7ck] (score 70, diepte 0) OP any chance you’ve seen a podiatrist? I felt like you did and swore it was plantar fasciitis but I actually had an unknown foot deformity (small but caused long term ankle and pain issues).

Others recommending insoles are partially right and PT might help but this isn’t actually normal if you truly can’t find any other shoes that work. Go start with the foot doctor?
[pcic8s6] (score 46, diepte 1) One physio appt (and the recommended at-home stretches) and I am pain-free. None of the many shoes I tried did much of anything.
[pcit20r] (score 43, diepte 2) I went to a podiatrist and all they’d told me to do was stretch my calf on a step. And buy insoles. What exercises are you doing??

I also have a friend who wore a foot brace for a couple weeks and set it permanently cured him, but those things are so uncomfortable and I’m skeptical…
[pcigg0s] (score 33, diepte 0) Insoles, babe! A good pair will last ten years. Not a lifetime, but you can use them with whatever shoes you like!
[pcj174f] (score 31, diepte 3) yes do calf stretches - the stand on a step (stair) and lower your heels is good, it helps so much! (and it's cheap and easy, can't do wrong - but you need to do it 😭)  
  
I just started one that is curl you toes, put the back of you foot (like right before the toes starts) on the ground and bend you knee a bit, to stretch you shins - it worked so well for pain after walking I was baffled.

Using a rolling pin to work your calves is also good- you do not need to buy equipment - and the handles make is easier to roll it down your calves
[pcju394] (score 22, diepte 0) r/barefootshoestalk is full of good suggestions and you can always ask for brands etc there as well. I used insoles and PT for years with no luck, switched to shoes that have a wider toe box and holy cow, I dont have painful feet anymore (it took a little time for my fascia to calm down, but my feet are so much better now). There are lots of cute barefoot shoes options now!
[pci8vj2] (score 21, diepte 0) Vionic Birkenstock
[pcjbykc] (score 21, diepte 5) No, the exercise really looks like this [https://fuss-sprunggelenk-akademie.de/fuss-sprunggelenk/uebungen/uebung\_6\_3/vordere\_schienbeinmuskulatur\_1.jpg](https://fuss-sprunggelenk-akademie.de/fuss-sprunggelenk/uebungen/uebung_6_3/vordere_schienbeinmuskulatur_1.jpg) back of foot 😥😭?
[pck0aqj] (score 19, diepte 6) Ohhh thanks, I would never have pictured correctly. I think I would have said top of the foot myself haha
[pck3kzl] (score 13, diepte 4) My pt also had me use a golf ball to massage the area that hurt (my heel, ball on the floor & roll it around with your foot)

While sitting put a hand towel on the floor under your foot with most of the towel extending past your toes & use your toes to scrunch the towel toward you (strengthens your foot)

While sitting put your foot flat on the ground, lift only your big toe, lesser toes stay in contact with the ground, then do the opposite, lift your lesser toes & keep the big toe on the ground. 

What helped me the most other than PT were crocs. I wore them whenever I could, including around the house. Now I have some strappy sandal crocs (with a thick sole) & they work great too & look less appalling 😅
[pci9w2u] (score 12, diepte 2) Check out the Birkenstock Paris Chunky; they seem in line with what you like. They make a lot more than Arizonas these days.
[pciuw4q] (score 12, diepte 0) Vionic are pretty cool... also did you try custom insoles / orthotics like the stuff from Superfeet? And... r/goodyearwelt approved work boots of any sort... some are available in really cool sole and leather stylings... and give the height effect of heels and the like without all the foot damage.
[pcj1pvc] (score 12, diepte 0) Have your knees, foot, hips checked first before giving up on normal shoes - permanent pain is something bigger at work usually.

 I was adamant I had plantar fasciitis this year- turns out it was something worse and I wasted time with only trying to 'cure' a plantar fasciitis with the exercises I knew (long time foot pain sufferer, insoles and frequent check-up since I was a kid, thought I knew all my foot problems already 😒)
[pcih56q] (score 11, diepte 1) OP could see a podiatrist to ask about custom orthotic inserts
[pcj4lre] (score 11, diepte 4) Do you mean ball of your foot? Feels like there has to be a typo/autocorrect there
[pcih8t6] (score 11, diepte 0) There’s a subreddit for PF with a lot of recommendations
[pci8roi] (score 10, diepte 0) No shoes are BIFL but you could look at YRU platform shoes. The soles are squishy foam and they make chunky Mary Janes
[pci8xte] (score 10, diepte 0) What about getting some cushy insoles for the shoes?
[pciivn4] (score 9, diepte 0) It’s a lot less about the shoe and more about the inserts. But the longer term solution would be getting it treated in physical therapy.
[pckutr0] (score 8, diepte 1) Losing weight is what got rid of mine, 20lbs is when I started noticing the pain was gone. I’m not suggesting anything to OP, btw! Just wanted to share what helped me because plantar fasciitis fucking sucks.
[pcjrmd9] (score 7, diepte 3) I got a brace from my podiatrist.  It wraps around my ankle and then theres a thick elastic band that goes under right before my heel. Its helped immensely, though I still need to do the stretches. I also have gotten a couple of 30 min massages just focusing on that-a lot of the tension is the calf. Plus wearing squishy shoes that look dumb around the house. But if its the same type of brace, it really does help.
[pcja7tk] (score 7, diepte 0) Mine went away when I started stretching my legs!! Just go to the doctor!!
[pcidykw] (score 6, diepte 0) Considered custom orthopedic insoles? Expensive, but...

Prosthetics companies make them for diabetics and other people with foot sensitivity. They mold them to your feet to redistribute pressure.
[pcii8do] (score 6, diepte 1) Also, if you've been going to physical therapy off and on without any sort of curative success, you might need to strengthen your feet even more, beyond just the exercises. That was the case for me personally as I have hypermobile spectrum disorder (it's soooo under diagnosed btw) and need extra muscle to keep all my joints in place. Slowly introducing barefoot style shoes helped me strengthen my feet day to day while also re-teaching me how to land my feet to reduce the impact. I do more of a mid foot strike now as opposed to a heel strike while walking, and I now stand with my center of mass more on the ball of my foot rather than my heels. Hypermobile patients often have a heel pad that sort of squished out of place, so it doesn't protect the foot from impact as well as it should. Barefoot shoes allow me to feel the ground better and adjust my walking and standing habits more easily. This has helped me more than any particular insole or supportive sneaker.
[pckmz9u] (score 6, diepte 0) This is going to sound weird but. My plantar fasciitis was the worst after I broke my ankle and it finally healed enough for me to walk on it. ( I had pf prior but.. but breaking it did not help lol) 

The only shoes I could genuinely wear without pain was my Tevas Hurricane XLTs. When I mean without pain- I mean I did a whole camping lake weekend with my dog and no matter how long we hiked I has no pain, which felt inpossible prior to trying them. Something about the footbed is just perfect for me, it isnt too soft so they las a long time, I just throw mine in the washer if the straps are gross. 

Even now that my pf is much better, they are still my favorite and I wear them even in the coldwith some wool socks and I’m good!
[pcla3lo] (score 5, diepte 2) Its so tricky to suggest this - i applaud you for it.

Its what did it for me.  230 lbs down to 210 and its like it wasnt even a thing.  

If losing weight is not a reasonable option, my night guards worked pretty good.  But I had to get the crazy big ones from a medical supply store because I could work the other ones off in my sleep.

Stretching before getting out of bed helps a lot as well.

Also not wearing shoes all the time and building up the muscles in your feet are important as well.  I found I became to reliant on wearing shoes for 14 hours straight and it still wasnt making them any stronger.  Having an awesome stretch/workout routine is important :)
[pck9wb2] (score 5, diepte 1) This is the way!! Buy the good insoles, put them in the shoes you actually want to wear. Best of both worlds.
[pcmg538] (score 5, diepte 1) I think it’s probably a bit of both. The right shoes make a huge difference for me but even after physical therapy the pain came back a few weeks later.. 

So I think both matter.
[pciazyw] (score 4, diepte 0) Barefoot shoes
[pciitit] (score 4, diepte 0) The [Santa Claritas from Birkenstock](https://www.birkenstock.com/us/styles/santa-clarita/?srsltid=AU7gw4U7iarWYz59MV2ULZf8KohJ3q7Yds2vG3koPWloxFuluHSQfWVq) are passably cute but they're hard and flat. Using them for my retail job has made my plantar fasciitis better.
[pckftbj] (score 3, diepte 3) There were a lot — the ones described here help somewhat but for me it was also key that he identified where the stiffness was actually coming from. For me, I had a very stiff midfoot so we worked on learning to fully spread my toes and sink my weight into the midfoot. I really recommend finding a PT to work with  
and not just trying to fix it on your own!
[pdg1mte] (score 3, diepte 3) i recommend you go to an actual physical therapist. mine is having me strengthen my hip muscles in various ways and its helping my plantar fasciitis
[pec73pi] (score 3, diepte 4) Thank you, I’ve been to PT and was confirmed to have weak hips and glutes lol fml. There are dozens of us!
[pcijj84] (score 3, diepte 0) Plantar fasciitis runs in the women in my family. You can try Orthofeet: my mom orders shoes from them and gets a lot of use from their online 60-day wear test policy. You can wear the shoes as much as you want for 60 days and still send them back. When your feet are really bad you can still be in pain when the shoe is just a little off, so it's a useful policy.
[pcikgo7] (score 3, diepte 0) I own all of those American Duchess shoes and even though the Bronte slippers are super cute they are incredibly flat and will probably be difficult to get an insert in. I wear them for events but never for very long. The Alpine and Renoir boots are super comfortable and you may be able to get an insert into them for additional support. I love my AD shoes, but they're not very supportive if that's what you need.

Aetrex makes a super slim insole (L500w) that I've successfully used with the Kensingtons and it makes them much more comfortable and I can wear them for much longer.
[pcjekvx] (score 3, diepte 0) Not cheap, but cute. A Broadway actress I follow who struggled with plantar fasciitis swears by this [brand](https://baredfootwear.com/us/collections/all-womens).
[pcjthzg] (score 3, diepte 0) I recently purchased the FitFlop Delicato Poise Mary Janes. I can’t speak to their longevity yet but they are cute in a sleek, understated kind of way and very comfortable right out of the box. Quality seems solid. The uppers are buttery soft leather and the insoles are very supportive. 

One note, I tried the ballet slipper version of the Delicato from the same brand and the fit was completely different. I’ve noticed this with other brands, that just because one style doesn’t fit the way I want doesn’t always mean the whole brand is not for me. So don’t give up hope if one cute style from a brand doesn’t work!
[pck0480] (score 3, diepte 0) One thing I don't see mentioned here is posture. Weight should be on your heels not the front of your feet. That simple shift can take the pressure off your arches. I suffer from back, hip, knee and foot pain. It wasn't until I became aware of how I was standing that I realized how much the position of my hip and where I was centering my weight mattered. Fixed that and as my 6 year old says, Wall-ah! Pain pretty much gone and I don't have to wear the expensive insoles from the doctor or the Keen shoes that while mostly comfortable I feel keep my foot in a prison rather than letting it move and flex.
[pckkyky] (score 2, diepte 2) Orthofeet!  They come with additional inserts and a 60 day wear trial that they genuinely stand behind. I developed PF after breaking both ankles at the same time. They have cute and professional shoes.
[pciqad4] (score 2, diepte 1) Yes!!!
[pcix62h] (score 2, diepte 2) Your body, Build\* it for life
[pclgvtz] (score 2, diepte 1) yes! my dad was convinced he had plantar fasciitis until i realized the congenital deformity i have is a dominant gene and he likely has it as well.
[pcjigfs] (score 2, diepte 0) Where are the blue boots with fur on the last slide from please? They're lovely!
[pckxok4] (score 2, diepte 1 OP) They’re from American duchess
[pck783w] (score 2, diepte 0) I went to the running store and got quality insoles. I can’t think of wearing a pair of shoes without them (except sandals) I think you could get specific ones from a podiatrist.
[pciqfpw] (score 1, diepte 3) Ty
[pcjde9f] (score 1, diepte 3) I would LOVE a pair of these, they’re right up OPs alley!  
  Skechers also did some cute lace-up boots historically which might suit OP when paired with an insole. Swapping the laces to a ribbon can completely change the vibe!
[pckbvx3] (score 1, diepte 4) ikea is now selling rolling pins (nice acacia ones) for a very affordable price FYI y'all!
[pciftih] (score 1, diepte 0) So these [Aetrex Mary Janes](https://www.aetrex.com/products/erica-casual-blue-cutout-ca425w) aren't exactly the cutest shoes ever, but they are designed to relieve plantar fasciitis! I have a pair of boots from Aetrex, and the heel cup design was very comfortable. The toebox was a bit narrow for me, but if you don't specifically need wide toebox shoes, these should work.
[pcjmeg9] (score 1, diepte 1) I am a podiatrist and have never heard of insoles that last ten years. 

Hook us up.
[pckupew] (score 1, diepte 1) Adding that I was informed ten years isn’t a feasible time to expect them to last. Just fyi. That’s really how long I used my last pair. :) Ymmv
[pckxduu] (score 1, diepte 1 OP) Omg those are so adorable
[pciq705] (score 1, diepte 0) Find a good, experienced foot Dr- age of 40+
[pciqeew] (score 1, diepte 0) And JBUs and Jambus
[pciqk0k] (score 1, diepte 0) Clarks
[pciy1kt] (score 1, diepte 0) it's a struggle to find both comfort and style in shoes
[pckyyh9] (score 1, diepte 2) Omg they ship to me... oh no 😂 thank you!
[pcjrmse] (score 1, diepte 0) I have chronic foot pain (plantar fasciitis and a bilateral Morton’s neuroma). When it’s bad I wear a pair of Dr Martins Mary Jane’s, the soft leather ones. I recently realized that taking a B vitamin complex and rolling a hard therapy ball under my foot really helped. I also have insoles in every pair of shoes I own. I hope you find relief.
[pcjvj1l] (score 1, diepte 0) The brace everyone talks about it where it's at.  Also, I love Earth Shoes.  Cute and super cozy! I have problems with my feet and it's only that company from here on out for me!  I have had 6 shoes from them, my first were given to me.  Best ever!
[pck0odh] (score 1, diepte 1) I wear Dr. Scholl’s loafers and their Western Bootie is a cute heeled boot, Naturalizer makes the comfiest heels I’ve ever worn. I still avoid a heel higher than 2” and I limit how much I walk in these - they’re not an all day shoe - they are a one-off for nice events or when I want a break from sneakers.
[pcktgu2] (score 1, diepte 0) I've always had good experiences with Durea shoes. They do offer some cute ones like their Mary Janes.  
They're a bit pricey though.
[pcktiot] (score 1, diepte 0) i hear this-about to try new balance as i think hokas are hideous! interested what non sneaker shoes are working here also
[pcl2jqe] (score 1, diepte 0) The bifl part is a slant board so you can do calf pt exercises every day. That will make a huge difference for the pf
[pclfwpe] (score 1, diepte 0) Some of these shoes - all of the, actually - are terrible. Head over to [r/footfunction](r/footfunction) and do some reading. GaitHappens is also a great resource. If the hole is on top of your shoe over the big toe, this is very good information to tell a foot professional.
[pcllo6m] (score 1, diepte 0) I tried so many different insoles and shoes. The only thing that helps in the long run is strengthening your feet and legs with weight training to improve foot posture
[pco9r7g] (score 1, diepte 0) I always look for good quality shoes and check reviews for "good arch support." 
My best brand for women's shoes is Dansko. 

I also put in Super Feet inserts plus a cushion for Morton's neuroma, in case anyone has that as well.
[pcocfy1] (score 1, diepte 0) Oofos and losing weight helped me more than all the shoes and PT I could pay for
[pcoznzi] (score 1, diepte 0) All those shoes are fucked anyways since you'll be squishing your toes into them and continuing to cause yourself long term pain as the foot deforms.

Other than a medical professional having shoes with a wider toe box with room for the foot to splay out will go a long way with long term health.
[pcq3tem] (score 1, diepte 0) Brand: Rieker. Style: Doris.
[pcq6l47] (score 1, diepte 0) I don't know if Plantar Fasciitis is what I had.

I got diagnosed with like three different things, by three different doctors. Finally got approved to see a specialist for imaging, after PT failed, and be told there was nothing wrong with my feet: "They're strong and your PT did an excellent job with your balance and stride."

7+ years of foot pain so bad it was rough to make myself get out of bed.

Went to a run store for new running shoes. Kid working the floor says, "I think your shoes are too small, would you be willing to try going up a size?" Fixed.

Anyway all that is to say, there's a lot of "advice" out there for foot pain. You're gonna have to do you. But...

Wedge heels/sandals, with a good ankle strap were the most comfortable "cute" shoes for me when I was struggling with foot pain. It wasn't perfect, but it was doable.

Also strongly recommend NB 9060 and Hoka Bondi 9. They aren't cute, but they are comfort perfection.
[pcskbnl] (score 1, diepte 0) Vionics & PT
[pd38cs6] (score 1, diepte 0) )
[pdw8kir] (score 1, diepte 0) Can you get shoe inserts? There are ones specifically meant for plantar fasciitis.
[pciq0ky] (score 0, diepte 0) ‼️‼️‼️😭 I only have 2 feet!
[pck0f42] (score -1, diepte 0) Dr. Scholl’s and Naturalizer are great brands for cute shoes that won’t mess you up!
(2 reacties met lagere score weggelaten)

=== THREAD dzhuum ===
SUBREDDIT: r/ems
DATUM: 2019-11-21  SCORE: 242  REACTIES: 74
TITEL: Dispatched at 03:25 for achy feet
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[f87npns] (score 162, diepte 0) Pain's been going on for a week, 4 cars in the driveway, family's home and awake, patient weighs 400lbs and is normally ambulatory, but can't be bothered to walk, and expects you to carry them from their bedroom on the third floor to the truck
[f87t6wm] (score 113, diepte 1) Could be referred pain from the PT's cranium being fully inserted into their rectum.
[f887q4v] (score 108, diepte 0) "So what occurred or changed at 325am that made you call 911 for an emergency?" 


I do in fact ask this question on a regular basis.
[f884kiu] (score 84, diepte 0) MAYBE TAKING YOUR FUROSEMIDE AS SCHEDULED WOULD HAVE PREVENTED THESE PROBLEMS, SUSAN
[f87zlg7] (score 60, diepte 0) Drink water, change your socks, take 600mg ibuprofen.
[f87v13g] (score 51, diepte 1) At that point I’m busting out the SKED and she’s goin for a ride. I’m also gonna pointlessly rearrange furniture for “better egress.”
[f8859nn] (score 50, diepte 1) And control your fucking diabetes.
[f88joum] (score 47, diepte 1 OP) So do I. The response is typically nothing
[f88pcva] (score 43, diepte 2) “Can’t move the stretcher in here unless this couch is moved outside”
[f88kpxf] (score 39, diepte 1) "it makes it reaaaaally hard to sleep :("
[f887487] (score 34, diepte 2) *heavy breathing pink puffer intensifies*
[f88oc2w] (score 33, diepte 1) I mean, it is a perfectly valid question. The hope that they may realize their stupidity is just an added bonus.
[f88vx9a] (score 29, diepte 3) I thought I was the only sicko that did this.
[f88js1i] (score 29, diepte 1 OP) Another life saved
[f889j98] (score 26, diepte 2) What's your favorite crayon flavor there jarhead?
[f88e7rb] (score 26, diepte 0) If in doubt, blame it on the gout
[f88b99a] (score 25, diepte 3) The green ones taste like apples
[f88nwev] (score 24, diepte 1) "Pain got worse, I couldn't sleep" is the usual answer.
[f89abm4] (score 24, diepte 1) I had a guy who called us out at 4:30 am because he hadn't peed in five days.  I asked him, "So, at 9 pm last night, had you still not peed in five days? What changed between now and then?"  

Later on, his daughter, who was attempting to run the call, told us she was going to follow us.  I couldn't resist saying, "Oh, I thought you'd ride with us, since your car is out of order."  

She stared at me blankly, "No, my car works fine."  

I laughed, "Oh, I just assumed that it was broken since you didn't just drive him directly to the hospital."  

She, not realizing I had just deliberately insulted her, simply responded, "No, my car is fine. I'll follow behind."
[f888snu] (score 22, diepte 1) Squid
[f88bmw6] (score 21, diepte 0) Tyfys
[f88kn7s] (score 21, diepte 1) They don't.
[f88nvs8] (score 21, diepte 0) i’ve got one better. dispatched at around 2-3am because the pt had heard something fall in the other room and thought someone was breaking in. didn’t even want us to take their vitals. the whole call i was wondering why the fuck they would send us instead of police. ended up poking around the house - nothing. some days, i wonder...
[f87n8mg] (score 16, diepte 0) Probably just needs a poo
[f88q5ou] (score 15, diepte 2) Here I am.
[f896xl9] (score 14, diepte 2) “I just couldn’t take it anymore”   
  
“It just became too much”
[f89307d] (score 13, diepte 7) *ChairForce
[f88jovb] (score 10, diepte 4) Also, not a squid
[f8939ch] (score 10, diepte 2) She knows the cheat code
[f88o6j5] (score 10, diepte 3) Every one of my friends and family know to only call 911 on me if I'm unconscious and can't fix myself. 

I ride in the back enough to know that I dont want to be on the receiving end of some of my coworkers
[f896vbn] (score 9, diepte 8) You sound jealous of his tee-time.
[f88gyv4] (score 9, diepte 0) I get this call a lot and 65% of the time it’s just homeless people who walk a lot with no shoes and 90% of the time it’s after 1am. 

Not to be a dick but, no shit your feet are gonna hurt.
[f891i3b] (score 9, diepte 0) This shit is literally every shift for us in built up areas in the UK. I still cannot fathom that at 0330hrs this is the time they decide this needs to be sorted; not the past 18 months where they haven't been to the GP.

My favourite ever was a guy who had been shot... 10 years ago in Iran but now he needed looking at. It was 0400hrs on a fucking random Thursday. Just fucking why?
[f88w4ed] (score 8, diepte 1) Uric acid crystals settle at low points due to gravity, no? I'd expect her to be complaining of pain in her colossal ass.
[f88pzss] (score 7, diepte 5) Sound like a squid :p
[f88qwy1] (score 7, diepte 6) Sounds more like a whiskey
[f88fr8j] (score 6, diepte 0) Twinkie wrappers and empty Dr Pepper cans EVERYWHERE
[f8910qv] (score 6, diepte 1) Yeah, my last foot pain call was around 1200 hours. Lady was sitting outside of a urgent care on the curb. She wasn't wearing shoes or socks and told us that she just couldn't walk anymore, said she had been walking all morning. We told her that didn't warrant a 911 call. She panicked and said that she was now having chest pain and breathing difficulty.
[f890teu] (score 5, diepte 1) You pay for it.
[f88tust] (score 5, diepte 0) How long has this been going on for ?

3 or 4 years
[f897czv] (score 5, diepte 1) Happened to a crew in my station, only it was that he hit his toe with something pretty hard and was worried it might have broken. 7 years ago.
[f891k7l] (score 5, diepte 0) ProQA recommendation Delta Response “ALS/BLS”
[f88rqzz] (score 4, diepte 6) Nah, Air Force
[f8907nr] (score 4, diepte 1) That's my question of choice as well.
[f897jth] (score 4, diepte 5) In fantasy land, it was well received and she made a full recovery.  


In the real world, she was transported to the hospital. When she realized she would be sitting in the waiting room for hours, she AMA'd and called 911 again to transport her to the next hospital. Fucking shit person.
[f88xwbc] (score 4, diepte 2) i didn’t have a radio on me at the time or else i would have...still a probie so i didn’t feel too comfortable questioning my very seasoned crew on their decision to enter the house. needless to say, i entered last. ive still got questions, though, believe me.
[f890ou7] (score 4, diepte 3) I encourage my EMTs to bring up concerns to me. Usually I am focused on something else and if you're catching something basic or weird to you then say, "Hey B-Kow, what about this...etc?" It has been helpful in a few situations but there has also been many teachable moments for the newbies.
[f891mdq] (score 4, diepte 5) Oh definitely. We are not police and we don't handle intruders. In a different (but similar) situation where there was an intruder then one or all of you could have been killed.  


Your lead is probably a seasoned medic who is either more comfortable in the job or numb to scene hazards due to their time on the job. But I'm willing to bet that if you spoke up and suggested calling for law enforcement during that call, they would have agreed with you once they thought about it.
[f8aiggr] (score 4, diepte 1) Got called at 5am for a woman who didn't sleep the previous night because she wasn't sure if she took her temazepam. Asked me what to do. Told her to take a nap, but she refused saying she didn't want to sleep through the day. So I told her to stay up, but then she said she didn't want to get tired.

How the fuck does any of this work anymore?
[f894rxb] (score 4, diepte 0) This is why we burn out.
[f89yp5k] (score 4, diepte 1) I wish I lived in such a place where somebody, not necessarily me but somebody could say No. fuck right off. You don’t need a bells and whistle ride to the hospital for that.

Abdominal pain may need to be evaluated, true enough; but the the time saved by the ambulance ride is typically meaningless for you, but might just be the deciding factor for the choking baby in my first due that has to wait for the second due ambulance while I’m hauling you in for your gastroenteritis.
[f89iajs] (score 3, diepte 9) Or taco Tuesday
[f89gz1f] (score 3, diepte 1) Probably had to go to the bathroom hung over.
[f893er7] (score 3, diepte 3) I heard that phrase and I immediately called to the hospital to alert to a cardiac event incoming and to prep all available resources. She got lights and sirens transport of the highest degree.
[f88v5jb] (score 3, diepte 1) Medicaid
[f88w2ux] (score 3, diepte 1) Lol did you ask dispatch if they sent the wrong boys?
[f8928iy] (score 3, diepte 7) Even if it's a silly thing that you're feeling unsure of, pull them aside (not in front of the patient) and let them know. It lets your crew know what your vining and also lets them know you're not on autopilot and actually thinking while on calls
[f88obmo] (score 3, diepte 0) You don’t need an ambulance
Don’t ya tell my feet, my achy breaky feet, I just don’t think they’d understand
[f89565b] (score 3, diepte 0) When I called the ambulance for my brother who was having severe abdominal pain they wouldn't send one 🙄
[f8c083e] (score 2, diepte 6) Sorry ma'am. That's an emtala violation and we will not be doing that. If you'd like, you can go back in and wait your turn.
[f898tdt] (score 2, diepte 1) Yup, was just gonna say this. After 0000 and foot pain? 90‰ chance they're an urban outdoorsman. If the temperature is falling? 100‰ they're cold.
[f890y7x] (score 2, diepte 2) I was in a bad enough mood today already 😩
[f890x6e] (score 2, diepte 4) do you think that i had a valid concern in that situation? i think back to it sometimes and really believe i should have said something. the “scene safe” alarm bells were going off in my head for sure.
[f8920m8] (score 2, diepte 6) okay, thanks a lot! i’ll definitely be more vocal about stuff in the future.
[f893a4i] (score 2, diepte 7) It's similar here where I work. We get dispatched to a lot of calls that fall under the "Police Matter" category. I assume it's because we are a fire/ems department and typically an engine crew goes with the ambulance. But fortunately, if we feel the need to call for law enforcement they are quick to respond and vice versa. We often get dispatched to a PD units location because it turned out to be an EMS call.
[f8tuows] (score 2, diepte 2) I have long felt that as soon as the sun sets, everyone in my service area loses any and all coping mechanisms. I’m truly glad that it appears to be the same everywhere
[f894zrm] (score 2, diepte 1) meanwhile,

80 year old female with seizure, no history of.  Alpha.

65 year old male, obese BMI 40+ don't bother dispatching fire, one crew will do.
[f8955jz] (score 2, diepte 2) No units available because ALS abd pain
[f89ghmk] (score 2, diepte 0) How come you're using explorer when you have chrome?
[f8tcxhj] (score 1, diepte 2) Listen. Craniorectal Inversion Syndrome is a real problem that affects thousands negatively. We need to be treating their pain, not making fun of them. This is the problem with healthcare providers in this country, there’s no empathy. 

Max em out on the fent, then high flow diesel bolus to the hospital to treat acute hypoturkeysandwichia. Hopefully one day our protocols will allow us to carry turkey sandwiches in our med kits, eliminating the need to risk our pts or ourselves in hot transports to the hospital due to our inability to start life-saving care in the field
[f8ro9ph] (score 1, diepte 2) 🙏🚑
[f8977a0] (score 1, diepte 4) /me raises eyebrow

Really? And how was that received?
[f892acn] (score 1, diepte 6) Could also just be a common thing in his agency. At my old job, we fairly regularly went to calls that are more the responsibility of the police, but there wasn't anything to be done (other than quit, I suppose). The way our dispatch worked, calls went to PD (or SO if out of the city) who then transferred calls to us. Once our dispatch center received the call, they had to send someone, and the police wouldn't take the call back once they passed it off.
[f88o4k3] (score 1, diepte 0) Did he stick a knife in it? If not, fuck him.

=== THREAD 15gclyq ===
SUBREDDIT: r/TalesFromYourServer
DATUM: 2023-08-02  SCORE: 71  REACTIES: 74
TITEL: Gross question — how do you prevent/treat blisters on your feet?
POST (source_id=post):
I worked 2 12-hr doubles in a row this past weekend. I got in the shower this morning, looked at my feet, and wanted to cry. My toes are so swollen and have blisters all over them; they look and feel like shit. How do you prevent blisters overall? And how do you treat them when you do get them? I’m scared because I work the next 7 days in a row and I fear for my toes 🥲

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[juhyr5f] (score 66, diepte 0) Go to the drug store and get some moleskin.  You cut them into shapes that you apply to your feet, where the blisters are occurring.  They are sticky, and will stay attached, even through a 12 hour shift.  

When you are at home relaxing or sleeping, elevate your feet by a pillow.  It will help reduce swelling.  

Drink water.  

Try to get footwear that's a little more relaxed...  I gained a size and a half in shoe size in the biz, over 10 years.  

Water.
[juiw2ob] (score 27, diepte 1 OP) I have fallen victim to dehydration recently. I bet that plays a big factor, thank you so much!!! Chugging a water bottle with my feet up now!!
[jui7f76] (score 22, diepte 0) Sprinkle cornstarch or baby powder on your tootsies before putting socks on and make sure your feet are DRY. Get socks that are specifically designed to help with sweaty feet. Bring an extra pair of socks with you on doubles and change them out on your break, as well as sprinkle some more powder on your DRY feet.
[juhyfs6] (score 13, diepte 0) Compression socks will help with the swelling, and put a bandaid around the current blisters to help them heal.  Better fitting shoes will prevent blisters in the future
[juixese] (score 13, diepte 1 OP) I 100% need better shoes — wearing crocs until I get my new pair of non slips, and they’re rubbing my poor toes raw! Good idea on the extra socks and cornstarch, I’m def giving it a try tonight!
[juiu3cs] (score 11, diepte 1) I agree with everything you said, and would add that - at home - keep the feet bare as much as possible.
[juj2z8n] (score 10, diepte 2) I cannot wear crocs. They give me blisters too. I'm not in the industry. 

Walmart sells non skid shoes for a decent price. I'd buy some while saving for better shoes.
[jui9hu6] (score 9, diepte 0) Invest in good socks and shoes. If they're worn out, they'll stretch and rub which will cause skin irritation and blisters. 

For treatment, moleskin is good to cover them but like most anything, prevention is the best treatment.
[jukfjth] (score 8, diepte 2) You being on your feet all day can make them swell, a little, or a lot. You need to make sure your shoes are sized for this swelling so that they do not rub blisters on your feet. You do not want them to be so large that they are loose as that will also cause blisters, just maybe a 1/2 size to have a little room. Also wear 2 pairs of socks and make sure they stay dry. If your feet sweat enough to make them moist then have another pair or two to change into.
[jui47vr] (score 7, diepte 0) Switch to a fresh pair of socks on your break.
[juihazd] (score 7, diepte 0) your feet swell while you are your feet for hours.  You need better shoes before your next shift.  Don't skimp
[jujfgfh] (score 5, diepte 0) I don’t have any experience as a server but i have dealt with a lot of blisters from walking 10-20 miles in boots.
First off try not to pop them i know it’s hard but it’ll help you in the long run
Moleskin helps especially if you happen to pop an old blister.
Invest in good socks, change your socks throughout your shift if possible.
If it’s feasible, a pair of silk socks under cotton or similar material can help wick any moisture if your feet get wet or sweaty.
What kind of shoes do you wear? Is it possible to get or wear different ones?
[juhxkdx] (score 4, diepte 0) Inji toe socks help me prevent them
[jujo84d] (score 4, diepte 1) KT tape works fantastic for me when I work our city’s convention or when I buy new shoes… my right heal always blisters with new shoes.
[jujo3gl] (score 4, diepte 2) I love Crocs for casual wear but they are absolute shit for hard floors or more than a few hours of work. Buy better as soon as absolutely possible.
[juj2zvd] (score 4, diepte 0) Don't wear cotton socks.  Go to a running store and actually get fitted for proper walking shoes, they will make all the difference in the world.  I'm guessing your shoes are too small (maybe even too narrow) especially after being on your feet for a few hours.
[junlhb3] (score 3, diepte 1) Mole skin is a bajillion times better than bandaids. As a Walt Disney 10 mile walker in a day ouch.   
but moleskin saved the day and the next day did t get more and the ones covered held up ok.

now what shoes are you wearing and do you rotate? You may need to change your socks during shift if they get sweaty. That just compounds issues. Good luck!
[juit3m6] (score 3, diepte 1) Tootsies hehe that's adorable
[juj2blb] (score 3, diepte 1) Good socks and changing them is the best play. Learned that in the desert section of the PCT quickly.
[jujq1zg] (score 3, diepte 1) I can have tennis shoes at my work. I buy the mid range ~100  USD running shoes. They're light weight, breathable, and comfortable. Only real downside is they only last about a year. But that's a small price to pay for feet that don't hurt and don't stink after a long day.
[juikt34] (score 3, diepte 0) Compression socks, supportive footwear and my favourite trick, massage vaseline into feet before putting on cotton socks. Prevents blisters.

Also bring a change of socks for during a long shift, can actually make a difference.
[juitj6u] (score 3, diepte 0) Blisters are usually caused by friction and shear. In a well-fitted supportive shoe and sock, your foot shouldn’t be rubbing, it should all move as one ‘package’. If you are quick and notice a particular place rubbing, tape or moleskin can help by giving a separate surface the friction is applied to. Obviously you don’t want to tape over blisters.
[juj9x7f] (score 3, diepte 0) Not a server, but it's not unusual for me to spend 12 to 16 hrs a day all week in my work boots. If you are wearing socks,  make sure they are well fitting, also take  a minute every couple of hrs to take your shoes off to fix your socks and let the Dawgs breath a minute lol  even better bring fresh socks to change into at some  point you'd be amazed how much better it feels even if you're putting the same nasty shoes.back on.
[jujb6g9] (score 3, diepte 0) Old military trick...2 pair of socks.  Base layer is thin nylon or similar, second layer is slightly thicker and moisture absorbent.   The socks will rub against each other, instead of your foot rubbing agains the shoe.
[jujdf86] (score 3, diepte 0) Good shoes that fit well
[jujz5w5] (score 3, diepte 0) Order a pair of Hoka Bondi SR shoes. I found out about then from a nursing sub here.

At $175, they are expensive (I used after pay to lessen the blow to my wallet), but holy hell, are they comfortable.

There was no break in period. I did have to adjust my gait as the shoes help you walk correctly. I've even had a lot less back pain and no foot pain when I first stand up in the morning


The shoes have the American Podiatric Medical Association seal of approval.

If you have wide feet. The toe box is nice and roomy and the sides don't run against my been-a-server-for-30-years bunions. 

https://www.hoka.com/en/us/mens-walking/bondi-sr/192410928682.html?&utm_source=google&utm_medium=ppc_brand&gclid=EAIaIQobChMIi_HBnJ-_gAMVrBCtBh0_DwdPEAAYASAAEgJJP_D_BwE&gclsrc=aw.ds
[jukf10y] (score 3, diepte 0) I was taught in medic school not to pop blisters as the blister helped protect the open wound. If it does pop, then keep it clean and treated with an antibacterial type of topical. It sounds like to me that you need some much better shoes that fit properly.
[m2xqmew] (score 2, diepte 2) YES. Disney is KILLING my feet rn! You’re amazing for 10 miles. Did 8 ish yesterday and 5 today and I’m dying
[juj9s8z] (score 2, diepte 2) Also when you wash them off after work run some Vaseline on the blister areas.
[laffxa5] (score 2, diepte 1) Definitely cornstarch. Baby powder often has fragrance added with can be irritating to broken and blistering kin.
[juiip1n] (score 2, diepte 0) When I was working the one thing I never felt bad about spending money on was good fitting shoes. I was on my feet and moving all day every day. The only time I was sitting was when I drove to the job site.
[juzassr] (score 2, diepte 1) this is awesome, thank you! 

I'm back in retail after a long break from being on my feet all the time from various jobs. I think I'll treat myself to some new, thick socks. (my poor feet deserve it! we have a cement floor.)

I used to always get new socks for long camping vacations and I totally remember how much it can help.
[juil0io] (score 2, diepte 0) Squirrels Nut Butter. Stuff is amazing 👌
[jv2190u] (score 2, diepte 1) fun fact: superglue is surgical glue!
[juj8lbz] (score 2, diepte 0) I strongly recommend a brand of clogs called Sticky Shoes. They are made in Brazil, but they have a US branch, and you can find them online from Walmart for about $50. 

A year ago, I was working BOH, and a woman from FOH gave me a brand new pair of these shoes that she didn't want. Let me tell you, these shoes are so damn comfortable and lightweight. They are true to size and fit like a glove. They're made of rubbery material, so you can easily clean them with a damp cloth. I have gotten compliments on how cute they look. 

I have suffered from arthritis for years. I hate Crocs and timberlands as they feel too big, loose, and clunky. I used to wear Danskos, but they can also be heavy, plus you can easily roll your ankle if you aren't careful.
[juj9msq] (score 2, diepte 0) not for blisters but the feet swelling/pain: Dr Scholls inserts. they’re like $50 usd but they’re SO worth it, my feet felt instant relief the first shift i used them. i recommend find one of the machines and stepping on it to find out exactly which pair you need!
[jujkzql] (score 2, diepte 0) Invest in some good shoes. I’d go somewhere where they measure your feet to find you the perfect fit. Also high quality socks.
[jujlg8z] (score 2, diepte 0) The moment you feel a hot spot developing, take a bathroom break and put some moleskin or a bandaid on it. It will prevent it from progressing to a full-out blister.

When you get home, put your feet up above the level of your heart, such as on the arm of the far end of the sofa. Prop up with more pillows if needed. For bonus points, lie down on the floor with your butt up against the sofa and your legs on the seat cushion. Your hips and knees should be at a 90° angle to each other. Tuck a pillow or blankets under your legs if they aren't because your sofa is too low. This is excellent for your lower back and your feet. 

After you've rested for a bit, and while you're still on the floor, do some gentle and slow stretches. Point, your toes for the count of 5 or 10, and then flex your feet for 5 or 10, repeat several times. Rotate your feet in circles in both directions and then write out the alphabet with your toes in the air... A, B, C.... it creates the full range of motion.

Give yourself foot baths with Epsom Salts and get yourself a tennis ball, and roll your foot on it to stretch the muscles and ligaments on the underside of your feet. End with a good lotion.
[jujntgp] (score 2, diepte 0) Baby powder in shoes works for me.
[jujpef4] (score 2, diepte 0) If you feel a hot spot (like it's starting to burn) immediately put balm on and cover that area with something so not isn't rubbing
[jujqsub] (score 2, diepte 0) Bandaid blister bandaids (they're supposed to stay on for a few days,  allowing your skin to grow back).
But also, trail toes on your friction points (not just feet!)
[jujt3as] (score 2, diepte 0) Try an anti-chafe stick. It reduces the friction at the point where your shoes rub. Also, baby powder can clump and make your feet feel worse, cornstarch is a starch (sugar) and can put you at risk for fungal infections.
[jujwk3e] (score 2, diepte 1) As a fat old man, I literally can't recommend anti-chafe stick enough! The best is "Body Glide" for runners, close second is "Gold Bond" brand. BG might be hard to find, check running stores, but GB is found in the first aid aisle at Wally World. It also cost about half of what BG does. Both brands look like deodorant stick, and can be used ANYWHERE one might suffer from chafing. It's worth every penny.
[jv2y1jo] (score 2, diepte 3) It is, a little. I think about the same, maybe a bit less. I find it odd that it does feel kinda sticky, but does protect very well. Technically, I guess it dries out? Anything is better than plain old petroleum jelly. You can't wash that off at all! And the GB last too. I used it while hiking, put it on first morning, still good 48 hours later.
[jv46ly3] (score 2, diepte 5) Noooo! If it's above 30°F, my legs must be free! They must breathe! I'm glad you found what works for you, anything it takes to stay active 

I wish I could remember who I got it from, I've been using it forever. Now my whole family uses it.
[jv21tma] (score 2, diepte 1) Lush makes a foot powder with tea tree oil. it's the best! I got a big fluffy face powder brush to apply it. it doesn't clump nor does it have corn starch. it's not cheap, but just like fancy salt you don't use much each time.
[juk5rf0] (score 2, diepte 0) Get some foot powder and blow a couple times into your socks before putting them on.  You want your feet dry af at the end of shift.

Comfy insoles (yeah, the gel ones) help, too.

Give yourself plenty of time to air the dogs out when you get home.
[juka4y9] (score 2, diepte 0) Wear shoes that fit. Get some moleskin for the ones you have
[jukqcb3] (score 2, diepte 0) Compression socks are key. 
Moleskin can also help a lot. 
Make sure your shoes aren’t too tight (lots of shoe stores will measure your feet to make sure you’re in the right size, say to them that you’re a server and are on your feet all day, also go in the afternoon/evening because that’s when your feet are the biggest).
[jukr76g] (score 2, diepte 0) You have a ton of good advice already, but let me add that getting one of those mechanical foot messagers off Amazon is amazing. I dot get blisters, but I do have pain and arthritis in some of my toes and this thing is FIRE. Mine has a heat setting as well.
[jul25lx] (score 2, diepte 0) I’m wondering if you have the right footwear! I’ve gotten blisters before and it was from either shitty footwear, or shoes that did not fit correctly. Right now, I’ve been wearing Snibbs and am on my 4th pair. These are pricy, but not outrageous (imo). I also like clogs such as Danskos (similar price point) but they take time to break in: I’ve heard two hours the first day and then switch to your old shoes. Then four hours the next day, switch out, etc. In the meantime, the moleskin should help until you can get some better footwear. :)
[juopcd6] (score 2, diepte 0) There are blister pads to wear over open wounds in the first aid sections of stores. But going forward find some good shoes and don’t forget to save your receipt to write off for work expenses for taxes!
[julwuok] (score 1, diepte 2) Dump the crocs and get some shoes that fit and give your feet some support. Support for your feet  avoids all sorts of other problems with ankles, knees, hips, back, and neck, and you’ll be happier at the end of the day. 
There are lots of options out there for shoes that support your feet.
[lag60bp] (score 1, diepte 2) I only get the sensitive skin kind die to having sensitive skin, but you're right. Cornstarch is the same thing. I get baby power more for the easy open close top than anything else lol
[jv225q8] (score 1, diepte 2) Yes, thankyou, somehow I’m getting downvoted
[jv224mk] (score 1, diepte 1) For those downvoting me I actually just did this for an injury on my foot and it worked great.
[juzaxo0] (score 1, diepte 1) my go-to is the vinyl bandaids. they provide just enough slip to protect it from getting worse.
[juj8lkx] (score 1, diepte 0) I strongly recommend a brand of clogs called Sticky Shoes. They are made in Brazil, but they have a US branch, and you can find them online from Walmart for about $50. 

A year ago, I was working BOH, and a woman from FOH gave me a brand new pair of these shoes that she didn't want. Let me tell you, these shoes are so damn comfortable and lightweight. They are true to size and fit like a glove. They're made of rubbery material, so you can easily clean them with a damp cloth. I have gotten compliments on how cute they look. 

I have suffered from arthritis for years. I hate Crocs and timberlands as they feel too big, loose, and clunky. I used to wear Danskos, but they can also be heavy, plus you can easily roll your ankle if you aren't careful.
[jv213ap] (score 1, diepte 1) I find the plastic bandaids are the best, because they cover the blister and slip inside socks instead of dragging. as soon as I notice a potential blister I slap one on.
[jv2255p] (score 1, diepte 2) But plastic bandaids fall off so easily. Cloth stay on for days
[jv2ufsc] (score 1, diepte 3) plastic gives the slippy tho. the cloth ones stick to my socks. and you should be changing them anyway.
[jv220st] (score 1, diepte 2) BG made me feel unpleasantly sticky instead of feeling glidy. is GB better than BG? or is it sticky too?
[jv3ihq7] (score 1, diepte 4) I've given up and just wear leggings.
[jujtaej] (score 1, diepte 0) Your feet should not be swollen and blistered after a shift, definitely need to change your shoes, it could be the toe box is too small and creating a lot of friction.   
Getting shoes that are comfortable for you to wear (even after 10 hours) and some compression socks should help you. Compression socks would help with circulation. Also the palms of your feet have to be supported, so like flat shoes like vans for example, would create a lot of soreness on your bones there. I used to do maeathon shifts back to back but the least of my complaints would be my feet, having good shoes allows you to work and perform better.
[juk6lrd] (score 1, diepte 0) I never have had blisters but my feet swell by the end of my shift which was making the pain in my feet and shins worse. What saved me was going up a half size and getting wide shoes. Also don’t cheap out on socks and the shoes themselves.

Make sure you are letting your feet dry out after your shift. Before being in the industry I wore socks all the time at home but now I am religiously barefoot or in house slippers so my feet have a chance to breathe. When I did get blisters it was because my feet were getting too sweaty. Also I ended up with athletes foot.
[jul6smi] (score 1, diepte 0) Not really a specific diagnosis, but make sure you invest in your feet. Drop some money on some perfectly sized shoes.  Give them a rub down, soak them in Epsom salts (reduces inflammation and make sure you spend some dedicated time with your feet up for the blood flow. A foot injury, even severe blistering, is a devastating injury for a server. Best of luck.
[jum77jl] (score 1, diepte 0) Invest in a good pair of orthopedic shoes. Your feet, back and future self will be eternally grateful
[juw77ds] (score 1, diepte 0) I wear two layers of socks when I have to be on my feet all day—the “inner” layer are super-thin socks I picked up in a camping goods section and are designed to wick moisture _and_ reduce friction from the outer layer of socks.  Blisters suck.  I hope you heal quickly and safely.
(5 reacties met lagere score weggelaten)

