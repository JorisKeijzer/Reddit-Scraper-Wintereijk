# Label-batch batch_0033

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
Schrijf het resultaat naar `batch_0033.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: mms7dy, 2vk0u0, 1iid1j5).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD mms7dy ===
SUBREDDIT: r/ChronicPain
DATUM: 2021-04-08  SCORE: 184  REACTIES: 52
TITEL: Manual labour construction has destroyed my body from multiple hernias, bad knees , bad shoulder fucked feet and hands every waking moment is pain and I’m only 34
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gttkzle] (score 21, diepte 0) I'm in a similar situation on the opposite end of the spectrum, from being all but fused to a desk.

It seems like we really need some sort of occupational rotation system, or maybe even *vacation time.*
[gtuclbb] (score 20, diepte 1) > maybe even vacation time.

Laughs in American
[gtud4py] (score 19, diepte 0) But you are still young, wait til your older! 

Hear this all the time. Been fucked up since I was 35. Made it worse driving truck. It was true, got worse as I got older. But apparently when you are younger it just 'isnt the same'.
[gttceel] (score 12, diepte 0) Yeah, that sounds like you need to stop before you permanently disable yourself. Maybe try to get social welfare and try to find a different way to spend your time?
[gtul6kx] (score 12, diepte 1) Found the non-American.
[gttwlsv] (score 12, diepte 1) “Have you tried yoga?” is now “Have you tried Keto?”
[gtu4r99] (score 10, diepte 0) Im 18 and my back is hurting every single day, cant work with what i want because straining it makes it worse. I dunno if i can live a normal life. Hope you get better
[gtv0qh7] (score 9, diepte 0) Im 35, ive broken my right leg, right wrist, torn left mcl, got 2 herniated discs in my neck & 3 in my lower back, had 4 surgeries on my left shoulder & just had surgery before Halloween on my right shoulder for torn labrum & bicep. My dr thinks i should be pain free now. I do hvac & honestly feel like i have to give up at this point cuz the pain my bodies in on a daily basis.
[gtu99wr] (score 7, diepte 2) Eating keto and doing yoga isn't going to undo hernias popping through muscle walls or shave down heel spurs.  That said, eating low carb (under 100g carbs/day) helps me some with musculoskeletal pain, even if I'm not losing weight from it.  (I have no idea what this guy is talking about with respect to mitochondria and carbs.)
[gtuesf9] (score 6, diepte 3) Full disclosure, I follow the keto diet and DO recommend it to people if they’re looking for advice or suggestions. It’s not a magic bullet but helps me deal with chronic pain & fatigue to a small but significant degree, right?

Your tone and delivery are bringing the “haters,” not your message
[gttydd5] (score 6, diepte 0) I'm sorry that happened to you and I hope you get some peace.
[gtv5mjt] (score 6, diepte 1) Samee and im only 17.
[gtu795j] (score 6, diepte 0) 💔 Not everyone can do or is  willing to do this kind of work. I hope you get some relief.
[gtv0y55] (score 5, diepte 0) I’m 35 and waiting for death
[gtvbt2h] (score 4, diepte 2) I honestly feel like my body is getting to the point where it's just going to stop functioning properly lol
[gttvpxa] (score 3, diepte 1) Yeah.. sounds like thus needs more details or at least a link or something
[gtv6xy0] (score 3, diepte 3) You seem like such a compassionate person!
[gtuae38] (score 3, diepte 0) Do you have a connective tissue disorder like EDS? If so, don’t feel bad for having been active this would have happened no matter what.
[gtufd6x] (score 3, diepte 0) That pretty Poppy of Mercy
[gtv7zco] (score 3, diepte 1 OP) Ya I’m a carpenter I wish for death some days
[gtvti8b] (score 3, diepte 1) Fractured spine and resulting nerve damage and never ending pain 24/7. Similar line of work here, haven't been able to work since the injury almost 3years ago and the amount of people that treat me like im bullshitting makes me want to break their back and see how they go lol
[gtteeq0] (score 2, diepte 0) depending on what is fucked, there may yet be hope for repairing/replacing things that are gone. but regardless, you kinda need to find a new job or some sort of assistance program while you figure out the best thing to prevent permanently disabling yourself
[gttf2z3] (score 2, diepte 0) That sucks sorry friend!!
[gttvgjt] (score 2, diepte 1) That doesn't make any sense
[gtulmz9] (score 2, diepte 3) A peer-reviewed study might be better received.
[gtva0m0] (score 2, diepte 3) Could you link any solid sources?
[gtuli4b] (score 2, diepte 3) Ditto. Now sugar makes me sick to my stomach. And these hard-liners who think keto is under 25 grams a day, that it's either on or off...don't understand how the liver and brain and ketones work.
[gtx3t4c] (score 2, diepte 5) There's some crazy, unsupported magical thinking going on there. Like "if you're not below 40 (or 20 depending on the rando), you're keto switch is NOT turned on." 

Yeah, it's complete bullshit. On paleo for about 5 years, I got test strips that showed that I was in ketosis every morning without even counting carbs, just avoiding white potatoes, flour and sugar. Eating as many veggies as I wanted. Eating a baked sweet potato every few days, and just one fruit every day or so. When I did count carbs I was between 60-150 grams. Still making ketos before breakfast every day. 

I'm ok with losing 3 pounds a week instead of 5 pounds a day or whatever ridiculous weight loss level they insist upon. 

So, I hear ya. *Screw those guys.*
[gtv0zuo] (score 2, diepte 1) how do I downvote this twice?
[gtu9hdi] (score 2, diepte 0) Look into prolotherapy. I wasn't able to walk a year ago. Old football injuries left things in a bad place. Prolotherapy, coupled with PT, can be very restorative. I hadn't heard about it until I lucked into a new PT office that also has a non-surgical ortho who does it.
[gtvcfu4] (score 2, diepte 0) I'm not 34 but I feel you on this man.
[gtvge6k] (score 2, diepte 0) Dog groomer, 33. I feel this on a spiritual level. Different body parts troubling me, but they still all result in constant pain.
[gtvx2r4] (score 2, diepte 0) Same. Luckily I finally found something that actually works as good as opiates and is legal (probably not for long) and I’m not talking about kratom. Kratom was never strong enough for me unfortunately
[gtwad1y] (score 2, diepte 1 OP) Share please
[guey4te] (score 2, diepte 1) Could you pls pm me too? Very interested. Thank you.
[gtvgxa5] (score 1, diepte 4) When I was following keto, the rule was no more than 20 grams net carbs per day.  Let me tell you, that was HAAAAAARD.  Even vegetables have carbs.  WTF.  Vegetables don't even taste like cake and ice cream!  How can they have carbs??? lol.

And woe is you if you complain about having gone over that 20 net carbs by 4 carbs the day before in a keto sub.  You're downvoted to oblivion while the comments roll in about how /r/keto doesn't allow posts about cheats.  Like, shit dude, all I had was an extra helping of cauliflower rice.  I haven't been on that sub in years, so I hope it's gotten better.
[gtvgygu] (score 1, diepte 1) Do excessive carbs make me feel shittier? Absolutely. But even on a keto diet I'm still in constant pain. Sometimes the pleasure of eating something sugary helps me forget that pain for a little while. 

Telling other people suffering chronic pain what they should do to get rid of their pain is unhelpful, and when people do it to me it mostly just makes me more depressed because I often don't have the energy to even think about trying what they recommend.
[gtvw7w4] (score 1, diepte 2) Dude thats rough! I missed 2 years straight cuz of 2 surgeries then went back, covid hit, got covid bad cuz thats my luck & then worked for 7 months & tore my other shoulder. The worst is people look at u like a piece of shit cuz ur injured & then immediately after ur not in a sling they expect u to be working!
[kz4ivjw] (score 1, diepte 1) I'm 33 waiting for 35 to wait for death
[kz657o0] (score 1, diepte 2) I'm 38 now
[l1gsjef] (score 1, diepte 3) Still waiting?
[gtvkbrv] (score 1, diepte 0) Sorry about your fucked body. 

  
When this post scrolled onto my screen, my first thought was "That is a fucking weird looking Bulbasaur."
[gtw88sb] (score 1, diepte 1) Dude please pm me if you can share, could use some alternatives to lyrica and opioids
[gxawwhp] (score 1, diepte 2) Hey. Just seeing this now. I’m sorry. I don’t check Reddit often. Email puretialab@gmail.com. Her name is Samantha. She’s super nice and really out to help people.
[gxawsol] (score 1, diepte 2) Hey. I’m sorry I am just seeing this now. I don’t check Reddit often. Email puretialab@gmail.com. She’s super nice and really out to help people
[gu1muni] (score 1, diepte 1) Is it those weird seeds? If it doesn't induce seizures I'm all in for it if you let me know!
Never mind... I think we are in the same boat. Or at least that's the one I'm likely boarding.
[gxavnyv] (score 1, diepte 2) Hey! I’m sorry I just saw this. I don’t check my Reddit often. Email puretialab@gmail.com. She’s very nice. Really out to help people
[gtwmkri] (score 1, diepte 0) I'm 35 and I've had a splattered disk pressing on the nerve.  I've had pain everyday for 12 13 years, I had to stop being a dairy farmer in 2017 cos the hospital visits were too frequent with me constantly push push pushing it till I snapped.
I'm prescribed codiene and morphine for the pain and fuck all works so yeah.... miserable and waiting to die to I don't hurt no more. Cant wait
[gu1mhjb] (score 1, diepte 0) My career in engineering and machining was turned into a stint when the army ruined my spine at the ripe age of 26. I hope I don't live to be 36.
[i817sgm] (score 1, diepte 0) I'm 46 and fucked after hernia got aches and pains all over
[gtu2r4t] (score -2, diepte 2) Google "low carb for chronic pain" and you'll get a ton of solid hits but here is one:

https://www.dietdoctor.com/is-a-keto-diet-the-best-natural-pain-reliever
[gtv1v07] (score -2, diepte 2) LOL have fun being inflamed and in pain
[gtu2zj0] (score -5, diepte 2) OK go ahead and be a hater. All you're doing is stopping people from accessing the clear reality that fasting and carbohydrate reduction are very clearly associated with reductions in inflammation and chronic pain
[gttmjjq] (score -15, diepte 0) Avoid carbohydrates- switch to carnivore. Carbs will exacerbate your mitochondria destroying itself and causing pain

=== THREAD 2vk0u0 ===
SUBREDDIT: r/goodyearwelt
DATUM: 2015-02-11  SCORE: 43  REACTIES: 52
TITEL: Review: Santalum MTO Service Boots w/ Unstructured Cap Toe in Black Horsehide Chromexcel
POST (source_id=post):
[**ALBUM After 1 day of Wear**](http://imgur.com/a/8FEBw)    
    
I would just like to state that this review is not an argument for or against shoe makers like Santalum who build shoes that replicate other shoe makers' lasts and models. This review is purely intended to inform those interested or curious on the build quality, materials, clicking, and customer service of Santalum. If possible I would like to avoid debating on authenticity and talk of that sort on this post, and stick to reviewing the construction and quality of these boots.    
    
About 9.5 weeks ago I ordered these boots from Santalum. I ordered their service boots in Black Horsehide Chromexcel with a full rubber sole, antique brass eyelets, and a plain cap toe. They told me it would take about 8 weeks, as opposed to their more typical 4-6 week turnaround time, to make these boots because they wanted to be extremely careful with more expensive materials, and they had to be very careful during the clicking and hand-lasting process. These boots are handwelted with Veldtschoen construction. The price was $220 plus $35 standard shipping (took about 1.5 weeks to arrive to Santa Clara California from Indonesia).    
     
Santalum's customer service is top notch in my opinion. Because of the time difference I knew they would always reply to my emails from 5:00 PM - 7:00 PM Pacific Standard Time Monday through Friday. They consistently answered my questions asking for updates in the manufacturing process and were accommodating when I asked to make changes. While they were in the clicking process I asked them to actually make the boots a cap toe version instead of plain toe. I also asked if they could make the cap toe completely unstructured and .5 inches shorter than their normal cap toe and they did it no questions asked. They asked for measurements on my other Santalum Cap Toe boots of where my toes hit so that the shorter cap toe would not crease oddly. The request I made that Santalum did not fulfill was no branding on the tongue. They said they don't remove branding. I was disappointed as I don't like wearing clothing with branding, but it is only an embossed logo and is high up on the tongue.    
     
AllOverall I think the quality is pretty good. The pictures in this album are after a day of wear.The stitching seems pretty neat, and the I don't see any flaws in the welt. There are some inconsistencies in measurements on the boot it seems but none noticeable. The clicking on the vamp is superb and the boots have just a small amount of very fine creasing in normal spots. However the creasing is worse on the heel counter and the ankles of the boots. I am not too upset about this because I only paid $255 for these boots and the clicking is bette than on my rancourts. The Horsehide CXL is a very thick, strong feeling leather and it feels very durable.    
     
I am a little disappointed on the fit of these boots. I sized the exact same as my last pair of Santalum Service Boots; however, these are a little smaller and are tighter on the sides of my feet. They are slighty uncomfortable right now, so hopefully the leather stretches a little bit and softens up, as the boots are still quite stiff.    
    
Overall I think that these boots are worth $255. I may have gotten lucky with clicking because I was one of their first customers who had boots made out of their black horsehide CXL, but I am happy with the product I received. The boots have a very nice looking low profile and slim toebox, and the unstructured toe should break down nicely.    
    
Let me know if yall have any other questions. There are additional pictures of some of my other boots and things in my imgur gallery if anybody is interested as well.    
    
[**BONUS: Family Pic**](http://imgur.com/KIA9SJb)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[coiiu7i] (score 6, diepte 4) Well, the 3 things you said they have in common are all aesthetic things, which arguably make them Tricker's-esque in my opinion.
[coihuiy] (score 4, diepte 0) Since first seeing them, it seems Santalum have been producing the best quality boots coming out of Indonesia. These look great. Almost Tricker-esque.
[coihx4z] (score 4, diepte 1) What makes them look like Trickers to you? They look like a Viberg "emulation" with the stitchdown construction and long tongue.
[coihsaw] (score 3, diepte 0) If this is horsehide chromexcel, how are they cutting such big panels while keeping thick leather? Correct me if I'm wrong (/u/Deusis or /u/rev_rend) but wouldn't thick horsehide chromexcel have to be from the strips, which are too narrow to cut such big panels? And FQHH, which is large enough for big panels, is much thinner?

Just trying to clear up any confusion or misconceptions that I have.
[coiti75] (score 3, diepte 2) Hey would you compare Sagara to Santalum?
[coijuin] (score 2, diepte 1) What /u/Deusis said. 

Role Club says they have to hand select strips to make their engineer boots. So you can get a pretty big piece for a boot from them. Of the 25 or so strips I have, fewer than half (probably fewer) would be big enough for boots.
[coj1uc4] (score 2, diepte 3 OP) I like Santalum's last shape better for sure, but I bet if you took every single boots made by sagara and santalum i feel like sagara's qc would be better. But both of my santalum boots have been 1st quality, so I can't complain. I love my Sagara boots, but I think for 30 dollars less, I like my black Santalum boots more.
[coiija9] (score 2, diepte 2) It was mostly in reference to [my own Tricker's](http://imgur.com/8cKKnKr)
[coiio79] (score 2, diepte 1 OP) I sent them an email at santalum.indonesia@gmail.com
[coiiuxx] (score 2, diepte 0) Man these look great, thanks so much for the review and pictures. Just shot them an e-mail with a price quote for the exact same boots but in regular brown CXL. Might skip exchanging my Thursdays in another size and just return them altogether, and get a pair of Santalums instead.
[coij9yx] (score 2, diepte 1 OP) I think you would be getting a much better constructed boot from Santalum having returned some thursdays myself
[coiqmuo] (score 2, diepte 1 OP) When they break in they are pretty comfortable. I don't think they're any different than your standard red wing or wolverine 1k but they won't be as comfortable as whites or nicks
[cois1b1] (score 2, diepte 0) Nice, I was talking to them for a pair in darkbrown CXL and they sent me some pics of yours to compare haha.

I'd totally get these but they'd cost me $340 Canadian or $235 for a local leather, which is just brutal. 

They look pretty close to Vibergs though... damn
[coisiqz] (score 2, diepte 1 OP) Oh damn it is tough being a Canadian lol. They definitely have the look I've wanted.
[coj1pll] (score 2, diepte 3 OP) i have only handled 1k's and red wings and not owned them, but the leather on these is thicker, and the clicking looks better than what I have seen on a lot of 1k's and some red wings. The stitching has been neat on both of my santalums and the construction is really solid. They have a full leather insole and footbed, not fiberboard, and they are handwelted. I believe they have a steel shank as well
[coj29s2] (score 2, diepte 5 OP) i would think so but I do not know how these would wear over a long period of time, so no garuntees, but they look really promising in that regard, they may need a reheel eventually with a denser material but i think they will wear very well
[coj4ggo] (score 2, diepte 1 OP) i would say that Sagara's are a very solid boot and their in house leather is really high quality, especially their aniline dyed black, brown, and oxblood pull up. I have not tried Santalum's in house pull up, but there work with chromexcel is really good. However, I prefer Santalum's lasts and for $255 shipped as opposed to $285 shipped for Sagara, I prefer Santalum. The construction of both is very solid and they both, in my experience, have good clicking. To me it comes down to preference in their aesthetic styling. If you want that viberg look, I think Santalum is the way to go.
[coj4qtx] (score 2, diepte 2) Thanks very much for getting back to me. Just to check: does Santalum provide a PDF full of MTO optins like Sagara does?
[cojp62t] (score 2, diepte 3 OP) No you just kinda have to ask what they can do
[coih11p] (score 1, diepte 0) They look good for the price, thanks for sharing.
[coih7e0] (score 1, diepte 1 OP) my pleasure
[coihx27] (score 1, diepte 1 OP) That is knowledge beyond mine, but when I emailed them, I asked to clarify if it was normal cowhide CXL or horsehide and they repeatedly referred to it as horsehide. I wonder if there was some miscommunication between Horween and them.
[coiijwg] (score 1, diepte 1) It depends on how big the dies are for their boots. Theoretically some horse strips can be almost 1 - 1.5' wide (that I've seen) at the widest point so it is possible to be the thicker 5-7 oz strip horsehide leather.
[coivdob] (score 1, diepte 2) Dude has a pic of horsehide Thorogoods on a strip of horsehide:
https://dontmournorganize.files.wordpress.com/2012/05/5152092.jpg
https://dontmournorganize.wordpress.com/2012/05/15/horsehide-laces-for-horsehide-boots/
It looks just about big enough to cut the boot panels out of.
[coihvp0] (score 1, diepte 1 OP) I have to say I am quite pleased with them. They have stretched a little more and now fit fine.
[coiipol] (score 1, diepte 3) They are black with a natural colored welt and cap toe but I don't see a similarity beyond that (broguing, gyw instead of stitchdown, 360 degree welt)
[coiidie] (score 1, diepte 0) They look really good. You're on their facebook too. How does one go about ordering?
[coinqua] (score 1, diepte 0) i saw they posted these on their instagram. i have a 15% discount on my next pair and you just made me most likely spending my next paycheck on a pair in brown horsehide... thank you(?)
[coiqncl] (score 1, diepte 1 OP) Always glad to help somebody spend money. :)
[coj45n4] (score 1, diepte 2) They just contacted me with a New type of leather they are receiving next week. Dark brown Buffalo hide, it looked amazing on the picture but I have no experience or knowledge about Buffalo hide...
[coj4f32] (score 1, diepte 3 OP) wow that could be really cool. Search buffalo on this sub and you should see some cool makeups. Do you know where they are sourcing this buffalo leather from?
[coj4gh5] (score 1, diepte 4) they just made sure it was not from horween, but from a small tannery in the states. they had tan, dark brown and burgundy available from next week. they all looked amazing
[coj4kps] (score 1, diepte 5 OP) care to share pics? this sounds really cool
[coj4mf0] (score 1, diepte 6) made an [album](http://m.imgur.com/a/egNUm)
[coj4n0o] (score 1, diepte 7 OP) i really like the light brown
[coj4npk] (score 1, diepte 8) i was looking at the dark one, but im going to spend some time considering. might seem a bit too contrast-y
[coj4o2v] (score 1, diepte 9 OP) id love to see them on a boot for reference
[coipvhs] (score 1, diepte 0) These look great. I can't wait to buy my pair when I sell my RM's so I have the money. How are they comfort wise? I'm planning on having these and my other RM'S on duel rotation for my placement, which is pretty much 9-5 standing.
[coiro0r] (score 1, diepte 0) Looks like they did an excellent job with the clicking.
[coiry1q] (score 1, diepte 1 OP) Yea Im super pleased that they used the best leather on the vamp and toe cap. It looks terrific
[coizvw4] (score 1, diepte 2) How do they compare to say 1Ks or other boots in that range? I like the Viberg-look so I'm thinking of either getting these now, waiting for the Canadian dollar to even out more, or get other solid GYW boots.
[coj1wjx] (score 1, diepte 4) Sweet, that's actually a lot better than I thought as I expected these to be inferior to 1Ks etc. I guess I could justify getting these then huh?
[coiwhhe] (score 1, diepte 0) So how did you size for these?
[coiwt0g] (score 1, diepte 1 OP) i sized about 1 size down from brannock. My brannock is exactly in the middle of 9.5us and 10us, and I got a 9us in these. I would ask them for advice on sizing though.
[coixz46] (score 1, diepte 0) So dumb question, but how do you go about contacting them for an order? Their website does not appear to be up.
[coizrjb] (score 1, diepte 1 OP) Email at santalum.indonesia@gmail.com
[coj3qrg] (score 1, diepte 0) How would you rate Santalum compared to Sagara price and quality wise?

I realise you own boots from both.
[cojnaem] (score 1, diepte 3) And, if so, do they offer wide fittings?  If so, I'm ordering a pair.
[cojuswj] (score 1, diepte 4 OP) You'd have to ask as I am not sure
[cpdy1mf] (score 1, diepte 0) Hey I know this is kind of late but would you mind showing some pics of your other Santalum Service boots?
[cpdykzh] (score 1, diepte 1 OP) I have a decent amount of pictures here http://imgur.com/a/trYUe and also here after break in http://imgur.com/a/gqWHC
[cpe23k4] (score 1, diepte 2) Hey! Sorry to revive old threads, but do you have any more pictures of how the black santalums are aging? Thanks!

=== THREAD 1iid1j5 ===
SUBREDDIT: r/goodyearwelt
DATUM: 2025-02-05  SCORE: 16  REACTIES: 51
TITEL: On Feet and Comfort (and getting old)
POST (source_id=post):
Hello GYW. Old head poster here. I used to be incredibly active on this sub about 10 years ago (that feels horrible to write out). Collecting nice shoes has been one of the things I’ve enjoyed most in my adult life. 

There is one thing I’ve loved for even longer: distance running. This, along with my flat arches, has lead to overuse injuries over the years, and one day in 2023, while wearing my Riderboot Dundalks, I felt a stabbing pain in my arch. What followed was 14 months of prolonged discomfort, a billion doctor visits, hobbling around, and general foot problems. 2023 was also the year I attended 9 weddings, and spent 9 long weekends walking around on dress shoes. 

I am slowly getting better (knock on wood), but I’ve come to the conclusion that flat insoles, especially those made of thick, firm leather, along with uncushioned soles are probably not for me anymore. It really sucks. Something heels also seem to set things off—even Blundstones can cause discomfort. 

The issue is that most dress shoe insoles, even those with cork that purportedly molds to your foot, do not have much support and are still never very plush. The bigger problem is that as a lover of nice shoes, orthotic shoes are…incredibly ugly, and barefoot/zero drop shoes are most decidedly not for my foot either. As a result, I don’t have great luck in white sneakers either. 

I’m looking for shoes that have a generally foot-friendly build, but which also have a cogent aesthetic language of their own and don’t look like sneakers. I am so, so tired of wearing running shoes day to day. If the Red Wing 875s had a soft, molded insole rather than a thick veg tan leather insole, they’d probably work well for me.

Does anyone have any thoughts on shoes that share some of the support and cushion elements of running shoes, but 100% do not look like running shoes? Or if anyone has input on how to get shoes to better accommodate orthotics (most dress shoes are too low volume for this), I think it could be a valuable discussion to start!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mb4iwgn] (score 14, diepte 0) Try sizing up and putting your own insoles in. Even sizing up by half will give you enough room in a lot of cases.
[mb4lxpn] (score 8, diepte 0) Just want to say I feel you. I started having pain from wearing my Indys (known for comfort!) which cascaded into my feet being temperamental in general (different than your situation - Morton's neuroma). I typically know within ten seconds of wearing a shoe if they will work for me. But this uncertainty has made buying nice shoes online, used or new, pretty risky. Weirdly I have Alden longwings on Barrie last that are 100% comfortable for me. Double leather sole. But I tried a different pair on Barrie, single leather sole, and they immediately triggered my neuroma. It's a bummer. Good luck out there.
[mb4kknb] (score 5, diepte 1 OP) I have a wide, high volume foot, so this isn't really the case for me, unfortunately, unless that shoe is already really generously sized. There are other risks to foot mechanics associated with sizing up too much (like going up a full size), so it can be tricky!
[mb6qfsy] (score 5, diepte 4) All but one of their lasts are wide, but not just, "whole foot wide", but in the, "I have a naturally shaped foot with narrow heel and wide forefoot," way. They are very much so not traditional. Their narrowest last is a roomy D. 

Their STC last on the African Ranger is a wide toe-boxvand one of the only boots I can wear comfortably. Similar roominess to original fit Altra running shoes or Topos. Most of their boots are EE width as standard. 

That aside, their popularity comes from a few angles, imo. First, They offer solid quality for the price. Good materials, made tough. Second  the owner is a solid fella with a passion for nature conservation. Lastly, their sales of the African Ranger boots go to getting those boots on the feet of actual Rangers in Africa that protect wildlife from poachers, free of charge.
[mb4yfx6] (score 5, diepte 0) Nicks makes a leather insert full or half sole that approximates the support of their 55 last.

I have successfully added it to some of my boots.  If you have any with removable insoles,  that might be even easier to fit.  They run $55 (half insole) to 65 (full insole) or $100 for a bubdle

https://nicksboots.com/deltaarch-full/?srsltid=AfmBOoo3ciL_gqAEpBS07JIUNkL1YBDXys6YX2piaXIVuYFtXtNuA4t8

https://nicksboots.com/deltaarch-half/
[mb4goif] (score 4, diepte 0) >I am so, so tired of wearing running shoes day to day. If the Red Wing 875s had a soft, molded insole rather than a thick veg tan leather insole, they’d probably work well for me

Perhaps the Red Wing 1907 would work? They come with a soft removable insole and still have the leather/cork underneath it. 

Chukka boots with wedge soles are also very soft and comfy - I'm not sure what is easily available in the US.
[mb5oaw5] (score 4, diepte 2 OP) This is both true and not true. Most shoes have a pitch (except zero drop shoes), and most shoes with a heel (most GYW shoes) also have a hinge, where the pitch plus the heel create pressure down the line and onto the sesamoid and metatarsals via the plantar fascia. So for people who have certain foot pathologies, no amount of orthotic support can overcome the pressure of that hinge. I am, sadly, one of those people. There's a way to create a shim under the orthotic that raises the ball of the foot without a metatarsal pad, but that's also controversial. I'm sorry for getting in the weeds here—I've heard doctors and PTs talk at me about this for a year straight lol.
[mb4t7ue] (score 4, diepte 2) On the flip side, I’ve found the TruBalance last to be the most comfortable last for me. I have five pairs on TruBalance and the only marginal comfort difference depends on the sole. I’m wearing these wedge Indys a ton and they’ve been fantastic. Another pair is on crepe and they’re even softer.

Try to find a gently used pair on eBay, so you’re not all-in if they don’t work out.

https://preview.redd.it/7grihvttpche1.jpeg?width=2742&format=pjpg&auto=webp&s=05f34507b0de53122c4f189a2da87df09ef163f0
[mb4try4] (score 3, diepte 0) I can only speak from experience as a fellow foot pain sufferer.  Plantar fascitis that morphed into arch issues and pain when standing.

I pretty much exclusively wear boots - dress shoes just don't work any more and won't comfortably allow my foot to sit in the shoe with an orthotic insert (even though it's very low profile)

Best for me has been lightweight boots that have support but which don't require much break in and the soles aren't too stiff.

Training shoes don't have enough support and aggravate the issue after a while.

Cheaney Trafalgar boots have been amazing for everyday use. 

Alden boots Barrie last. - nice ankle heel support with room for toes 

Both of the above work in terms of weight and sole flexibility.  Boots like viberg and redwing or English boots with thick leather midsole and dainite sole - have aggravated it
[mb4upcc] (score 3, diepte 1) >Cheaney Trafalgar boots have been amazing for everyday use. 

Off topic - but did you ever review / photo these?

I've been lusting over a pair for years ... would love to know if they would work for my weird duck shaped feet.
[mb538tc] (score 3, diepte 0) As a fellow flat foot nice shoe guy I get where you're coming from.  One new (2024) brand I've noticed recently is Arch Support Project.  They're wildly expensive but they're the only high-end leather brand I've seen recently that explicitly focusses on supportive shoes.  They have collabs with [Division Road](https://divisionroadinc.com/products/arch-support-project-workman-chelsea-vibram-asp-gumlite-nero-vachetta-800-calf?variant=45760982515924) and [Standard and Strange](https://standardandstrange.com/collections/arch-support-project) right now.  Certainly not for everyone and certainly not a reasonable price.  However, if you're like me and trying to find just a small rotation of grail shoes/boots that you can wear constantly, it might be worth a look..
[mb5u37j] (score 3, diepte 0) Have you ever tried White's or Nick's? The arche support of the 55 last changed how I look at boots. They both do a lot of custom MTO stuff, and if I remember correctly, I will do orthopedic friendly builds upon request.
[mb68tgj] (score 2, diepte 2) /r/jimgreen is the place for you.
[mb6a028] (score 2, diepte 3 OP) I've actually seen this mentioned before, and am very curious. Do you know what they do differently? The internal structure of their shoes seem very similar to something you might get from danner or Blundstone, which is to say rather traditional. I'm sure I'm missing something because of how popular they are, but any help would be tremendously appreciated.
[nwhzxw0] (score 2, diepte 2) Wish I had better news for ya. But - so far Indys are a no go. Grant Stone diesels - nope. Parkhurst 645 last - no. I have a pair of Viberg hikers that are roomy enough for me to put an insole in (designed to release metatarsal pressure) and those have been working okay (downside is they are 3 lbs each!). I have an old pair of AE Chelsea’s that seem to work when I wear thick socks. My new theory is that because I have low volume feet, my neuroma or whatever it is is triggered when my feet aren’t held securely in place by the upper. Wish I could help ya. I am very comfortable in narrow Birkenstocks and SOME New Balance 998s so I have been wearing more of those.
[mb4uy73] (score 2, diepte 2) I didn't but I've had two pairs for over 5 years so fire away if you have any questions..
[mb5lw3t] (score 2, diepte 4) Definitely not the Trafalgar for you.  If you don't mind a much heavier sturdier boot, their hurricane II C derby is very spacious in the toe area.   It's a chunky boot.
[mb4v23k] (score 2, diepte 1 OP) What is it about the cheaney trafalgar that works? I have some vibram gumlite soled boots (very similar sole material), and those are still a little tough to wear for me. Is the insole different/supportive?
[mb5wgsb] (score 2, diepte 3 OP) This is super helpful, I didn't think about the lack of a midsole playing such a role. Thank you.
[mb4uid7] (score 2, diepte 0) If your main issue is arch support, Nicks are quite expensive but have some of the most intense arch support on the market for their 55 last. You can also get them in extra wide sizes or with a sprung toe for more room and adding a comfort insole.
[mb52jny] (score 2, diepte 0) I know this isn't your ask, but I've switched to Birkenstock Bostons because of foot discomfort due to my "unique" foot. They may not be what you're looking for entirely especially depending on your aesthetic preference but it has been ages since my feet were as pleased with a shoe.
[mb6t8zl] (score 2, diepte 0) I wonder if moccasin style construction might work for you. You may be able to upsize something like a Russell Moccasin with the appropriate outsole that keeps the footbed relatively horizontal, and that way you could fit your orthotics in them?
[mb8e76h] (score 2, diepte 0) Get your favorite shoes resoled with something softer like Vibram 2021
[mb4nfmv] (score 1, diepte 1 OP) I love the idea of a wedge sole, it seems like what my foot would like, but I worry that even with the removable insole, the thick veg tan that RW uses will make the boot stiff and painful. I've been looking for brands that use a wedge but without the leather insole (while also looking nice), but they're rare. if you have any recs, I'm all ears!
[mb7ws33] (score 1, diepte 2) The 875 is a pretty high volume boot. If I buy true to my Brannock size it leaves me enough room to comfortably wear an Aetrex memory foam insole in them. Red Wing used to sell these rebranded as RW insoles. Although the 875 has a leather footbed, it doesn’t cause the boot to be stiff, even with the insole added. The combination of wedge outsole and memory foam insole is incredibly comfortable for all day wear on hard surfaces. My job involves a lot of walking on asphalt and concrete and these are the boots I reach for when I know it’s going to be a long day. 

https://www.aetrex.com/men-s-premium-memory-foam-med-high-arch-orthotics-L2300M.html
[mbdurch] (score 1, diepte 2) I second the wedge idea. I've gone through a similar experience to you, and I've settled on Alden Trubalance shoes/boots and Grant Stone, all on wedge. I use these 3/4 inserts on top of the existing insole and they've been a game changer for me: [https://www.amazon.co.uk/dp/B00VX9QXBW/](https://www.amazon.co.uk/dp/B00VX9QXBW/)
[mbnvlzu] (score 1, diepte 2) I have the redwing 1222's, they're the traction tred lites. Cushioned new work line of 875's. Have a poron insole on top of leather midsole, and I have their insoles in them you can switch out. They are extremely comfortable and look great. I use them for work boots doing carpentry. Ran up and down stairs building a wall at the top the stairs just recently. I love all leather boots but just got a blister breaking in a new pair and really appreciated wearing a pair of boots with cushion afterwards. Check em out

https://preview.redd.it/bnu9xxgiexhe1.jpeg?width=4032&format=pjpg&auto=webp&s=f98de83c247e0c4a4ed8a204733a368233bb6f25
[mbhy656] (score 1, diepte 4) Literally came here to mention Jim Greens as well. I have wide feet and fallen arches. If you need extra width you can upsize and buy some of the Dr. Scholl's heavy duty support insoles and keep them long, rolling the front up into and around the toe to reduce the inside length of the boot.

You can also do this with some of the Danner boots built on their wider lasts.

This is what I currently do and it has drastically reduced my foot pain.
[mb5gdej] (score 1, diepte 1) Yeah, almost any shoe can be an orthotic shoe if you get custom orthotic inserts made and they fit the shoe.
[mb4k4gk] (score 1, diepte 0) Some brands make boots/shoes with foam insoles. What immediately comes to mind is Idrese and Chisos.
[mb4nsmq] (score 1, diepte 1 OP) Thank you. I am, unfortunately, the opposite. Most shoes will feel good when I put them on, but when I get to day 2-3, I'll be in agony and feel like I can't possibly stand a moment longer. I hear Indys are indeed very comfortable, I'm sorry they didn't work out for you. Morton's is tough, I have a good friend who suffers and has been wearing Altras daily for years.
[nwhxz8h] (score 1, diepte 1) Hey man. I have been freaking out cuz of maybe having a neuroma. I feel at a lost because I’m a runner and love gyw boots. If I could at least manage to get Indy’s to work for my feet I’d be extremely happy. I know my dream of owning and wearing out a pair of Engineer boots is pretty much over. Which boots have worked for you?
[nwi322p] (score 1, diepte 3) That’s such a bummer. I had gotten a pair of Eastman tanker boots last year after saving up for them for 2 years. They fit well until recently where I feel pressure around the midfoot and pinky toe on the foot with the neuroma. The only wide toe boots I find not ugly are the Indy boots. All my vintage converses up for sale too. I’m at such a loss. Oddly I also have a pair of Chelsea boots that work for me. Maybe that’ll be what i look for. Thanks for the response.
[nwi5i5p] (score 1, diepte 4) Sorry man. I am considering seeing a podiatrist to at least get assessed. Might be worthwhile.
[mb4ql1p] (score 1, diepte 0) Maybe try RM Williams? They have various "comfort" options. Some Mephisto models may also work for you.
[mb4rh4l] (score 1, diepte 1 OP) It's funny you should say that, I've been wearing RM Williams since \~2013. My original pair has been everywhere with me, and I got married in a new pair last year. While their poron insoles are indeed very comfortable compared to leather, my feet no longer like them for daily life. They have genuinely no internal support structure, and their dynamic flex version hasn't been particularly good to me either.
[mb4qo3v] (score 1, diepte 0) Check out Samuel Hubbard, they are a little non -traditional but the most comfortable shoes I own.  Also pick some insoles that work for you and head to a Red Wing store and see if any of the boots work sized up to fit the insoles. Red Wing does have their own insoles too.
[mb4zxm3] (score 1, diepte 2) If you have wide toes the Trafalgar is a bit almond shaped. Check out the similar lightweight boots from trickers for more width.  C&J also do one
[mb54ly9] (score 1, diepte 3) Ah I struggle with toe width with Trickers ... so I guess Cheaneys is impossible.

Curse of narrow heels and very wide toes.
[mb4ziob] (score 1, diepte 2) Tough meaning, they don't flex enough which forces your foot to flex in the stiff boot and cause pain? 

With the Cheaney I think it's because there's no midsole.  So the foot is supported but it's very light and flexible.  

C&J and trickers have also brought out similar very light weight boots with no midsole.  Worth checking out.
[mb9l1ml] (score 1, diepte 4) If you want a more dressy look, officine creative also make lightweight welted boots
[mb55fh0] (score 1, diepte 1) /u/nice_nice50 Any recommendations for an orthotic maker?
[mb5ngoe] (score 1, diepte 2) Depends where you're based but having tried a tonne over the counter I don't rate them.  I've had them made by someone using plaster of Paris - also no good because you don't fit them when your weight is on them

Best one is custom heat moulded from 'Sidas'.   You need to find a supplier that fits and then makes them professionally.  Not cheap but worth it
[mb4y0id] (score 1, diepte 0) I use an orthotic half-insert that was made for dress shoes and I guess dressier boots. It goes from the heel to just before the ball of the foot, so it doesn’t increase the height of your foot in the toe box. Works pretty good, although when trying it with AE shoes the salesman suggested going up in width since obviously you are increasing the volume of how your foot sits at the back and instep.
[mb5317f] (score 1, diepte 1 OP) I used to wear birks as a teenager and loved them. Tried them again recently and they absolutely killed my foot. Even the soft footbed was too hard and too high-arched. tragedy because I low-key love the shape of the Bostons and Tokios. But I appreciate the rec because that's pretty much what I mean when I said I wanted shoes that have their own cogent aesthetic language—they are their own thing and are not trying to camouflage themselves as something else.
[mb5poq9] (score 1, diepte 1 OP) This is actually super interesting, thank you for sharing. I love the idea of blending modern notions of foot mechanics and old school construction.
[mb9oz9i] (score 1, diepte 1) What they are doing is also possible without this look. The last has to be hollowed out more in the arch are of course like they are doing, but the support in the arch area can be built in between the inner and outer leather.
[mb5y6rt] (score 1, diepte 1) This was going to be my suggestion.
[mb6wpfb] (score 1, diepte 0) Might want to check out bespoke orthopedic footwear. Something like the [premier collection](https://www.craryshoes.com/gallerycustomcollections) here might be an option.

It’s probably not the cushioning you need just a better fit and support where you need it(rather than where you don’t). There is a lot more shaping under foot in bespoke footwear compared to ready-to-wear.
(14 reacties met lagere score weggelaten)

