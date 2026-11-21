# Label-batch batch_0101

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
Schrijf het resultaat naar `batch_0101.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: wdt7v8, 12fu4am, 78sbip).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD wdt7v8 ===
SUBREDDIT: r/solotravel
DATUM: 2022-08-01  SCORE: 176  REACTIES: 75
TITEL: NYC on a budget
POST (source_id=post):
I am a 30F Canadian and this was my first totally solo trip (other trips have had solo time but not start to finish).

Budget: I aimed for $1,000 CAD. Came in at $1,062 (about $827 US). A basic breakdown is as follows:
Bus: $261
Hostel: $348
Cell data: $6
Medical insurance: $37
Museums: $77
Cash: $332, $250 US. The cash got me my week long metro card, the city tax at the hostel, magnets (the only souvenirs I buy), a $5 special exhibit at a museum, medication, and food. I actually ended up with a few dollars left over, even after getting McDonald’s at a rest stop on the way home (that I regretted lol).

I ended up slightly over budget because I decided at the last minute to get travel medical insurance, and then I ended up not bringing enough sinus/allergy medication. 

Trip length: 6 days/5 nights. My bus left Toronto Sunday evening and arrived Monday morning. My bus to Toronto left Saturday night and arrived Sunday morning. 

Accommodation: Q4 hostel in Queens, 4 bed female only. No complaints, but I really lucked out with roommates, which can make or break it. Right near subway stations so it basically close to everything. 

Activities:

Monday: dropped bag off at Q4, went to the MET, did the Roosevelt Island tram (included in Metro card), wandered around a little, early night!

Tuesday: walked the High Line, checked out Chelsea Market, Little Island, Greenwich Village, Washington Square Park and Soho. Then I decided to subway up to check out the indoor garden at the Ford Foundation, then wandered around Midtown East and that corner of Central Park. 

Wednesday: checked out some stuff along Hudson River area including some piers, then did the New York Fire Museum. After that I walked over to Little Italy, Chinatown, and the Flatiron district. I checked out some exhibits at the New York Public Library, Bryant Park, and then did the obligatory ten minutes in Times Square. 

Thursday: checked out the Only Murders in the Building building and wandered around there for a little bit before doing the American Museum of Natural History. There was a free entry afternoon at the Museum of the Moving Image so I booked it over there for an hour of that, then took a scenic route back to the hostel. 

Friday: went to Brooklyn. Started in Dumbo, walked along the water for quite a ways, then over to the New York Transit museum. Walked the Brooklyn bridge. Walked around the financial district for a while, saw Battery Park, Stone Street, the Oculus. Then subwayed up to the Morgan Library and Museum for their free evening, and walked around that area. 

Saturday: did a lot of Central Park. Started in the top left corner and zigzagged through. Skipped the bottom left which I had been to before. Wandered around midtown east, then checked out the Rockefeller Centre, Grand Central Terminal, then down through Murray Hill, Gramercy Park and Alphabet City. 

What went right/wrong: Pretty much everything went right. I used the app Wanderlog to list out all the stuff I wanted to do and then made potential routes. I didn’t anticipate hitting all of the stuff but I got most of it. I kept things flexible due to the weather. I had a few days planned out that were mostly indoor and then moved those around the days it called for rain. I found that I had a hard time visualizing where things were but the app made it easier to see and plot out days. The last time I went I didn’t realize until later that I was really close to some interesting things but didn’t know about it, and I didn’t want to miss out this time. 

The only thing that wasn’t really worth the time to me was the Brooklyn Bridge. I’ve heard you get great views on the bridge, and I don’t think you do. Too much structure in the way. I walked it to say I did and because it was a nice day, but regretted it shortly after due to it being crammed with tourists. I’d subway back and forth next time. Brooklyn waterfront had amazing views of the city though (also got to creep on a Succession set on one of the piers in the Financial District through the binoculars which was a personal highlight for me). 

Food: the main cost saver was food. I am NOT a foodie (though I love food). I don’t drink except at parties/events where drinking is expected. I got Dunkin donuts a few times out of sheer laziness. I got free Van leeuwan ice cream twice through keeping an eye on Instagram. For meals I had one sit down diner, then bodega/hole in the wall take out (panini, omelet, burrito, 2 Bros pizza). I did spring for the Los Tacos once, and Shake Shack once. I got some treats at Emack and Bolio’s ice cream in Midtown and Stuffed Ice Cream. I also got two pretzels from food carts in Central Park because I love them. But overall, not a lot of food. I drank mostly water but had a couple of pops and one bubble tea. 

Safety: I was very conscious to not look like a target. I’m a plain looking white girl so I tend to blend in, and I got asked for directions about 5 times. At no point did I feel unsafe. It sounds horrible but I actually encounter more aggressive people on my walk to work (which says more about the worsening issue in my city more than NYC). There were people sleeping off to the side on streets, some silently holding out cups, a few asking for money on the subway but addressing the crowd, not individuals. The most unsafe I felt was in Times Square due to the crowd, increased change of pick pocketing, cons, etc. Cops patrolling the area with big fucking guns made me even more uncomfortable. I didn’t feel on edge like that anywhere else. 

What I skipped: I was there a few years ago and did some of the more touristy things. Ferry by Statue of Liberty, Empire State, Wall Street, 9/11 site (no interest in the museum), a bus tour. I didn’t feel like those needed to be revisited (unlike the MET and AMNH).

Recommendations: Loved all of the smaller museums I went to (transit, fire, moving image). All worth the ~$10 entry. The MET and AMNH were treats. I had been to both before but don’t think I covered either enough (didn’t realize at the time just how massive they are). The only annoying thing about them is screaming children but I don’t think there’s a time of year you can avoid that!

Also, I can somehow walk a lot. I ended up with a few blisters (under already calloused areas!) but manageable. I walked 182,000 steps and 122 kilometres over the 6 days. I walked around a lot of places as opposed to going into buildings. Usually I walk with headphones or a podcast but didn’t use them once. Instead I just listened to the city and it’s people. I saw a lot of tourists walking around in nice shoes/heels/sandals and it was just baffling - I needed my Skechers and my converse with gel insoles. Clearly I’m getting old. 

Final verdict: Highly recommend!! I can see how it can get expensive for sure if you like quality food, are into the theatre, or want to do tours. The next time I go I hope to be able to spend a little more but it was a very good budget option, despite so many other trip reports with higher budgets. I would like to go out at night more to bars and such, which I did not do due to safety and budget, but I don’t really feel like I missed out. I could go back in a few years and still have plenty of new things to see and do.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iil7voe] (score 63, diepte 0) As someone that lives in NYC, you absolutely crushed it! So many of my favorite activities on this list
[iillfvr] (score 47, diepte 0) pro tip: there's no need to buy a week unlimited pass anymore because tapping your phone to pay will automatically get you the pass once you get to the breakeven point (12 rides)
[iilt7f6] (score 39, diepte 1) That only works if you don't travel over Sunday/Monday.  OMNY resets on Sunday night, so if you're a visitor who arrives late in the week, it's likely you'll do less than 12 trips before it resets and the count to 12 starts again.
[iil15wj] (score 25, diepte 0) Wow, that's quite the impressive trip.  You definitely crammed in a ton of stuff in a short amount of time.  Thanks for sharing!
[iilby7g] (score 19, diepte 1) Not OP but if you have a smartphone finding your way around is completely idiot-proof. I visited NYC for the first time a few months ago and was nervous about finding the right subway stops and getting lost. Pffffft like you literally pull up Google maps and type in where you want to go, and it will tell you the exact location of the nearest correct subway stop AND which line to take AND what signs to look for once you're down there AND all the stops your subway will make along the way. It also does the same for bus routes.

That combined with the absurdly simple layout of the city makes it sooo easy to find your way around. Seriously, don't even sweat it.
[iil55zo] (score 17, diepte 1 OP) Yet it didn’t feel crammed at the time! I think the key was doing most of the advance ticket items (like the museums) first thing in the morning so that I could spend the rest of the day wandering about doing whatever without needing to be anywhere at a specific time. I was able to cover a lot of ground that way. I also left Saturday as a totally open day. I didn’t actually have anything planned for it, it was just overflow from what I didn’t get to during the week.
[iil5vxu] (score 16, diepte 1 OP) I think walking everywhere really helped, and seeing things along the way instead of making an effort to schedule time to go. For example, I didn’t actually plan on going to Little Italy or Chinatown, but I found myself over that way by mid afternoon and just carried on through. I think being able to go at your own pace is such a huge advantage to solo travel, and as I was leaving I thought about how having someone else with me probably would have slowed me down.
[iil34lu] (score 14, diepte 0) So impressive how much you got in and at such a reasonable cost in NYC!
[iil9uny] (score 13, diepte 0) Love this! 

What you did is a dream of mine: a trip alone to New York and not spending a ton. I'm saving your post and will revisit it when the time has come for me to dare to do what you've done.

 One question, was it difficult to manoeuvre/find your way using public transit? 

Did the app help with that?

 I'm just scared to get lost. It's not a deal-breaker of course but it's something that's on my mind every time I even start to think about this trip.
[iil58ok] (score 11, diepte 0) glad you enjoyed our beautiful city!
[iilf0la] (score 8, diepte 1 OP) Thanks!

I don’t find it all that confusing. Everything is pretty well labelled. But I rely heavily on Google Maps, even at home. I just put in my destination and it tells me which line to take and the end stop (so you know which direction to go). I saved NYC on my Google maps so I could use it offline which was super helpful. It had all the streets and stations, and then somehow also knew my location, so I could navigate by looking at a transit map. 

I had two issues with transit on the trip. The first was me being dumb. I forgot that some stops are one way only - the entrance to the other direction would be across the street. So I saw the sign saying the line, entered the station, swiped my metro card, and realized when I was already through the gate that it wasn’t the direction I wanted. So I left the station, crossed the street, went to the other station, and my card wouldn’t swipe. It can’t be used so quickly, it’s like a 20 minute wait. I explained what happened to the attendant and I apologized and he let me through even though he clearly thought I was an idiot. You just have to be careful to read the full sign before going in, because it is clearly labelled, I just forgot, and up to that point every station I had gone to had a way to cross. 

The second was just finding the damn entrance. Most of them are stairs going down, and the signage is along the railing. When there’s a lot of people, it can be hard finding it. I got really turned around in Time Square trying to find the station and ended up walking around in circles until I spotted it. 

Getting lost isn’t the end of the world though, and can make it more fun. I did my ticketed items first thing in the morning when possible so after that, I didn’t have a schedule to adhere to. It would be more nerve wracking if I had places to be at certain times throughout the day but most days I didn’t, so that was nice. I lost about 15 minutes of my day walking in circles in Time Square but no big deal.
[iimujnc] (score 7, diepte 1) Hard agree!! What a great trip, and totally great that you were able to see and enjoy so much on such a small budget! I’m totally going to recommend that wandering app to friends who come visit.
[iilp7k9] (score 6, diepte 1) If you are ever at 34th st on the east side, walk out to the east river and take the ferry to Wall Street. For most of the way it travels along the east bank so you get a spectacular view of the city and the traffic on the East River. 
A sunset ride is just spectacular.
[iildosx] (score 5, diepte 0) Next time try the nyc ferry.  Not the staten island ferry but the one that takes you from Wall Street to lic or Brooklyn.  I live here and it’s extremely safe.  No one really bothers you and pickpockets are basically only in Times Square.
[iimvqld] (score 4, diepte 1) Also people in NYC love showing off how well they know their way around if you need directions.  IME New Yorkers will tend to ignore everyone (not unfriendly just indifferent) until you look lost and then everyone is very helpful
[iilrex9] (score 4, diepte 1) thank god for omny 🤩🙏
[iikwmn8] (score 3, diepte 0) Great post
[iio0e0z] (score 3, diepte 1 OP) Thanks! I read a lot of blogs and such from people who live there because I wanted to avoid tourist traps and see more of the city itself. Even though I saw a lot of stuff, I feel like there’s still plenty more to see and do, would love to go back in a few years!
[iince1e] (score 3, diepte 1) Most of the main rails you go on either go up or down they aren’t doing anything crazy. I just finished my nyc trip yesterday and I did get lost once going on the right train going the wrong direction, but that was it. It’s pretty simple with google maps as it tells you the train name and arrival. 

Also the streets are insanely easy to figure out where your stop is they’re basically like 42 street, 43 street, 44 street, first ave, second avenue, etc. Basically incrementing street numbers
[iilaxo7] (score 3, diepte 0) That sounds like an amazing trip, I hope to do many of those things next time I get to visit NYC. Such an incredible city.
[iinjt9h] (score 3, diepte 3) God I'm jealous. The TTC was supposed to have it implemented a decade ago and the *earliest* it's expected at this point (without any progress reports) is 2023.
[iiq7c6i] (score 3, diepte 5 OP) Dude, feel free to check my post history, not an ad. It wasn’t even good, it was just there. My honest review is that Tim’s is better (which is already a low bar nowadays), and the medium iced coffee was the same size as an extra large Tim’s, which made me want to see how ridiculously sized an extra large Dunkin would be (never did get one because the first one was meh). Super weird to think a brief mention of going to Dunkin is an ad 😂
[iikz7eu] (score 2, diepte 0) Thanks for sharing, sounds like a great trip!
[iilfcm5] (score 2, diepte 2) Ok! Thank you!
[iio2bk4] (score 2, diepte 1 OP) I had the ferry on my list as a maybe, and thought about using it to leave Brooklyn but opted to walk the bridge (never again). It’s definitely on my list for next time!
[iili35q] (score 2, diepte 0) Wondering if you can share details on the bus ride!!! Lots of helpful stuff already thank u
[iiljddf] (score 2, diepte 0) Such a great write up!
[iill19d] (score 2, diepte 0) Thank you for sharing your trip!

I’m from Montreal and planning a solo trip in NYC soon. How was your experience with an overnight bus? The last time I took it I couldn’t sleep at all and it’s 9 hours long…
[iingbg8] (score 2, diepte 2) since march 31 2019
[iim26j3] (score 2, diepte 1) The PATH from Jersey City is a different system so pricing is different but you can use the same metrocard for both. The bus and subway are the same $2.75. An unlimited card for NYC MTA may make sense if you use it enough during your stay, but won’t cover the PATH. In general, staying in JC works quite well with direct PATH routes to World Trade Center or midtown (with other stops in between)
[iinolrf] (score 2, diepte 3) Unfortunately no. A single metrocard can have both a time value (unlimited NYC subway) and a dollar value which you can use for the PATH. But unlimited NYC MTA doesn’t pay for the PATH. They are run by separate agencies.
[iip50kp] (score 2, diepte 5) Once you enter the subway system all transfer to different subway lines are included no matter how far. If you exit, however, it’s a new fee. Subway to bus, and vice versa transfer does work though. Within two hours. All rides are the same $2.75 no matter how close or far
[iio5j6j] (score 2, diepte 1 OP) I stuck entirely to the subway system and the tram once (which was covered by the card). I know the card works for the buses too but I didn’t need to use them. Not sure about how it works from Jersey though, unfortunately.
[iio96vt] (score 2, diepte 1 OP) I talked about the bus ride in a few other comments (pretty lengthy because it a bit of an adventure on its own lol)
[iilzyfc] (score 2, diepte 0) Wow! This is incredible! Thanks for sharing. My trip costed me over $2000. Way over my budget and that wasn’t including the rent. I need to watch out for those restaurants and out of the blue bar hopping.
[iio5tak] (score 2, diepte 1 OP) Thanks! I browsed a lot of menus and I think food/drinks is what can really get you. But for a lot of people that’s totally worth it! I have a relative who is a big foodie and she was shocked that I didn’t plan to do any nice restaurants or have drinks. One day I hope to go back with a bigger budget and splurge on all that!
[iima8wy] (score 2, diepte 0) Hey, I stayed in Q4 when I was in NYC about a decade ago! Glad to hear it's still alive and kicking. I recall enjoying my stay. At the time, it was quite close to https://en.wikipedia.org/wiki/5_Pointz, and I think it was demolished shortly after I left... a shame.
[iimnneb] (score 2, diepte 0) Thank you for the report! This is exactly what I need because I've been thinking the past 3 days if I should go to NYC for my next trip but I'm scared to do it since I heard it's unsafe these days.

A question, did you always brought your passport with you all the time? And what about money? Coming from Asia, I don't want to rely on credit card so I'm thinking to bring cash. But I'm worried if I get mugged and lost everything. I won't be able to put all my money in my wallet, so I'm thinking to split it to my backpack as well but still worried about the mugging.

And I'm a night owl, is it still safe to walk around past 9pm? I usually just wandering the city looking for convenience store for snacks. Also planning to skip restaurant and straight to junk food to save some money.
(39 reacties met lagere score weggelaten)

=== THREAD 12fu4am ===
SUBREDDIT: r/WaltDisneyWorld
DATUM: 2023-04-08  SCORE: 53  REACTIES: 48
TITEL: April 1-6, a report of what worked for us
POST (source_id=post):
Hi, all! Someone did this recently -- listed out all the things that worked for them and what didn't --  and it was helpful to me, so I am hopeful this might be helpful to others who are planning! Our fam -- me (DW47), DH55 and DS12 -- went on our very first trip to WDW this past week. It was crazy busy but also really fun. We stayed at POFQ and hit one park each day except for Day 2, which was Epcot and then Hollywood Studios After Hours. I planned and planned and planned; here is how stuff shook out for us.

**Worth every penny to us**

* One backpack and one fanny pack. We bought the Eddie Bauer [20L Stowaway Packable Backpack](https://www.eddiebauer.com/p/82300168/Stowaway-Packable-20L-Backpack?rrec=true&sp=1&size=ONE%20SIZE&sizeType=&color=Reef) while it was on sale around the holidays for $15, down from $30. Right now it looks like it's gone up to $40 for base price but it's on sale a lot. That worked for us and was plenty big. DH usually carried that; I carried a Fjallraven [fanny pack](https://www.rei.com/product/203693/fjallraven-high-coast-hip-pack) with my phone, charger and other quick needs. I really liked being able to just shift it to the side when I was on a ride that had a pull-down bar.
* Two 20-oz. insulated water bottles. Initially we carried one, but it discouraged us from drinking as much as we really needed to. We thought the water refills and stations would be more plentiful in the parks than they were, and they were also often pretty well camouflaged. We did what someone here suggested and filled up with ice at the resort and just topped up with water to start each morning. Even with the insulation, there was plenty of melted ice water any time we were thirsty!
* Dramamine for DH. He's someone who gets carsick easily and loves roller coasters much more than they love him back. He started taking it on Day 2 and it really turned the trip around for him.
* Sporks and straws. We got this [three-pack of Humangear sporks](https://www.amazon.com/dp/B01C6HBN96/ref=twister_B084NS4PS7?_encoding=UTF8&psc=1) and this [spork/knife combo](https://www.amazon.com/UCO-2-Piece-Integrated-Camping-Utensil/dp/B07MMTTJXJ/ref=sr_1_32?crid=1V4ZQQMM2M30J&keywords=sporks+reusable&qid=1680972698&sprefix=sporks%2Caps%2C110&sr=8-32). Together they worked great and were sturdy enough to take on anything we were eating, and we didn't feel quite as bad about all the waste. The straws were alright but we mostly drank water out of our water bottles so I think we ended up using those twice; we just brought silicone ones we had in the house.
* My trusty old sneakers. I had gone and gotten myself some fancy shoes (that rhyme with mocha) and dutifully walked around in them for weeks. And they always hurt a little bit but I thought that was just how my feet were going to be! But on the day we were leaving I grabbed my old New Balance trainers from like 9 years ago and wore those the first day -- no pain! I treated myself to the mochas for the second day and it hurt so much! So back to my old sneakers, which were great for the rest of the trip. If you have good shoes, you will be fine!
* This may be controversial, but Genie plus and Individual Lightning Lanes. We used it every day except our first day at Epcot, and we did use it our second day there. We used ILLs for the big rides that we couldn't get for free VQs: Rise and Flight of Passage. Did VQ for Guardians and Tron; both worth the wait in line. Did not get an ILL for 7 Dwarfs because, come on. The whole thing was expensive but we found real value in it.
* Food at: Satuuli Canteen in AK; Sunshine Seasons at Epcot; ABC Commissary in HS; and Morimoto Asia. Also the basic popcorn tub and refillable drink cup at the resort.
* Nonsanitizing hand/face wipes. We also had the sanitizing ones, but the gentle ones that could wipe away messy food were awesome at times when we really felt grimy but weren't ready to get up and hit the bathroom.
* Food for breakfast in the room: A bag of pre-cut bagels; a small jar of peanut butter; a bag of apples; a bag of small oranges; bags of almonds, cashews, pumpkin seeds, sunflower seeds. Great to have a relatively non-labor-intensive, nutritious start to a day that would include lots of less-nutritious things!
* Snacks for the parks, specifically beef jerky (Jack Links Teriyaki was a hit) and Keebler Cheese and Peanut Butter sandwiches. I found myself at Target just kind of lost and wandering just before the trip. If you do, too, these are ones that are solid (if you don't have food restrictions) and that we kept coming back to while in the parks and in line and sometimes even just in the room. The protein helps esp after all those steps.
* Zipper-type bags. Worth every penny on these! We got some popcorn on Day 2 before getting on GOTG and the tub popped open and spilled in the ride car! I was mortified. After that I put all my popcorn refills into a gallon bag right away. No more spills!
* Phone charger. One of my weird pandemic lockdown buys was a bunch of Anker phone chargers. I do not know why. I thought it would be slightly more apocalyptic than it was? Anyway, it came in handy for my Samsung S9 though DH never really needed it for his iPhone Something.
* Moleskin. Cheap as heck and worth so much. I cut it into various-sized pieces before we left and I ended up using most of them after that day with the bad shoes. DH also used a few. Worked great.
* MagicBands. I was going back and forth on this, but it was really convenient to just tap in and pay for things with our little wrists. I got the $10 ones from ShopDisney and I did get DS a plain MB+ so he and DH could track down villains in Batuu; he did get some fun out of that but that day was so dang hot that they gave up after 5 bounties. Also got some [Bit Belts](https://www.amazon.com/Bitbelt-Protect-Magicband-Fitbit-Vivofit/dp/B010OX42WO/ref=sr_1_2?crid=3FVRTYQ9VXXV2&keywords=bit+belts&qid=1680976703&sprefix=bit+belts%2Caps%2C112&sr=8-2) to keep them affixed, which worked great.
* Staying on property. This is also probably controversial but I loved having someone drive me home at the end of the day. It also allowed us to easily split up when I needed a break and DH and DS wanted to continue running around the parks. Also we took advantage of Early Entry and RD'd a couple days.
* The individual minifig reservation at LEGO at Disney Springs. It's a zoo both inside the store and out, but the little minifig is pretty beloved.

**Probably was fine and may work great for others but I could take or leave**

* Those little hand fans that people talk about. The days were in the low 90s when we went and they helped a little? But I didn't find us using them that much even after the first time we used them. Also the cooling towels, though I probably didn't put enough water on them.
* Those hydration packets. Again, this may work great for others but I only used one and probably didn't need to go as crazy buying these as I thought I should. Ice water (once we got a system down) worked great.
* Chub rub/glide/etc. I bought some pretty long, snuggish shorts before the trip and so didn't find myself using this after the first day.
* Some Table Service. We did Boma and it was good? But I didn't think the value was quite what we wanted and after a long, hot day, filling up on buffet food was not tops on our list. We had favorite Quick Services in most every park so I think we would skip if we ever came back.
* Those rhymes-with-mocha shoes that betrayed me. 'Cause baby now we got bad blood.
* The PUR filter pitcher I brought down (we had one from other travel) after reading about the water in Florida. It worked fine but the water from the resort quick service was plentiful, colder and tasted better.
* Hollywood Studios After Hours. This, too, may be controversial and it was probably the fact that we had a park day scheduled before it and were just too tired by the end of the day to really get the value out of it. However, it did give us the opportunity to go to Savi's Workshop walk-up and get DS a laser sword, which was the only merch we bought aside from the popcorn tub, the cup and one magnet. So that was valuable, but if we came next time we would definitely rearrange our schedules to make it worth it. Or we would just skip it. One of the rides we really wanted to do again, MMRR, was down the entire time we were there, and Rise was down for the beginning of the night.
* Food at: Cosmic Ray's at Magic Kingdom and the turkey leg at Fife and Drum Tavern in Epcot. Also Les Halles at Epcot. Any food truck food at Disney Springs. :(

**Not applicable to our trip**

* Ponchos. We ended up buying every single kind of poncho (because I like to throw money at a problem): thick reusable for around $6 each, thin disposable for about $1 each, and then little rain jackets that curl up into their own pocket for about $20 each. DH already had one of those and I grabbed one for me and DS. Never rained a drop! I guess I'll just keep the little ones in the glove compartment now.
* Hats. We brought these but didn't wear them. Mostly we were in and out of the sun, doing rides and things; we never stood out for a long time and no one got a burn on their hair parts, as we had worried. DH did keep applying sunscreen to the top of his head, where hair used to be more populous.
* That PhotoPass thing. I just couldn't wrap my head around it so we never got it and I am not missing it now that we're home.
* Park hoppers. DS was worried that we didn't have them going in but I told him that Disney would be happy to take our money at any point if we changed our minds. And we never did! We happened to have enough days to do the parks the way we wanted to.

OK I think that's it. I hope this helps someone!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jfh7tem] (score 19, diepte 0) Great report. What didn't you understand about Photopass? It's just a way to get more family photos and ride photos from your trip. We always wound up with hundreds without much effort.
[jfhdgzv] (score 14, diepte 0) Hoka has a 30 day guarantee. Depending on when you purchased you could get a refund.
[jfh91e0] (score 12, diepte 0) Wow this was so helpful. Also: “IPhone Something” and “laser sword” had me cracking up. I’m like the same exact brand of mom.
[jfhg541] (score 11, diepte 0) >This, too, may be controversial and it was probably the fact that we had a park day scheduled before it and were just too tired by the end of the day to really get the value out of it.

I've done After Hours before, and not doing it the same day as a park day is key. Take the day off, sleep in, have a nice brunch, and get some pool time in before heading over to the park. They let you in 3 hours before the event starts, take advantage of that to squeeze in what you can, and you can have a great evening.
[jfh8k2u] (score 8, diepte 1 OP) Yeah, I probably made it more complicated than it needed to be, but to me it was, timewise, one thing too many. Coordinating when we needed to be where for rides and food was this huge undertaking and then thinking about stopping to take pictures just seemed a bridge too far for my head.
[jfhcxx8] (score 7, diepte 0) > my old New Balance trainers from like 9 years ago 

I go through a pair of shoes every 6 months or so... 
Tell us your secrets
[jfhhl7e] (score 7, diepte 1 OP) OK just got one through Zappos! Thanks!
[jfhaupd] (score 6, diepte 1 OP) I had seen some kind of flimsy plasticware in Epcot review videos, in particular. I thought we'd be eating around the world a lot more than we actually did, but it was good to have reusable ones that I knew were solid for each thing we did eat. They were great tools to help us tackle that turkey leg, for instance. Also, they're a spoon on one end and a fork on the other, not the combo spoon/fork that is common, so they're more functional than you might expect.
[jfhntuv] (score 5, diepte 0) Sounds like you got a lot out of your trip, love to see it! I allllways make it a point to bring moleskin, it comes in clutch every single time. It was great to see a review of the after hours at HS, we’re going in January and I’m playing around with the idea of doing that in lieu of a whole day there. I think we’ll hang at the resort during the day instead of trying to do another park. Thanks for this list!
[jfhhxft] (score 4, diepte 1) And you can do that cool "world" family photo in front of the Epcot ball with this. I always get photopass.
[jfhetwl] (score 4, diepte 1 OP) You are probably a lot more active in them than I am!
[jfhflju] (score 4, diepte 2) Thank you! How did you score the Magic Bands for $10? I just bought them from ShopDisney for $25.
[jfhn5on] (score 4, diepte 0) Which Hokas did you get? My Bondis are easily the most comfortable shoes I've ever owned, they feel like walking on clouds.
[jfh5z34] (score 3, diepte 0) This is a Fakespot Reviews Analysis bot. Fakespot detects fake reviews, fake products and unreliable sellers using AI.

Here is the analysis for the Amazon product reviews:

>**Name**: humangear Gobites Mini UNO 3-Pack, Blue/Gray/Green 

>**Company**: humangear

>**Amazon Product Rating**: 4.8 

>**Fakespot Reviews Grade**: D

>**Adjusted Fakespot Rating**: 2.0

>**Analysis Performed at**: 11-06-2022 

[Link to Fakespot Analysis](https://fakespot.com/product/humangear-gobites-mini-uno-3-pack-blue-gray-green) | [Check out the Fakespot Chrome Extension!](https://chrome.google.com/webstore/detail/fakespot-analyze-fake-ama/nakplnnackehceedgkgkokbgbmfghain)

*Fakespot analyzes the reviews authenticity and not the product quality using AI. We look for real reviews that mention product issues such as counterfeits, defects, and bad return policies that fake reviews try to hide from consumers.*

*We give an A-F letter for trustworthiness of reviews. A = very trustworthy reviews, F = highly untrustworthy reviews. We also provide seller ratings to warn you if the seller can be trusted or not.*
[jfhiasx] (score 3, diepte 2) There’s now one by Cinderella Castle, just up from the wishing well. Don’t miss it!
[jfha2yn] (score 3, diepte 1 OP) :) Close enough, right??
[jfhgk6b] (score 3, diepte 2) I accept that!  Although my top step day ever was at Blizzard Beach; the main park days are often on the low end.
[jfhe1du] (score 3, diepte 1 OP) Oh my gosh! I hadn't even considered that; thank you!!
[jfhhdib] (score 3, diepte 3 OP) Ugh, sorry. I had a $10 off coupon for each one through the resort, and they were $20 at the time.
[jfhnht2] (score 3, diepte 1 OP) Oh I'm glad! I got the Clifton and it's like there's a part in the middle of the shoe that is gone somehow. Like if you've slept in the middle of the bed forever and there's a crevasse there -- there's a crevasse in my shoe that just does not support my foot.
[jfic4hj] (score 3, diepte 2) I looove my Clifton's but I tried on like 8 different types at a running store. Not all shoes work for all people. Glad you had a back up!
[jfi2sw6] (score 3, diepte 1 OP) Ooh good tip on the camelback! 
Which park felt busiest to you? Somehow AK did for us, even though we were at MK for Tron opening.
[jfiozws] (score 3, diepte 0) Wonderful report - very helpful thank you. Glad you had a great time!
[jfkl98y] (score 3, diepte 1 OP) That makes a lot of sense. Have a great time in June!
[jfi7u3m] (score 2, diepte 2) Whats that?
[jfh94et] (score 2, diepte 0) Why the sporks?
[jfi8wnd] (score 2, diepte 2) Glad to hear it!
[jfhf3pk] (score 2, diepte 0) Wonderful trip, report, thank you. I am taking notes.
[jfhf6vm] (score 2, diepte 1 OP) Yay! Glad it was helpful and I hope you have a great time!
[jfhpynu] (score 2, diepte 4) Did they give you a coupon when you checked in/where did you get this?  I know there are pre-arrival magicbands that are 10 dollars off online, but they have no more of the basic MB solid color online anymore.
[jfhscfm] (score 2, diepte 5 OP) I think that's what it must have been -- the basic pre-arrival solid ones.
[jfhokmo] (score 2, diepte 1 OP) Oh yay! I think that is a great plan!
[jfi298y] (score 2, diepte 0) I too was at Disney this past week, camelback waterbottle/backpack worked like a dream!! 

We had hopper passes but the LL/Virtual queue kept us at our reserved park most of the day.
[jfi3qyo] (score 2, diepte 2) Honestly they all felt super busy. I would have to agree animal kingdom was busy from open to close. We weren’t able to catch the avatar ride on individual LL for the entire week. We waited right before the park closed and still took 4 hours to ride.
[jfj6832] (score 2, diepte 2) We were at AK yesterday, and I agree that it felt the busiest (to be fair, with this week’s crowds, it’s a bit like asking which sand is sandiest). My daughter was over it, and my wife nearly had a legit anxiety attack around 1:45. Thankfully, we were heading out. So many people, though, and so so hot.
[jfkgv27] (score 2, diepte 3 OP) Oh, I'm sorry you had that experience. I had a similar one to your wife's around the same time and had to stake out the one alcove with a fan and no people. It was way too much, especially considering I was expecting a more relaxed day that day.
[jfki00o] (score 2, diepte 4) I’m sorry you had that experience, too! It’s hard to navigate that on such a wild day. 

Admittedly, I didn’t help much by saying, “Follow me, I’ll get us out,” and taking a wrong turn and ending up back in Pandora. That wasn’t an easy “my bad” to say.
[jfkjrwl] (score 2, diepte 5 OP) Oh man. I know that feeling! Reading your experience makes me feel like AK somehow does that to people; I had executed every G+ element flawlessly for our group the entire trip except that day. I had very purposely and wrongly cancelled a Dinosaur LL for an Everest LL. The conviction I had when I cancelled it! The yikesness I felt when my family was like, uh, why did you do that?
[jfijb09] (score 2, diepte 0) Why no LL for the dwarfs did you not need one or what
[jfijk8o] (score 2, diepte 1 OP) I just felt like it wasn't worth it to us, given the magnitude of the other rides we had bought with ILLs. Just couldn't square that in my mind. We RD'd it instead and that worked out great!
[jfils9n] (score 2, diepte 2) What’s rded mean? sorry lol and when we went it was the only thing I missed out on LL wise and the regular line took literally almost 2 hours.
[jfilyxf] (score 2, diepte 3 OP) Oh, ha -- the jargon is a bit much; rope dropped. We got in the standby line right at the start of the day. I think ours was 50 minutes or so.
[jfkiy3l] (score 2, diepte 0) Great tips for newbies and vets alike.  Thanks for sharing.

We’ve done Memory Maker and we haven’t done Memory Maker… we always wished we had done it on the trips we hadn’t, so I booked it again for our June trip.  Just a lot easier than trying to do selfies or asking others to take good pictures of us, plus the ride photos are definitely worth it we feel.
[jfm60uc] (score 2, diepte 0) Your comment about the shoes-that-rhyme-with-mocha made me laugh. I too have some, but they make my already big feet look even bigger and since I wanted to be cute (instead of comfortable?), I wore my Keds to the parks and boy, did I regret it. By the last day, I wore my husband's slides because my feet hurt too bad! So cute I was not! My Hoka's are comfortable, but I just don't like the way they look. I have since then bought some Sketchers that feel soooo comfortable AND they don't make my feet look so big.

P.S. - We also like to bring easy things like bagels or bananas for breakfast. We just don't eat enough to justify buying a breakfast meal there, plus we're usually in a hurry to get there. And, we may be in the minority, but we don't like Boma. We've eaten there twice and it was just ok, nothing special, but people seem to love it.
(4 reacties met lagere score weggelaten)

=== THREAD 78sbip ===
SUBREDDIT: r/CampingandHiking
DATUM: 2017-10-26  SCORE: 3  REACTIES: 0
TITEL: [Trip Report] Olympic NP - North Fork trailhead to Hoh Rainforest trailhead via Whiskey Bend
POST (source_id=post):
Total Miles: 95
Total Elevation Change: 24,000 ft
Location: Olympic National Park


Gear: https://www.trailpost.com/packs/373


Photos: https://imgur.com/a/3htPx


Route: North Fork trailhead to Hoh Rainforest trailhead via Whiskey Bend. 


Day 1: (2 Miles) Driving and Wolf Bar

Day 2: (21.9 Miles) Wilder Camp

Day 3: (16.6 Miles) Dodger Point

Day 4: (16 Miles) Altair

Day 5: (14.1 Miles) Appleton Pass

Day 6: (10.2 Miles) Hoh Lake

Day 7: (14.2 Miles) Finished


Food:

Total Weight Per Person (lb): 11.50 (includes fuel)

Weight Per day (lb): 1.44

Calories Per Person Per Day: 2604

Cal/Oz: 113


Details about food:
https://docs.google.com/spreadsheets/d/1kncDa1Uw_mgNOna36jG9JnfB7zB2F6v1wX-1h0jQcvc/edit?usp=sharing


Comments on food: 

The Probars are an awesome staple, highly recommended, although a little bit expensive. 
The beans and rice with fritos and cheese is my new all time favorite backpacking meal. I was nervous the cheese would go bad, but that wasn't a problem. 
Pita Pepperoni pizza sounds sounds and looks unappitizing, but it is surprisingly good. 
A lot of M&M's and candy are also recommended. 
I would probably nix the Thai Peanut Noodles, they were decent, but not good enough. 

The amount of food was good, I was never hungry.



Narrative (Skip to the bottom for thoughts on gear):


Day 1: We had to drive from Seattle to the Hoh Rainforest trailhead to drop off a car. We picked up our permits at the wilderness center there, and added on an extra day so we had a place to sleep that night, and so we could knock a couple miles off the trip. Driving from Seattle to Hoh Rainforest trailhead took about four and half hours. We then took our second car to the North Fork trailhead, which took about another hour and a half. 


We took a quick hike through the Hall of Mosses, but I wouldn't recommend it for anyone who is doing a backcountry hike. It was really similar to what all the trails looked like below 3000 ft. In nearly the entire park it is rainforest under 3000 ft, and alpine above. 


Hiking to Wolf Bar was quick and easy, and we made it just a little before nightfall. 



Day 2: The relatively long miles meant we pretty much had to keep our heads down and hike with only a few breaks. There was very little elevation gain, so it was a good starting day until we got our trail legs under us. 


There were a few river fords, which slowed us down. Some of the creeks washed out the trail, which resulted in us wandering around for about an hour at one point, trying to find the trail. 


The campsite had a nice little two person hut, which was welcome at the end of a long day. 



Day 3: Doing the extra 2 miles to Wolf Bar the first night made this day way more manageable. The first ten miles of the day were flat. At this point we had to ford the Elwah river, which was the largest ford of the trip. It was cold, but not overly technical. Unfortunately my foot slipped on a slick rock and my second biggest toe on my right foot got pretty dislocated (and possibly fractured). 


Thankfully the water was cold, so I barely felt it. I popped it back into place and finished crossing without issue. We spent some time discussing what to do next, and decided to push on to Dodger Point that night and see how the toe was fairing the next day. We figured it was about 20 miles out either way, and if we went to Dodger Point, the next day would be all down hill. Also, most injuries are worse after the first day, so we would do the hard uphill while it was still relatively painless.


The trail from this point was considered to be a “primitive trail”. The ranger assured us that it just had a few more fallen trees and was a bit narrower, but there were parts that felt like bush whacking, and we lost the trail more than once. There was about 6 miles to the top with 4,000 ft of elevation gain. Also, there was no water for about 12 miles of the trail. 


Once we reached the maintained trail near the top we were exhausted, but the views were pretty spectacular, and my toe felt relatively good. We had the option to turn up to Dodger Point and hike another half mile and 500 ft of elevation, but we decided to drop our stuff on at the campsite and take a break before heading up to the point. The campsite ended up being deceptively far down the trail, so we opted not to turn back. I wish we could have seen actual dodger point, but with the toe and all it felt like an acceptable sacrifice. 



Day 4: It was freezing cold overnight (probably near 30 degrees which is torture for a Texan). My toe looked pretty bruised, but felt well enough to walk. I had to limp a bit and I could barely bend the toe, but the pain was manageable. 


We got down to Humes Ranch, and decided we could continue hiking to Altair to cut some miles off the next day. We passed by the Goblin Gates, which is a pretty cool rock formation carved out by the river. 


We got to Altair campsite, and were trying to figure out how to get a reservation, but it turned out that the campsite had been converted to a day picnic area and had no overnight camping. We couldn't make it to the next camp before nightfall, so we just found a secluded clearing and quietly stayed the night. 



Day 5: the toe was stiffer and more painful than the day before, but I decided that it was still manageable. I had to limp pretty heavily, but we were still able to make our mileage as long as we hiked most of the day. We ran into some guys drinking beer next to the road. One of the guys told us to “have a great fucking day” as we walked off, which raised our spirits. 


Again, another high elevation gain day. The final ascent to Appleton pass was pretty steep, with little tree cover, it felt a bit like the passes of the Sierra’s. Nothing very notable happened except running into a pack of deer in our campsite who were completely unafraid of humans. Again, the views grew increasingly stellar as we got up high and the trees thinned out. 



Day 6: We started the morning losing about two thousand feet, then gaining three thousand right after. We then got into the seven lakes basin loop, which is heavily traveled and has quotas on most of the campsites. This is where we started running into your normal weekend warrior types, lots of people carrying sixty pound packs.


After passing Heart Lake we saw our first bear of the day. We then got up on the High Divide Ridge which provided the best views of the entire trip. On one side was Mt. Olympus, and on the other side the seven lakes basin. You hike along this ridge for about 7 miles, with great views the whole way. We saw our second bear in a small lake below playing like a dog. 


We then descended into the Hoh Lake basin. The campsite was the only quota site we stayed at, and we were one of four other groups. This was the first night we had to camp next to anyone. 


Next to the lake was another six bears (3 mom and cub pairs). We were a bit intimidated by the close proximity and shear number of bears, but we followed our boy scout bear prevention techniques and had no issues. 



Day 7: The last day was entirely downhill. We had the option to extend the trip by one more day and hike up to Glacier Meadows by Mt. Olympus, but we opted to just hike out. My toe was still very stiff and painful and I had kicked a few rocks by mistake, so I was ready to get a milkshake and rest my foot. After some seemingly endless switchbacks we were back in the Shire-esque rainforest. The hike was filled with increasing people slowly introducing us back to society. 



Gear Review:


Pack: Gossamer Gear Kumo. The pack was pretty good, but a tiny bit small for a week of food and our gear. Once I upgrade my tent it should be fine volume wise. I like the roll top, and the back pocket. The removable hip belts slowly loosened, which required me to stop and take off the pack to tighten them once or twice a day, which was a bit annoying. The shoulder straps are my biggest real complaint, they are pretty stiff and uncomfortable above 20 lbs. I made my own GG G4 last year and all I did was cut and sew some thermarest foam into the shoulder straps and it was comfortable up to 30 lbs. By the halfway point in the trip my pack was very comfortable, but the first part left my shoulders a bit sore. Grade: B+ good pack, uncomfortable shoulder straps, finnicky hip belt. 


Tent: We used a Big Agnes Copper Spur UL2 with glow light. The tent is relatively heavy and bulky, but the double doors were nice and the glow light was kind of fun, although very bright. The space was adequate, but a bit cramped, camping with my brother made this a non issue. Grade: B-, nice features, too heavy. 


Sleeping Pad: therm a rest xlite. Light, thick, warm and comfortable. The pad is a bit narrow, and relatively loud, but not too bad. I used an Exped UL pillow, which is a bit too thick for back sleeping, but perfect for side sleeping. Grade: A- light, warm, and comfortable, too narrow


Quilt: my MYOG quilt using Argon 67 and 950 fp down. It is thick enough for about 30 degrees, but we pushed right up against that limit, and I just finished acclimating to 100 degree days over the summer, so I was a bit cold. I wore some lightweight long underwear, and stole my brothers long underwear and wore my down jacket, and was just borderline comfortable. The quilt is super light and relatively warm, but on this trip I probably needed a little thicker long underwear. Grade: A, light and comfortable, really closer to a 35-40 degree bag. 


Other gear:  I used a BV450 and my brother used a BV500. This was exactly the right size for a week. I carried the tent to make up for the smaller can. I used a Bearikade Expedition last year, which was about the same weight, but twice the size. Obviously the Bearikade was nicer, but I was able to sell it, and buy this canister, and a Ursack and still have money left over. 


My Nitecore Thumb was perfect, but it annoyingly flickers when you change the angle. It also shines in your eyes if you pin it to your shirt, a small piece of tape helped that. 


I didn't like using a plastic liner in my pack, it was a pain having a bag in a bag. It didn't rain, so I am being a bit unfair, but I am a plastic liner hater. 


I used a Nitecore F1 charger with two allegedly 5,000 mAh batteries. That was more than enough for my brother and I to keep my S8 and his Nexus 6P charged for all of our pictures, some games, and some music. 


My MYOG gravity filter had some pros and cons, it was better sometimes and worse others. I made it out of a sawyer bag, a hose, and a camelback valve glued into a smart water bottle cap. I ran a tiny vent line up from the bottle to the bag to allow the air to vent, but to prevent water from overflowing if the bag had more water than the bottle could hold. I liked that I was able to use it with a hard water bottle, and that it had a valve, but it was finicky and got tangled easily since I had to spin the cap to get it on the bottle. I think some quick connects would make it significantly more useable. I want to try a Befree as a squeeze filter as well. 


CMT trekking poles are awesome. 


No rain, so no comment on the Houdini and Snow Peak umbrella. 


Altra Lone Peak 3.0s were so comfortable, I probably couldn't have made it with the messed up toe with my previous invo8 Roclite 295s. The only thing I would like improved is breathability. Grade: A 


I lost my buff, but was nice the first two nights. 


The Uniqlo down jacket is great value, but it isn’t quite warm enough for trips like this or the JMT trip that I did last year. I found myself a little bit cold, and since I use it along with my quilt, it would help boost my quilt rating to have a warmer one. I am thinking of getting a Ghost Whisperer or a Montbell jacket. 


Clothing: All good, I didn’t make any changes from this year to last besides swapping the rain jacket. 


Stove: I used the Zelph StarLyte at the recommendation of Andrew Skurka. This was my first attempt at using an alcohol stove, and I loved it. It was simple and light, the fuel was cheap, and since the StarLyte can hold up to an ounce of fuel, I was able to just blow it out when my meal was done and cap it, so I didn’t really have to worry about measuring perfectly. I made my own caldera cone which worked out surprisingly well considering how easy it was to make. My Titanium pot is a bit too short to fit the rolled caldera cone though, and it is “non-stick” lined, which isn’t necessary. I will probably replace it with a taller pot at some point. 


Phone: The galaxy S8 worked out well. It has a nice camera, and excellent battery life with the low power settings being really aggressive. It is water resistant, which saved my phone when I mistakenly left it in my pocket during a waist deep creek crossing. The photos tended to have a bit of solar glare on them, which was a bit annoying.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

