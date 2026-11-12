# Label-batch batch_0025

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
Schrijf het resultaat naar `batch_0025.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(5 threads: 48h3rj, 3hwh6b, gco1dg, gzapb0, w4wl1v).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 48h3rj ===
SUBREDDIT: r/goodyearwelt
DATUM: 2016-03-01  SCORE: 71  REACTIES: 33
TITEL: I attended a Shoemaking class last June in Ashland, OR. Here is the recap.
POST (source_id=post):
I was fortunate enough to attend a shoemaking class last year.

It's something that I've ALWAYS wanted to do, I originally went to school because I wanted to design sneakers, and then went onto leatherwork because I was experimenting with shoemaking in leather.  I never went to a class before as there are only a few in North America, most are far away (and honestly, pretty shitty looking). 

So when I heard that there was a class hosted by[ Marcell Mrsan](http://www.shoemakingcourse.com/) at Bonney and Wills studio, just before the first annual Shoemaking Symposium in Ashland, OR. I'm based in Vancouver, BC, so Ashland, Oregon was only around 11hrs of driving away!  I also took it as a little vacation, so I took off ~2weeks of work, rented a car and took off.

The course was 8 days. 8-5pm with an hour for lunch. We usually stayed a bit later, and sometimes took parts home to work on. Cost was $1800 USD. At the time that translated to about $2200 Canadian. You left with one pair of shoes... but more importantly a stupid amount of hands-on knowledge.

There were 8 students in the class, ranging in Ages and backgrounds. Only myself, and one other student hadn't ever made a pair of shoes before. It was very much a master-class, and everyday was very work-filled and intense.  I was lucky that I had been pretty involved in leatherworking for the past 4 years, so hand-tools weren't too crazy for me, and I had done a ton of research over the years learning how shoes are made just out of my own curiosity. 


-

Here is a pictoral journal: http://imgur.com/a/8x3v4

As well as my instagram day-by-day:
 

[DAY 1:](https://www.instagram.com/p/3xWzYQi40P/?taken-by=handandsew) First day of shoemaking class! Learning how shoes are patterned, different styles, options and so much more. An absolute overload of information, but super excited to make my first pair, and start designing/making more!

[DAY 2:](https://www.instagram.com/p/30DyCnC45g/?taken-by=handandsew) Day 2 shoemaking class: skiving counters.. . So much skiving.here is my teacher @marcellmrsan showing how effortless it is, why is mine full of holes?!

[DAY 3:](https://www.instagram.com/p/32s9iDC497/?taken-by=handandsew) Shoemaking day 3: working on the insoles! A lot of really complicated cuts with your knife and the lifesaving ( and life taking if you're not careful) channel knife. Tomorrow is lasting uppers!!
[
DAY 4:](https://www.instagram.com/p/35AT8Xi4wd/?taken-by=handandsew) Day 4: Lasting! This was a very fun day, lots of hands-on intense shoe work. I managed to last both uppers and finish the toe puff on one. Tomorrow finish toepuff and move on to welting!

[DAY 5:](https://www.instagram.com/p/37pkLKi40v/?taken-by=handandsew)Day 5: welting. This is the thing that sets this class apart from other places. Hand welting is not fun, your stitching across a solid 1" of 5 different leathers, it can get really messy trying to thread needles through everything. But this is the most secure attachment and can only be performed by hand

[DAY 6:](https://www.instagram.com/p/3-OvNHC4zu/?taken-by=handandsew)Day 6: finish in seaming both shoes, as well as knotting the heels and outsole prep for tomorrow. I was particularly proud of my nail placement and bending in this photo! It's harder than it looks to stretch everything and line it all up.

[DAY 7:](https://www.instagram.com/p/4AwBhcC4wE/?taken-by=handandsew)Day 7: shoemaking class. Put the soles on the shoes! Lots of hammering and careful cutting of the thick leather with a lip knife. Then stitching through the welt into a handcut channel in the sole. Tomorrow is finishing.
[
DAY 8](https://www.instagram.com/p/4FR8kti41-/?taken-by=handandsew)Day 8: finishing. Last day of class was a hurry of details; sanding glassing, and protecting the welting and sole. Like all finishing in leatherwork this could easily bleed into a few days worth of work. I'm so incredibly happy with these being my first pair of shoes I've ever made. There is a lot of improvements to be had, and I'm excited to keep pushing those limits. I think I've caught the shoemaking bug.

[
CLASS PHOTO:](https://www.instagram.com/p/4FTO6aC44j/?taken-by=handandsew)And a special thanks to @marcellmrsan and @bonneyandwills for hosting this amazing class. It was humbling to talk with people who were willing to give so much knowledge and share their craft with beginners like me. I highly recommend to anyone interested check out their respective sites for future classes. It was an incredibly inspiring experience.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d0jjc9q] (score 6, diepte 0) This looks like a great experience! I often times dream about taking part of something similar myself, but unfortunately there are some health concerns that prohibit me from involving myself in a course that intensive right now.

I also hand welted my first pair of shoes, and I sort of regret going that route. It was very overwhelming, and I've stuck to stitchdown construction ever since then. I'm sure it would be much easier now that I have more experience with awls and needles and hand sewing in general, but it was a terrible idea to hand welt my first pair completely without any guidance. Didn't help that my uppers were made of 6 oz. veg tan that was rolled stiff, haha.

It's funny that Paige Sorrell took the class. Suspect she mostly wanted to meet Marcell!
[d0josm7] (score 6, diepte 1) Yeah, I was very surprised to see almost 1/2 of the class being women as there are so very few GYW options out there for women.
[d0jhu0z] (score 5, diepte 0) Thanks for cross-posting this!

Very interesting class. I found it interesting they gave you the uppers all sewn together but I suppose that saves a lot of time and allows you to focus strictly on the construction.

In the end, do you think it was worth it? How are the shoes holding up? Do you have any updated photos of how they're aging? Do you plan on making any of your own shoes in the near future?

$1,800 seems really reasonable for that type of intensive class.
[d0jiy48] (score 5, diepte 1) > I found it interesting they gave you the uppers all sewn together but I suppose that saves a lot of time and allows you to focus strictly on the construction.

This baffled me a little bit too before I thought about it, since a huge part of shoemaking is pattern making (which seems to have been covered), clicking and closing. Closing is above all a very delicate process and if you make a mistake the whole shoe is going to look awful, so I can see why the participants were given a finished upper to start out with. The class seems to be more focused on learning the basics of hand welting and the use of hand tools in general, which is great. Machinery can be a bit overwhelming for a beginner.
[d0jozl0] (score 5, diepte 1 OP) No problem!
Yeah, some people comment on that. Honestly having been taken through the whole process, the actual cutting and sewing of the upper is fairly trivial. You don't "learn" as much as just need to practice until you get good... And the class is focused on the hand welting technique. Time was limited.

Definitely worth it. Knowledge and time with marcell as well as everyone else in the class (and bill shanor!)  Was so great. Good connections too. More than anything for my line of work, its great to have on the resume.

The shoes are unfortunately a bit too tight for regular wear. People always comment on this in shock. Honestly I didn't take the class to have a pair of wearable shoes. And if you go in just looking for that you're going to be disappointed. Because after learning properly, you'll look at the first pair in disgust haha.  I really want to make another pair, when time permits!

For the price it was a great experience.
[d0jnc18] (score 5, diepte 0) Awesome you were in the class with Paige Sorrell; I follow her mother on Facebook and just absolutely drool over the boots she makes.  Cool to see her daughter getting into a different angle of the business.
[d0jp48a] (score 5, diepte 0) Very cool experience. Thanks for sharing.
[d0jq45r] (score 4, diepte 0) I've always been curious - when lasting the upper and hammering the nails into the last, doesn't that wear down the last pretty quickly? Having all of those nails being driven in and pulled out repeatedly. How long does a last..last?
[d0jga6v] (score 2, diepte 0) Marcell is one of my favorite people.

He seems like a great teacher if you are serious.

Is he as curmudgeonly in person as he seems to be online? I usually attribute his Curt nature to his Hungarian nature.

I'd love to take one of his or James Ducker's workshops sometimes, but family and financials make it less than feasible.

Will has always seemed like a really great and friendly guy as well. I'd have loved to attend the symposium but I couldn't. I'm actually considering the next one and getting /u/stevenkmason to ~~pay for me~~ go with me.
[d0k96rn] (score 2, diepte 1) As someone who wants to make my own shoes/boots sometime in the future, could I ask you some questions? What's the difference between stitchdown and welting? Why is stitchdown easier? And what type of equiptment do you use? I saw your work and I think thwy're really beautiful.
[d0kjplf] (score 2, diepte 2) With stitchdown you skip the whole part where you channel the insole to create the holdfast to which the welt is sewn. Instead you glue a midsole directly to the insole and turn the uppers out and stitch them directly to that, either just the front half of the uppers (like Viberg/Truman) or the whole thing (like Clark's desert boots). It's also more forgiving to last a stitchdown shoe, since you don't need to really tightly last the toe portion of the shoe since it will be turned out anyway. With hand welting you need to do a really good job lasting the toe, or you will get puckering.
[d0k3wpz] (score 2, diepte 0) um...how big are the toads...  



(very awesome thread and pix btw - your shoes came out great!)
[d0kj0rs] (score 2, diepte 0) I think giving students completed uppers is the way to go. Regardless of how well students shoes turn out your average person can figure out the upper is just leather sewn together. What they wouldn't know is the gyw process and how to do that part.  
  
I also did a shoemaking course and I don't think it was anywhere near as good. I didn't do it to become a beginner shoemaker, I did it because I was curious about the process.  
We spent most of the course just skiving, gluing, and sewing the upper together. We finished with some lasting and glued on a pre-made sole.
[d0kl0fu] (score 2, diepte 0) Good job! I spent six weeks after the symposium at Bonney &amp; Wills with Bill - such an amazing teacher. Lisa Sorrell ran a 3 day leather inlay&amp;overlay course at B&amp;W after the symposium, which was fantastic too! Definitely worth going to this year if anyone is wondering about it.
[d0ke8zf] (score 1, diepte 1 OP) I would certainly say he is great if you are serious. He is very very oldschool, and will take no-excuses.  One student was essentially left behind in my class when he started to struggle in the 3rd day. We helped him rush to catch up at the end... but it definitely was a bit rough to watch. Marcell is very traditional.  He was actually a perfect opposite to Bill Shanor, who felt like the kindest,gentlest teacher haha. It was great as always to have a balance. Both were needed at different points.
[d0kmefy] (score 1, diepte 2) That sounds a bit like what I expected for Marcell and Bill.
[d0ke558] (score 1, diepte 2 OP) The class focused more on the hand-welting technique. As I said, only 2 of the 8 students hadn't made shoes... it definitely wasn't a beginner class! 

It's tricky with machines, you need a lot of time to get used to a new machine, even if you've sewn thousands of uppers before. And although sewing the upper seams is part of shoemaking... I would say it's the least "skilled" part. You just need to put the hours in on the machine. Which we didn't have time for in the class.
[d0ke1v6] (score 1, diepte 1 OP) It was a fantastic experience! Hand-welting is definitely a bit crazy. I could imagine it being even crazier if you don't have all the little tips and tricks that make your life a little easier.

Yeah, it was honestly a bit surreal seeing her there (I wasn't expecting her!), as I had been watching her mum on Youtube for the past like 3 years.  She was really nice to talk to, very kind. She has had lots of experience with Marcell actually, as she spent some time taking classes at SCAD, where he teaches.
[d0ke6f6] (score 1, diepte 2 OP) Funny enough, half the class was canadians too!
One woman was a shoe designer based in LA, and the other was a rancher in Alberta interested in cowboy boots.
[d0jwtc0] (score 1, diepte 1) I just bought a skiving knife from Lisa and have really admired the work of hers I've seen.
[d0jwwmx] (score 1, diepte 2) Yeah, her work is incredible. I'm always sharing and reposting her content on facebook.  Someday I'd love to have her make me a custom pair of boots.
[d0jvbsa] (score 1, diepte 1) Depends on the material and construction of the last. Some lasts have metal plating on the bottom, either full plating, 3/4 or just the heel. On those it's obviously not an issue since the nails just chinch against the metal plate (which is helpful in finishing the shoe as well, since you don't need to drive the nails back down when you take the lasts out). Plastics lasts tend to last longer than wood with their higher density since the perforations made by the nails don't structurally damage the material in the same way.

I can't tell you how long it takes for a pair of lasts to go out of commission, but they last a while. You'd be surprised by how many times you put nails into the exact some holes as well, which would be extra true in a factory production setting.
[d0jwrnd] (score 1, diepte 0) Thanks for posting this. I first heard about classes there a couple years ago in [this article](https://www.1859oregonmagazine.com/shoemakers-row-oregon-custom-shoemakers). Once I'm done with school and move down fairly close to Ashland, I'd like to take one of their classes.
[d0kgh6b] (score 1, diepte 0) I've dreamed of doing a class exactly like this, but the only thing that makes me hesitate, is not knowing whether the shoes are bespoke lasted? Or are you using a size that fits your foot well and making modifications from there?
[d0khct1] (score 1, diepte 2) I can agree with most of the point you make (some of it makes a lot of sense). But if I had the choice of paying $1800 for a pair of shoes that were made to fit my feet versus a generic foot shape, I'd choose the one made to match my own. With the greater purpose of hopefully leaving with a last of my own individual feet to work from in the future.
[d0khnre] (score 1, diepte 3 OP) Last making and modification is an entire artform in itself.

Making a pair of bespoke shoes isn't as easy as taking measurements and bam, shoe.  You need to make changes to your last, create an entire pair of test shoes, and then test fit, make changes to your last, then create a final pair of shoes.  That's not something you can "learn" from a class.
[d0khv5c] (score 1, diepte 4) I wrote up a reply, but I like yours a lot more, so I deleted mine. I'd also add that they had the uppers pre-made for you and you can really only do that if you know what last you will be using, otherwise everything is just off. That and $1,800 for a pair of bespoke shoes is pretty cheap compared to the top guys that we generally throw about. 

I'd love to actually see someone create a bespoke last. I wonder if it's like what Michelangelo said about how every block of stone already has a statue inside and you just have to clip away the excess
[d0khx4b] (score 1, diepte 5 OP) Thanks. I couldn't agree more.

You should look into orthotics. Every shoe made with custom orthotics usually has a custom last created exactly to the clients foot needs. Very cool, and lots of interesting mixes of oldschool technique with new technology.
[d0ki0ov] (score 1, diepte 6) Yeah, there's actually a guy in Seattle who specializes in creating shoes for people with deformities, injuries, and the like. He's been doing it for decades and I can't believe he makes any money as his shoes start at only $500 for the shoe and $600 for the last. If I were ever serious about learning, I'd see if I couldn't apprentice/shadow with him for a bit. [Link](http://mobetashoes.com/the_process.htm)

He actually mentioned in an interview that he has taken on quite a few apprentices, but they all leave when they realize how much work it requires and how little it pays :(
[d0khyle] (score 1, diepte 5 OP) here is a custom last created by a local shoemaking friend of mine! https://www.instagram.com/p/BApsC-Hlviv/?taken-by=westerly_shoes

You should check out the rest of her stuff if that interests you.
[d0ki5ma] (score 1, diepte 6) Very cool, thanks for sharing. [Here is a video](https://www.youtube.com/watch?v=rxe4lIJIRyc) of the guy I was talking about. I mean the tracing of the foot he was making the last for is so wild! Like I couldn't even imagine feet like that, but there is he making a last for it. I just wish I could see more of the video process for coming up with something so different.

Edit: Found one. [This is really cool](https://www.youtube.com/watch?v=AUfRgA1VsGY&list=PLqvk0j-025nVDcnibt2lyzu1jOfA-RojA)
[d0kr93x] (score 1, diepte 0) Very cool! I'm from Southern Oregon originally so I spent a lot of time in Ashland while growing up. I had no idea this studio was there - I'll have to check it out next time I am back for a visit.

Thanks for sharing the process with us. Your shoes look great! Do you feel more strongly towards them since you made them yourself versus other pairs you might own?
[d0kgxj4] (score 0, diepte 1 OP) > The shoes are unfortunately a bit too tight for regular wear. People always comment on this in shock. Honestly I didn't take the class to have a pair of perfectly bespoke shoes. And if you go in just looking for that you're going to be disappointed. Because after learning properly, you'll look at the first pair in disgust haha. I really want to make another pair, when time permits!

I wrote earlier in the thread. I teach leatherworking for bags and accessories, and people always go crazy just looking at the end products I make and wanting to do that themselves.... its just not feasible.

Imagine going into a woodshop for the first time and asking to make a 6 piece dining set.... everyone would just laugh at you.

If you want bespoke shoes... hire someone to make them for you.

=== THREAD 3hwh6b ===
SUBREDDIT: r/BarefootRunning
DATUM: 2015-08-21  SCORE: 2  REACTIES: 32
TITEL: Feet swollen and tender after hike
POST (source_id=post):
Hey,

I am an above average fit person, and have gone barefoot (by and large) during the last five years or so.

Yesterday I went on a hike with my sister, we went ~20 km then and another ~22 km today. 

Now, my feet are a mess. I have pains under the skin of both my heels, and under the skin of my front sole (where the second and third toes connect to the foot).

I was walking in VFF Lontra, my sister was walking in Nike Free 4.0. She had no issues.

It soured my mood quite a bit and ruined most of the experience. Why did it happen? What can I do to prevent it from happening?

My own suspicions:

Moisture

Shoes too large

VFF's are bad for hiking

I haven't hiked enough

My skin is a monument to bad genetics

Help :(

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cub69gs] (score 7, diepte 0) Do you usually run 20 km one day and 22 km the next?

 My guess is literally just that you over exerted what your feet can do, especially without support hiking over rocks and whatnot. Like running barefoot, hiking barefoot takes a break-in period.
[cubq7rf] (score 2, diepte 0) The first time I went for an actual hike on an actual trail in Vibrams I was surprised at how much it hurt the bottom of my feet. Then I switched to running completely unshod and reached a new level of de-sensitivity for my feet. Went on another hike. It still hurt. A year later, went on a hike barefoot. Was sore, but less painful. Turns out nature is pointy. Even the frees have 3x to 4x as much material between the bottom of your feet and the ground compared to VFFs. 

It's probably fair to say that for what you were trying to do and your current level of sensitivity your VFFs were not the right shoe. Maybe for half that distance, tough to say.
[cubpm68] (score 1, diepte 1 OP) I do not hike or run such distances often but my sister does not do these distances either, and she was totally fine (her soles at least).

:/
[cubrrkt] (score 1, diepte 2) Yeah, but the amount of material between her feet in Nike Frees and sharp rocks, roots, etc, is a significant difference than VFFs. 

Stay off your feet for a day or two and they'll be fine. Pick up a pair of minimal trail runners to hike in. I found some Merrell Mix Masters in an outlet for me for $30 to hike in. Not completely minimalist, but for hiking they have good cushioning. I've done 15 miles back to back days with no problems.
[cubtm0p] (score 1, diepte 3 OP) Is it about the thickness of the shoe soles, for sure? Couldn't it be that VFF's are terrible at wicking moisture, which leads to spongy and vulnerable skin?

My experience with minimalist shoes other than VFF's is that their toe boxes are too small, which I really dislike :/
[cud930k] (score 1, diepte 4) I've found that problems can be related to a variety of problems, ranging from the shoes, the insoles, socks, my skin, my form, my bunions, etc.
[cubcblx] (score 1, diepte 0) Blisters, or not? Those are fairly long distances, especially doing another long hike the day after.

Have you tried toe socks?
[cubplmu] (score 1, diepte 1 OP) I used toe socks inside my VFF Lontra.

No visible blisters at the skin surface, though I suspect there are blisters 'deep down' somewhere.
[cucs0g0] (score 1, diepte 2) After reading more comments here, it does sound like your soles just had a lot of friction on the bottoms, but not enough to cause visible blistering. 

I think this improves over time with thickening of sole skin when you continue to hike minimal. 

If it doesn't improve, I would try other shoes or sandals and check my form to make sure I'm not adding friction to my step with a pushing or twisting.
[cucwkwc] (score 1, diepte 3 OP) Hmkay, I'll try sandals next time I think. Should keep the feet dry I hope...
[cubsj5x] (score 1, diepte 1) This. I hike in minimalist (nb mt10v2) shoes for 3 years now (hiking only during the summer). The first year I could do valleys. The next I could do moderately long hikes. This year I can do longer hikes but by the end my feet are quite tired and starting to get sore. It takes time.
[cubti68] (score 1, diepte 2 OP) Sore in what way though? For me it wasn't about muscles or ligaments, just skin.
[cud8zrf] (score 1, diepte 3) I wonder if everyone is walking on different surfaces?  Might account for different experiences?

Being unshod, I've found that my skin has adapted over the years.  I used to avoid getting my feet wet, but now I can run in the rain, without any problems. So yes, even skin can take time to develop.

As for deeper tissues, I also spent time training so that I could run on a half mile segment of drainage rock on a local trail. The first time I went on it years ago, I had to walk in the brush alongside the trail. After several months, it was still challenging, but doable.
[cud9rq4] (score 1, diepte 4 OP) And you didn't tense up while running on the drainage rock?
[cudaudy] (score 1, diepte 5) I probably tensed up somewhere, as the first 3 miles of the trail were fairly normal, and only broke out into a heavy sweat when on the rocks. :) Great workout, but too long of a drive for me to get to the trail regularly.
[cubtniy] (score 1, diepte 1 OP) Assuming that my issue did not stem from nature being pointy, what could it be?

What if I stepped in a puddle during day 1 and kept walking though my feet were soaked?
[cucbgq8] (score 1, diepte 2) Not likely... Feet in wet tend to smell, chafe, or blister but that's not what you described.It really is most likely fitness and the extent to which you used muscles you don't normally use. Are you feeling better now? How long did it it to recover?
[cucoewp] (score 1, diepte 3 OP) I must have explained it badly, sorry!

What I had was basically like blisters but at a deeper level, so they were not visible from the skin surface. It felt like walking on blisters though. No appreciable muscle pains.

My feet are much better already after two days and nights of sleep and inactivity. My heels appear completely recovered, while a bit remains to recover on the front sole.
[cud8mtu] (score 1, diepte 4) I've had that blistering feeling in the past, too. When it happens under thick skin, sometimes it's not apparent until several weeks later, when my skin starts peeling. That's after my skin grows from the inside, finally pushing the blister to the surface.
[cud9s89] (score 1, diepte 5 OP) Good to know I'm not crazy!
[cubqg0e] (score 1, diepte 0) Trails in Merrill trail runners or NB minimus haven't jacked me up.   I switched over to non-toe shoes after bruising my instep on a rock while wearing VFFs.
[cubtgyy] (score 1, diepte 1 OP) Mmm I'm also beginning to suspect that individual toe pockets do not in fact help much, perhaps the opposite. I'm not sure though.

Either way, I find minimalist shoes other than VFF to have too small toe boxes, even though they're supposed to be large and roomy. Perhaps my feet are abnormally wide at the toes?
[cud8d8e] (score 1, diepte 2) I've found VFFs to provide great grip for quick changes in direction, like sharp corners.  Otherwise, no real advantage for me.

Rather than your feet being abnormally wide, perhaps most mass market shoes are too narrow? It's interesting how the toebox of shoes become narrower from childhood to adulthood.

https://www.thebarefootrunners.org/threads/the-shape-of-popular-athletic-shoes-from-childhood-to-adult.17589/
[cud9uov] (score 1, diepte 3 OP) :[

I suppose it will be a few years until shoe manufacturers understand what we need/want/should have.
[cudaq1a] (score 1, diepte 4) Most modern shoes are made for fashion, not necessarily function. They're making what the market demands. :(

http://www.thebarefootrunners.org/threads/articles-about-hallux-valgus.17677/
[cudqp1p] (score 1, diepte 5 OP) :(
[cudrlka] (score 1, diepte 5 OP) I wish there was a legit way to correct the great toe misalignment without compromising the function of the foot.
[cuekq31] (score 1, diepte 6) Dr. Mark uses CorrectToes. https://nwfootankle.com/files/TestimonialCorrectToes.pdf

I've had some success engaging the big toes. http://www.thebarefootrunners.org/threads/engaging-the-big-toes.17853/
[cuewnqb] (score 1, diepte 7 OP) Interesting!

I suppose CorrectToes might be a very good investment despite its steep cost. Hmm. What do you think? My feet: 

http://imgur.com/SVcrmZo,B3JeS6h#0 (relaxed)

http://imgur.com/SVcrmZo,B3JeS6h#1 (splayed)
[cuex8d4] (score 1, diepte 8) I don't know. Your big toes look fairly straight already.
[cuexljv] (score 1, diepte 9 OP) I would like my feet to look like these:

http://freegrowthblog.com/wordpress/wp-content/uploads/2010/03/native-barefooter-feet.jpg

Do you think that, in the future, there will be surgeries available that correct the misalignment without inhibiting function?
[cuf9lgx] (score 1, diepte 10) I'm no expert, but my understanding is that surgery should be the last option.
http://www.apma.org/Learn/FootHealth.cfm?ItemNumber=979
[cufht83] (score 1, diepte 11 OP) There is nothing about surgery consequences in that link that I can see??
[cuflxdz] (score 1, diepte 12) "When early treatments fail..."
[cug3ffz] (score 1, diepte 13 OP) Yes but I was having mind things like "Surgery typically leads to reduced mobility bla bla bla".
[cuflymp] (score 1, diepte 10) No surgery will make your feet look like that.  That's from a lifetime of being unshod.
[cug3h01] (score 1, diepte 11 OP) :(

I have naive faith in future medicine. I want undone what my parents did not know they were doing to me. !

=== THREAD gco1dg ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2020-05-03  SCORE: 4  REACTIES: 31
TITEL: I need neutral running shoes, can you help please 😌
POST (source_id=post):
After running for a year in stability shoes NB 860v7..3-5 miles 3 x week, somehow I am now a neutral runner!

My current shoes feel like I’m running on logs, my legs ache but push myself through, maybe a lower drop or maybe just having a neutral shoe will make all the difference?

  
I’ve done quite a bit of research but going round in circles, 

The few shoes I seem to be drawn to are

**NB FuelCell Rebel/1080v10**

**Brooks Ricochet 2/Hyperion/Ghost 12**

**Nike Zoom Pegasus Turbo V2**

**Hoka‘s but I’m a bit wary of squashy soles...**

**Asics Gel Nimbus 22**

I need something that I can wear a lot and won’t fall apart quickly.

I would like a responsive sole but with a bit more cushioning (preferably lighter than I’m used to than I’m used to 272g) that I can also use to train for longer distances 

I also like my feet to feel locked down when I run

Price doesn’t really matter as long as I can avoid buying more pairs....  


Any help would be great, thanks 😊

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[fpci94y] (score 8, diepte 0) The Nimbus is a decent choice if you want a cushioned shoe that isn't to squishy and they will last as ASISCS is renewed for making shoes that will last 500+ miles.

The 880v10 has recently had a major revamp and in some circles is considered a better shoe than the 1080 - so could be an option. I wouldn't say that either the 1080 or 880 is "squishy" due to the more traditional EVA midsole material vs the new "super" foams that you will find in things like the Fuelcell Rebel/Pegasus Turbo and Hyperion Tempo.

Depending on your size - both the Nimbus and 880 can weight abit more than the 860 you have been using(closer to 310grams) - this obvious lessen if you're in a smaller women's size shoe.

Also for the "everyday trainer" you might want to add the normal Pegasus 36(or 37) or Reebok Floatride Run or the Floatride Energy.

So many choices, so little time.
[fpck7pi] (score 7, diepte 2) I wear a fair few New Balance shoes (Beacon v1, Zante v3, v4, and Zante Pursuit, 1080v9/1080v10) and they are as good a quality as you would expect from a leading sports shoe company.

Im not a big nike fan, people seem to rave about them, I only have the original Zoom Fly. I did have the pegasus 35 once, but realised that I had been sent a women's size 9 rather than a mens - they hurt ALOT!

I know reebok are coming back out with shoes that look abit more "retro", not to everyones taste - the worse they look the more I like them!! Some Reeboks can be abit narrow, similar to Adidas.

My recent foray into Asiscs has been with the Novablast - very soft shoe to walk in, but once running, it certainly perks up. It a tiny tiny tiny bit narrow around the middle of my foot but loads of room for my toes. My favourite shoe at the minute - until next week when I buy another pair or something else.

Shame its hard to get anywhere to try things out as I personally think the 880 is the way to go for a "do it all" kind of shoe.

Until you realise you need an Recovery day shoe, an everyday training, a tempo shoe, a speed shoe, a racing flat, a trail shoe, a 5k shoe, a carbon plate shoe and a marathon shoe :D
[fpchcwy] (score 5, diepte 0) If you liked your 860, why not go for the equivalent neutral shoe, the 880?
[fpd00q1] (score 5, diepte 0) Surprised adidas Boston hasn’t been mentioned yet.
[fpch6cc] (score 4, diepte 0) If you don't want squishy avoid Turbo 2, 1080 etc.

Brooks Ghost is a sensible milage shoe.
[fpd0un6] (score 3, diepte 3) Your last sentence killed me! I'm definitely heading in that direction.
[fpdb64k] (score 3, diepte 1 OP) I very nearly bought the Rincon, all the reviews pointed to it being exactly what I want but heard that it may not last and is a bit slippy in the wet. Part of my run is sometimes through the woods...any advice on these issues?
[fpcifwi] (score 2, diepte 1 OP) That’s really helpful, the Brooks does look like a workhorse!

 Tbh I don’t know if I would like squishy or not as I’ve only ever run in my NBs which are super firm...
[fpcj76t] (score 2, diepte 2) Ricochet 2 is quite a nice lightweight responsive shoe if you want something a bit firmer.
[fpcigtz] (score 2, diepte 1 OP) Definitely a consideration, thanks!
[fpcl9nm] (score 2, diepte 3 OP) Yes, the quality of my NBs is good, the sole is hardly worn and I know they and Asics make great shoes!  
I run for freedom and fitness, I don’t care about times or 7 different shoes...just want a bit more comfort and a spring in my stride. 

It is a pain not being able to go to an actual shop, although would be happy to social distance forever!!

No, I’m not keen on Nike tbh either. Before the lockdown I did go to a Nike store, they guy got me a flimsy looking mans shoe, didn’t ask my gait or preference and was on the hard sell..I made my excuses and left.

I’ll have another look at the Reeboks, looks aren’t everything... and seriously consider 880/ Nimbus, although I’ve just had a look at the Novablast and they looks amazing and a bit different, narrow midfoot is ok as long as I have room for my toes to spread, my other asics don’t allow that!
[fpcupj5] (score 2, diepte 6) Welcome to Running shoe geeks!! haha!
[fpcznj5] (score 2, diepte 8) Or just do what I do..... buy 20 pairs (I may have a problem or two) https://i.imgur.com/UG6sYSG.jpg https://i.imgur.com/aMsjTqp.jpg https://i.imgur.com/bZEHqsy.jpg https://i.imgur.com/PeDuZuy.jpg https://i.imgur.com/s8KlZwp.jpg
[fpdavcy] (score 2, diepte 1 OP) Good point....tbh not even checked out MIzuno shoes BUT my flat arch is no longer flat, I actually believe that running and daily yoga has righted my gait
[fpd1fah] (score 2, diepte 0) I just got the Hoka Rincon’s and I’ve been loving them. I only have 15 miles on them but they’ve been awesome, and they’re not squishy. They kinda feel like a kinvara that’s been stacked up a few mm.
[fphe5ql] (score 2, diepte 1 OP) Just bought some!! 😃
[fpcjp4o] (score 1, diepte 3 OP) I think that’s a good consideration for me, thanks! Maybe get something more cushioned when I’m actually running further!  
Brooks let you try them out too I believe...
[fpcj6jz] (score 1, diepte 1 OP) Haha, yes too much of a choice...my head hurts!!

Thats some excellent advice, thanks...I’m 6 foot, 67kg and take a 8.5W, so maybe weight isn’t that important after all.

I trust that NB are be good quality, and am expecting that technology has moved on somewhat so may be the one,

I did see that the Pegasus appeared popular but not sure about lockdown or durability of it (I have no experience of Nike shoes)

I have an asics trail shoe, it’s a little narrow but made equally well.

Reebok, I did look but wasn’t keen on the shape, I actually think Nike shoes are ugly too, I’m fussy, I’m a woman....
[fpcmhqa] (score 1, diepte 3 OP) Out of curiosity which is your favourite NB shoe?
[fpcmneq] (score 1, diepte 4) New Balance Beacon, one of my few shoes to go over 200 miles - light weight, with plenty of cushion. I would of thought the Fuel Cell Propel which is very soft but its alittle shoe and just to soft!(Forgot about that one).
[fpcumbj] (score 1, diepte 5 OP) I’ll check them out too, cheers!

 I looked further into the nimbus...they say they are for heel strikers, my head is spinning
[fpcyw6u] (score 1, diepte 7 OP) 😂 yep!! At this rate I’ll be lugging my support shoes around forever...
[fpda4wo] (score 1, diepte 9 OP) 😂😂
[fpcyscc] (score 1, diepte 5 OP) Ah the beacon v2 and FuelCell  Rebel/Propel were in my list at one point, I have to make a decision!
[fpdaid5] (score 1, diepte 1 OP) Ah, it was on my list as one point...i have a pair of Adidas skate shoes (which I love) but never tried their running shoes
[fpd0rd3] (score 1, diepte 0) It might not be the stability features that are the issue, just the particular stability shoe you are using. Have you tried the Mizuno wave inspire? It's not a super light or low-drop shoe, but it's very responsive and not squishy.
[fphg80o] (score 1, diepte 2) Nice!
[fphnrre] (score 1, diepte 4) !IGNORE
[fpe0c5m] (score 1, diepte 0) I've been running in Nike React Infinity and Brooks Glycerin lately.  I have no aches or pains anywhere so something is working😇
[fpg3ot7] (score 1, diepte 1 OP) Thanks! Are Brooks narrow around the toe box?
[fph5396] (score 1, diepte 0) No I would consider them normal sized
[fphe41y] (score 1, diepte 1 OP) Cheers, I’ll bear that in mind!
[fphn3ki] (score 0, diepte 3) 𝓷𝓲𝓬𝓮 ☜(ﾟヮﾟ☜)
#Nice Leaderboard
**1.** `u/RepliesNice` at **6963 nices**

**2.** `u/spiro29` at **5748 nices**

**3.** `u/GreenAppleCZ` at **5081 nices**

**...**

**271870.** `u/Ethanssss` at **1 nice**

---

^(I) ^(AM) ^(A) ^(BOT) ^(|) ^(REPLY) ^(**!IGNORE**) ^(AND) ^(I) ^(WILL) ^(STOP) ^(REPLYING) ^(TO) ^(YOUR) ^(COMMENTS)

=== THREAD gzapb0 ===
SUBREDDIT: r/goodyearwelt
DATUM: 2020-06-08  SCORE: 43  REACTIES: 29
TITEL: [Review] Viberg Slippers in Camel Oiled Calf - One Month Review and Those Insoles
POST (source_id=post):
Hey Ya'll,

Hope everyone is well and staying safe. With the slight extra time these days staying inside, I've had a little more time to write up some more reviews. The latest is this one month review on the Viberg Camel Oiled Calf Slippers. It's fairly quick and to the point, but I also do talk about fixing up the insoles that have been slipping. We've noticed a few batches (inconsistently) come through over the last 6-9 months where the insoles were not staying put. The result was a sliding insole that basically bunched up in certain areas.

Again, not much to it other than picking up some rubber cement and applying it. But figured for those who may not have figured out a way to fix it, here's one way.

**For a full read:**  [https://theshade.witheredfig.com/2020/06/worn-viberg-slippers-in-camel-oiled-calf-one-month-review-and-those-insoles/](https://theshade.witheredfig.com/2020/06/worn-viberg-slippers-in-camel-oiled-calf-one-month-review-and-those-insoles/)

**Or for a quick and dirty, TL;DR:**

All in all, these are a lovely pair of slippers that are much more versatile than you may think at first. It's a fairly "standard" light brown leather color, but I think it's got a bit more character than Natty CXL. A bit more grain, a bit more pull-up, and some more variation that results in some inconsistent leather throughout. The leather outsoles are comfortable and break-in quickly. They bend nicely and easily where they should, and look to be holding up fairly well after one month (although probably just 3-4 wears/week). The leather insoles though - they did start sliding around and after getting tired of adjusting them every so often, I picked up some Barge's All-Purpose Rubber Cement. I did a quick check in with Steve of Bedos Leatherworks and he personally uses Master's Rubber Cement, but he said both would work fine for the purposes of this.

Sizing-wise, I am a 10E Brannock and wear 9.5 in most 1035/2030 Service Boots, and took an 8.5 in these 2010 Slippers. They fit well with no socks (which is how I wear them). I could size down to an 8 for a very-very-very tight fit and prayed that it would stretch. However, I'm confident 8.5 is the right size for me, it's snug enough without being too constricting. My heels to pop up a little when I walk, but with how the overall slipper surrounds your feet, they won't be falling off anytime soon.

&#x200B;

[Viberg Slippers in Camel Oiled Calf - One Month Review](https://preview.redd.it/q5iq3z7rqr351.jpg?width=1024&format=pjpg&auto=webp&s=5a262fe3a948f01d45f45995c4219a90c375e272)

[Some Barge All-Purpose Rubber Cement To Lock In Those Insoles](https://preview.redd.it/ld3c6e4wqr351.jpg?width=1024&format=pjpg&auto=webp&s=73a0ec13e9d67209081ecd2da78a6fc59908de1b)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ftf65d7] (score 45, diepte 0) Wtf is having to buy rubber cement to fix $500+ one month old leather slippers.
[ftf6htx] (score 22, diepte 1) For what it's worth, insoles coming unglued has happened to 100% of my shoes I wear or have worn barefoot - including OSB, Quoddy, Rancourt, and Allen Edmonds.  It's not a huge deal to repair with shoe cement, but I don't disagree that for the price you'd think Vibergs would last longer than a month without need for repair.  

Good on Withered Fig for being transparent with their review and providing a solution to the problem.
[ftf6rs0] (score 11, diepte 2) Huh. Personally never considered it a “repair” any more than I would call changing windshield wipers a repair. It’s a normal thing to do in the course of ownership.
[ftf8ufj] (score 11, diepte 3) Yeah, I’d say that’s semantics. Repair, cost of ownership, maintenance. Whatever you want to call it. 

The point I think we agree on is that insoles come loose, and while a month is a little early for that to happen, it’s going to happen when you wear shoes barefoot.
[ftflk3a] (score 9, diepte 0) This isn't a super flashy design but my lord it's such a solid make-up.
[ftfcge2] (score 6, diepte 0) TIL that Withered Fig carries size 13 in (some) Vibergs. The first and only stockist I have found to do so. This is simultaneously fantastic and horrible (for my wallet) news.
[ftfnddj] (score 5, diepte 3) I'll offer the minority report here and say that the only shoe I've ever had to reattach the heel pad to was a pair of 50 year old Florsheims.
[ftgiaic] (score 5, diepte 1 OP) Actually from my experience, wearing socks with regular sneakers ends up being much more stank over time than these leather slippers with no socks.
[ftg2c4e] (score 4, diepte 1) Not if you use shoe trees
[fth0q6y] (score 4, diepte 1) Everyone's different. Some folks wear no-shows, and use foot powder and shoe trees, but still experience foot odor. Some folks do nothing to mitigate odor and have no issues.
[ftf93i2] (score 2, diepte 4) Agreed. It’s happened on all my footwear worn barefoot as well
[ftfsg9c] (score 2, diepte 5) Good point, I wear some pairs sockless, but not super often. Never had a heel pad come off on those, but it would take a while given my use.
[ftfru8n] (score 2, diepte 1) Exactly how I feel. It’s not flashy but is just really nice.
[fti1nu9] (score 2, diepte 2) I think it also depends on sock material. 
For me (in decreasing order of stank)
Poly socks >>> cotton socks > bare feet >> wool socks.
[ftlfk9s] (score 2, diepte 2) These are great, but not taking orders now and another 6-8 weeks to be made, summer’s over! Maybe for next year...
[ftj3etk] (score 2, diepte 0) Nice review, what an interesting leather!  
I've been loving my [washed natural kangaroo pair](https://i.imgur.com/goXSyP7.jpg), some heel pads solved my similar slipping issue immediately.
[ftn6pne] (score 2, diepte 0) I've seen those on the website. I'm more of a fashion guy than a boot/classic menswear guy, but these things look amazing.
[ftfpqc4] (score 1, diepte 4) Always good to collect more case reports! Just to be sure: do you wear shoes sockless, ever? That’s the only footwear that I see it happen consistently
[ftior6s] (score 1, diepte 5) Plenty of reports of this happening on boot insoles also, Viberg have said they changed insoles/ glue they use which is causing issues.
[ftiu5ag] (score 1, diepte 6) Interesting, and good to know!
[fthlk2i] (score 1, diepte 3) Yeah I’ve used Barges on all three pairs of my commando sole Indys. Things that are glued on just have to be re-glued after some time.
[ftgf890] (score 1, diepte 2) Hmm my insoles on my J Fitzpatrick loafers have been solid. Wore it barefoot 3x a week for a good 3 - 4 months.

Maybe it will happen in the future, but 1 month in sounds ridiculous to me.
[ftfm2fu] (score 1, diepte 1) They've started going back to just a leather sock liner instead of a padded one I think in part of the difficulty in securing the padded one (it was a lot thicker and has an arch portion to it too)
[fthj6py] (score 1, diepte 1) I had to do this recently with my viberg service boots after about 10 wears (tops). The insoles started migrating around
[ftfw4wx] (score 1, diepte 0) Wearing impermeable leather footwear without socks is just a stank factory right?  

Love the style. Hate the thought of wearing around.
[ftj42f6] (score 1, diepte 1) Anecdotally, and not the model in OP's at all, but I got these to wear without, during summer:

https://markalbertboots.com/collections/mens-collection/products/loafer-antique-tan

I'll have to test at the end of the season perhaps, but so far they seem more resistant than a lot of my other shoes.
[ftk17rl] (score 1, diepte 2) Those look great.  I’m still paranoid to spend that much on an experiment for my stank ass feet.
[ftlqqgg] (score 1, diepte 3) Saw that about covid-19, yeah.  I had mine via special order due to width, \~6 weeks and done., so that seems about it during normal times.
[ftq1wxk] (score 1, diepte 0) If any of you are looking to buy a more affordable version of this check out Frye's website. The Chris Venetian loafer in tan is pretty similar.
[j6ovc1f] (score 1, diepte 1) Thank you! This helped a lot!

=== THREAD w4wl1v ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-07-22  SCORE: 2  REACTIES: 28
TITEL: Outside of foot pain while running
POST (source_id=post):
So 1 just got some new running shoes - the Nike Air Zoom Pegasus 38's, and they feel amazing when walking around. However, whenever I run with them, I get extremely intense pain in the outsides of my feet and partially the arch of my feet (I have pretty high arching feet) - and sometimes this even forces me to have to stop running due to how bad the pain is. And I am not sure what to do, so I was wondering if anyone had any recommendations regarding what I can do to fix this. Any help would be greatly appreciated!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ih4ozmz] (score 6, diepte 2) If it was me I wouldn’t bother with insoles yet. I’d concentrate on getting stronger and stretching. If I was going to buy insoles it would be from Academy Sports or REI. I wouldn’t waste money on custom ones
[ih4ny7m] (score 5, diepte 0) Look into stretches and strengthening exercises for plantar fasciitis and peroneal tendinitis
[ih6oj9q] (score 3, diepte 1) I’d second this opinion. Assuming your shoes are the right size, it could be a mechanics thing. I had peroneal tendinitis that resulted from Achilles tendinitis. Started out as tenderness and then pain on the outside of my foot. Initially thought i had PF. 

After some PT, I had to really focus on muscle imbalances and strengthening my weaker side. So, a lot of eccentric raises, balance work, squat variations, etc.
[ih5bxeb] (score 3, diepte 1 OP) Why?
[ih5cb16] (score 3, diepte 3 OP) Yes, I just bought them, I do not know much about running shoes. They seemed great to me at first - until I began to have pain while running in them
[ih5xkhp] (score 3, diepte 0) That happened to me when my shoes were a size too small. Like, they felt fine, fit well for walking but i would get intense pain on the outer side of my foot from running in them (hoka arahi), i went up one size after doing the foot measurement picture scan on their website and BAM, all gone. Maybe it's as simple as that.
[ih5qew8] (score 2, diepte 4) I do recall some people mentioning this outside of foot pain with Pegs 38, but at the same time I know a lot more people who wear them happily.

In my opinion if any shoes are causing you pain, return them. I did the same with Invincibles - great shoes, but they were hurting me so they went back.
[ih7bnr3] (score 2, diepte 8) When you say Puma has never worked for you, have you tried any of their shoes in the last year or so? They basically redid their entire range and came back to the market with some very competitive trainers.

I tried these but returned them all for various issues that may not affect you:

 \- Nike ZoomX Invincible Run FK1 - very good shoe but the forefoot cushion was bottoming out for me causing me pain. Could be because I was too heavy for the extra soft ZoomX foam.

 \- Nike React Infinity FK2 - arch support was too high for me, digging into my arches and causing pain. Didn't get to try them because of that but they use the same React foam as Pegasus so it might be something worth a try? The FK3 is now out which is almost identical to FK2

 \- Reebok Floatride Energy 4 - this is the cheapest of all the shoes I tried (RRP is £70 but they were going for £35-40 in sales recently). I actually liked them, they felt similar to the Pegs. The only reason I didn't keep them in the end is becaue the Pumas felt more fun and versatile.

I don't think Adidas have a good "daily" runner in the offering at the moment. Boston 10 and Adios 6 are good trainers but for very specific uses. They also have strong offering on supershoes, but nothing to compete with in the "do it all" shoes from other brands. I owned Ultraboosts 19 and they just feel dead and heavy, only use them for walking now. I also tried 21 & 22 but I couldn't get a good lockdown with the laces so my foot was all over the place with them. Also the heaviest running shoes I've worn to date.

Other than that I have no other own experiences of versatile dailies.
[ih5l1n7] (score 2, diepte 2) They’re a great shoe… for some people. Everyone’s foot is different, and if they’re hurting your feet, they’re obviously not the right shoe for you and your feet.
[ih5ynkq] (score 2, diepte 1) Yes it sounds like he has narrow shoes hurting his feet when it starts to swell.
[ih71dxp] (score 2, diepte 2) Do you think it could be the width, that you may need the wide version?
[ih725nt] (score 2, diepte 4) I think some are just narrower than normal, as far as i remember nikes are notorious for being narrow
[ih72bpm] (score 2, diepte 5 OP) Got it
[ih4o7ve] (score 1, diepte 1 OP) Awesome, thanks! Also, do you think that insoles could help? And if so, what kind?
[ih713ga] (score 1, diepte 2 OP) Awesome, thank you!
[ih5a8ti] (score 1, diepte 0) Don’t wear the Air Zoom Pegasus 38’s
[ih5ipe7] (score 1, diepte 3 OP) Are they actually really bad? Should I return them?!
[ih71b66] (score 1, diepte 5 OP) Got it, thanks! Also, do you have anything recommendations?
[ih772om] (score 1, diepte 6) I can highly recommend Puma Velocity Nitro 2. Very simillar to Pegs, slightly softer and a bit bouncier.

Saucony and Asics also have some good alternatives, but not at this pricepoint. You will end up paying 30-50% more with those brands.
[ih78air] (score 1, diepte 7 OP) Thank you! However, Puma's never worked for me - do you have any Nike or Asics recommendations? Even Adidas?
[ih7d63u] (score 1, diepte 9 OP) You are the best, thank you so much. I really appreciate your time - I will look into those!
[ih715ga] (score 1, diepte 3 OP) Yeah, that's true
[ih70zjy] (score 1, diepte 1 OP) Thanks for the tip, however, I am typical a US men's 10.5 - but for these, I went up to an 11
[ih71puf] (score 1, diepte 3 OP) Oh that is a good point, that could do it. However, I never have had wide feet - but I did feel that the insoles of the shoe slanted outward, causing me to naturally supinate... causing such pain
[ih7amcn] (score 1, diepte 0) definitely agree with others - insoles are critical - most running shoes dont have much arch support. I also have high arches and I've tried every brand of insoles on the market. Ultimately, I switched from my custom insoles to this brand called [Fulton](https://walkfulton.com) and immediately all of my foot pain went away (and back pain). These are made from cork so they mold to your arch and absorb shock/impact - definitely recommend
[ih7aqiy] (score 1, diepte 1 OP) Thank you so so much!
[ih4rmhz] (score 0, diepte 3 OP) Okay, thank you!
[ih5c8e4] (score 0, diepte 2) That’s an honest question, you’re not trolling?

