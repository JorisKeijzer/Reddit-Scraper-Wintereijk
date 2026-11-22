# Label-batch batch_0111

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
Schrijf het resultaat naar `batch_0111.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 8b48ra, 5bd27a, 66bqyx).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 8b48ra ===
SUBREDDIT: r/weddingplanning
DATUM: 2018-04-10  SCORE: 95  REACTIES: 56
TITEL: Recap: Our Downtown Winter Wedding!
POST (source_id=post):
Hey you guyssss! We did it! 

I didn’t post a lot, but this subreddit was my life raft and voice of sanity during the planning process. I got some of my best ideas from other recaps, so it’s only fair to return the favour! 

First of all, [PHOTOS!](https://imgur.com/a/DJwTT)

Okay, here we go: 


**Venue - $4228**

Our venue was a little industrial loft in the east end of Toronto. We got $1000 off because March is a slow season, but quickly spent it again to rent their recovered wood bar, get our SOP (liquor event licence), event insurance, and rent chairs. The venue was very bring-it-all yourself. We had a venue coordinator to help coordinate, but all catering, booze, decor, rentals, music, etc. had to come from outside. 

They were undergoing renovations when we booked to expand their catering kitchen and add washrooms. Sadly, the washrooms weren’t finished by the time we got married, so we received a partial refund (yay!) and access to the super cool service elevator/ coffee shop downstairs to be able to access their washrooms (double yay!). The coffee shop was closed within an hour of our wedding starting, so we were able to use it as spill over for quiet conversation all night long. 

We had access to the venue at noon before our 4pm start time, and were able to come back the next day to pickup excess decor and booze.


**Decor - $1244**

This includes our tables (plastic, rectangular), table linens (burlap), and the lace runners. I so, so wanted wooden farm tables but couldn’t swallow the extra $900, so plastic it was! This also included our DIY tassel garlands (made by my husband - eeeep, still getting used to that word!), paper fans, supplies for our memory table, the key and tags (acting as our escort cards), jam jars and ingredients (used as both favours and place cards), our table names signs (each one named for one of the streets we lived on throughout the course of our relationship), confetti, confetti bags, stickers and our cake topper.

We did VERY little DIY, and went the Etsy route a lot of the time! We made the jam ourselves over the course of an afternoon, stuffed the confetti in bags, stuck stickers to things, and assembled the tassel garlands. The guys showed up at the venue 2 hours before the start time to set it all up. My job was just show up, know my lines, and look pretty! Loved it! 


**Photographer - $1700**

That got us a second shooter and 6 hours of services. We were also able to barter for an extra hour for a total of 7 hours because my photographer had never shot at our venue before and wanted to add it to her portfolio. Woohoo! We LOVED [Stacy Kenopic](https://www.stacykenopicphotography.org/) and her work, as evidenced by our lovely photos above. She was also HELLA fast. We got our pictures back in two and a half weeks! 


**Flowers - $1779**

Done by Coriander Girl. They did our bouquets, boutonnieres, fresh garlands for the tables and arch, and the copper arch rental.

A word of caution and funny story: when the florists dropped everything off they recommended refrigerating the boutonnieres, and we forgot them in the fridge! One of the bartenders found them an hour into the dancing and brought them out. Hilarious! 


**Alcohol - $1442**

This is totally an unrealistic price for what we got. I have a friend who works at a local winery so we got 6 cases of each: Cab Sauv, Merlot, Rose, Sparkling White, and Pinot Grigio for $550. Completely ludicrous but so great for us! The rest was spent on beer from a local brewery called Left Field. We got a pilsner, a brown ale, and a sour saison. So. Yum.


**Catering - $5036**

Our largest cost, but it was so worth it. We used one of the venue’s preferred caterers, Cherry St. BBQ, which I would totally recommend. They knew the venue inside out, and we got rave reviews on the food. We didn’t get any photos, but here’s an [instagram pic](https://www.instagram.com/p/BY1e4pll7Dw/?taken-by=ammmiem) from our tasting. We had brisket, chicken, sausage, quinoa salad, coleslaw and mac and cheese. 


**Cheese - $500**

Yes, we spent $500 on cheese and proud of it! Although when you compare the costs to a wedding cake, it’s really not that bad. I’m not big on icing, and my husband used to work at a cheese shop in high school (Alex Farms on Bayview - where our wedding cheese was also sourced and so we got a little alumni discount), so this was a natural fit. We did get a tray of distraction sweets for anyone who needed a sugar hit later (cookies, bars. brownies, etc), and didn’t hear a single complaint about the lack of a “proper wedding cake”.

We chopped it up right after the ceremony to serve as our cocktail hour snack while we snuck out for photos. 


**Dress - $1100 (base) + $450 (alternations)**

Big ups to my mom and stepdad for paying for this as a surprise for me! It’s Maggie Sottero Patience with straps added for extra support. As you might be able to tell, it wasn’t quite enough support and I was still hoisting it up all night. I still felt and looked great, but it was a bit of an inconvenience. Thank goodness for bouquets and my stole to help keep things covered up in the family photos!

Bought it at Becker's on Danforth. It was the second place I shopped, and I knew that I'd overthink it if I kept looking so I stopped. 
 

**Suit - $1600**

A custom made number from Surmesur in Toronto. It’s very, very dark green and husband LOVED it. And he gets to wear it more than once! He also got his vest, shirt, and tie from them.


**Save the Dates - $20**

Electronic from Paperless Post. We started planning in September for our March wedding, so we just wanted to get the word out fast.
 

**Invites - $250 (Minted invites) + $130 (stamps)**

Cost of stamps also includes enough stamps for our thank you cards. Got a two-sided, single card invite and did all of our RSVPs through theknot.com. Our wedding website is [scottandammie.com](http://www.scottandammie.com/) if anyone wants to check it out, we worked really hard on it! 


**Calligrapher - $100**

She did all of our chalkboards. Bless people with good handwriting. Bless delegation.


**Wedding Bands - $1830**

Mine definitely represented the most of this cost. We went back to the same jeweller (Denis Fairhead) that did my custom engagement ring so they would fit perfectly together. Husband’s ring is birdseye maple from Made You Look on Queen St. 


**Officiant - $350**

Mary Beaty, a humanist minister. We’re both atheists and she allowed us to really customize our ceremony to suit of personalities. Our readings were [A Tuesday Kind of Love](https://thoughtcatalog.com/stephanie-georgopulos/2012/05/i-want-a-tuesday-kind-of-love/), and [this passage](https://www.goodreads.com/quotes/447369-i-will-love-you-as-a-drawer-loves-a-secret) from Lemony Snicket’s The Beatrice Letters. Each read by one of our siblings. 

**Traditions that we tweaked:**
- Our cheesy wedding cake
- Both my mom and dad walked me down the aisle, with my stepdad and stepmom walking down arm-in-arm just before us
- No parent dances or tossing of things
- No showers (though we did have an engagement party) 
- No flower girls/ ring bearers


**Notes that didn’t fit anywhere else:**

* We were definitely only able to pull this off with the financial help of our parents. We worked with them to split the cost four ways between us and our three sets of parents. 

* Don’t trust your bald stepfather when he insists that he wants to hire his hair dresser to do everyone’s hair. He offered to pay for myself, family, and my bridesmaids so it was hard to say no, but our hair was originally straight out of the 80s. One of my amazing bridesmaids set up a “speakeasy salon” in the basement to fix everyone’s hair to the point where you see it in the photos. So thankful to have had her! 

* We had some no-shows and some rude guests but at the end of the day it really didn’t matter, and we barely noticed. Any unruly guests were largely handed by our wedding party who insulated us from any of the drama. We were so lucky to have such a great wedding party, and now we can laugh about the bad guests (who admittedly were few and far between) in retrospect rather than problem solving in the moment. 

* Definitely take some time to pause and look around to appreciate the unique permutation of people that you’ve brought together. The only thing they all have in common is you! How cool is that?! 

* Nobody can tell what things cost. I got SO many compliments on my $25 amazon veil, you wouldn’t believe! If you invest in some solid foundational pieces, nobody can spot the dollar bin items scattered throughout. Another great example of this was our plastic folding tables.

* Conceded where you have to, but only to things that don’t really matter to you. At the end of the day we had the wedding we wanted, on the terms we wanted, in a way that suited us perfectly! 

* Wedding stress anxiety are real, sleeplessness is real. My way through was wine and melatonin. Ain’t no shame in finding a way that works for you that might be a little…less than healthy.

* If you can afford it, honeymoon right away is flipping awesome. At least take a couple of days off before going back to work. I think we would have gone nuts if we'd gone straight back. We did the Disney World thing which was SO FUN and I could write another recap on that alone!  


And one last note, because it feels important. *I was 241 lbs* when we got married. And I felt beautiful, and loved, and cherished and worthy. And I was SO worried that I wasn’t going to. Confidence is something that I’ve been working on for a number of years, but something about being a “fat bride” had me shaking in my boots. And a big part of getting over it was seeing so many gorgeous women on here rocking their shit on their wedding day. So thank you for that, and I hope that I’ve returned the favour! 

Holy crap that was long! 

TL;DR: Got married, had a fucking blast, wouldn’t trade it for the world, wouldn’t want to do it again! <3

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dx3uzym] (score 9, diepte 0) Girl your waist is something dreams are made of! You look amazing and so happy! Absolutely beautiful photos!
[dx3xbg7] (score 8, diepte 0) Superb writeup and congratulations!

I chuckled out loud at the part about the hairdresser. Sage advice, my friend, sage advice.
[dx3v8p9] (score 6, diepte 0) Everything looks amazing and you looked gorgeous. Congratulations! How many guests did you plan for?
[dx3vg0i] (score 6, diepte 1 OP) Yes! Forgot to add that! We budgeted for 80-90 guests and invited 106. Our final number was 89. [Here are some stats](https://imgur.com/a/J9o0i) I kept along the way! It's a week-by-week RSVP breakdown.
[dx3v5zn] (score 5, diepte 1 OP) Thank you! It really was the best day. And let me just say that corsets are the fucking bomb!
[dx41uz2] (score 5, diepte 0) Thank you for sharing your pictures, what a beautiful day! Fellow fat bride here—I went wedding dress shopping this past weekend and was terrified to expose my fat arms in public but my favorite dress is completely strapless and I think I’m gonna take the plunge and go for it! Seeing other brides who look like me on this subreddit make me feel like I am worthy of feeling bridal and I cannot thank y’all enough for how much your posts and your confidence are boosting me up!!!
[dx3zjo9] (score 3, diepte 2) Yes! It’s just good storytelling. But seriously, I wouldn’t have guessed you guys had any trouble with the hair stylist.  Your bridesmaid did great! :)
[dx3xzt7] (score 3, diepte 1 OP) Not to my knowledge! We had a couple flaky friends that we had to badger to RSVP, but not because they hadn't seen the back - they just lost the invite. Although I imagine those people are going to find a way to get it wrong no matter how thorough you are or how prominent the information is. 

The best part about the website was being able to send the flaky/ forgetful people the url, and saying "go here and click the RSVP button, that's all you have to do". Even did it with a couple of friends on their phones while we were at a bar one night! RSVP'd right in front of me.
[dx3wjwg] (score 2, diepte 1 OP) They are fantastic! I don't know much about flowers, so we just gave them a general colour palette to play with and said go! 

Only note with the arch: be sure to arrange for return of the rental. We totally forgot and had to have my mom throw them an extra $50 on the second day of our honeymoon as a pickup fee. It was totally our fault though, they were nothing less than spectacular!
[dx3x1ae] (score 2, diepte 0) Yay! It looks like a blast! Thanks for taking the time to write a recap, I really appreciate these!
[dx3xupv] (score 2, diepte 1 OP) Oh. My. God. He was truly the worst part of our prep, but every wedding needs a thing like that to turn into a good story!
[dx5utvq] (score 2, diepte 1 OP) I feel you on the fat arms thing! It was my biggest foible to get over. I had to keep reminding myself that this was the body that my husband loved me in and was marrying me in, and that's all that really mattered. Go rock that strapless! <3
[dx956sy] (score 2, diepte 2) I NEEDED to read this right now. It's like kismet. I just got done with my first dress fitting and the only thing I can see in pictures are my big fat arms. 

BUT this subreddit makes it obvious that brides, as a rule, a gorgeous. It's magic. Thanks for the reminder and congrats on a beautiful wedding.
[dx43mpg] (score 2, diepte 0) Looks beautiful! Do you mind sharing the link to your veil?
[dx4fvwh] (score 2, diepte 1 OP) For sure! It's right [here](https://www.amazon.ca/gp/product/B01LYK4PEH/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1).
[dx4g0mh] (score 2, diepte 1 OP) YES! That is exactly why it was so important for me to share that thought at the end. Ride the hope and know that as long as you feel confident, it'll beam out of you in the most incredible, beautiful way!
[dx4mvg2] (score 2, diepte 2) I am pretty sure it's this one! http://www.davidsbridal.com/Product_twist-bodice-chiffon-dress-with-beaded-belt-w11147_all-bridesmaid-dresses

(P.S. I work at David's Bridal and if you come in and describe the dress to us we'll be able to find it: I can only guarantee this for bridesmaids dresses.).
[dx4hifg] (score 2, diepte 1 OP) They were so, so easy to coordinate with! Jay (the event manager there) even helped broker our furniture rentals, and had no problem serving other food not prepared by them (our cheese cake and sweets). If you're considering them, I would highly recommend making an appointment for a consult. They comped us that entire platter of food and two rounds of beer. We could hardly walk out! 

I don't know about temperature, but I think if I remember their process correctly, it's all smoked for the same amount of time as their restaurant food, stored, and then reheated on site. I hope that helps!
[dx5u2o4] (score 2, diepte 2 OP) All good! Someone also sourced the dresses above, but here's the link again: http://www.davidsbridal.com/Product_twist-bodice-chiffon-dress-with-beaded-belt-w11147_all-bridesmaid-dresses
[dx5u7sf] (score 2, diepte 1 OP) Thank you so much! We're still obsessed with the cheese cake! I'm actually munching on some of the leftover piave with leftover cab sauv right now. :)
[dx5uabv] (score 2, diepte 1 OP) Thanks! I actually didn't mention it because it was a bit trickier to replicate. I got it from a local Toronto Wedding Bunz group. Traded a $75 dollar liquor store gift card to rent it for the month!
[dx5ufou] (score 2, diepte 1 OP) 1. Thank you so much! 
2. I'm not sure, but if you go back to at least 2016 and hang out at the Starbucks at Yonge and Eglinton we should eventually bump into each other and become besties!
[dx5svg6] (score 2, diepte 0) 1. You are beautiful!!!
2. This looks like an amazing day--so many good details! Great photos too.
3. I love that your stepdad and stepmom walked down together. That's so sweet.
4. Omg...the hairdresser!!!!! That must have been mortifying, but at least it's a good story now. Your stepdad owes you!
5. Would you mind sharing the link for your Amazon veil?
6. Thanks so much sharing your wonderful wedding, and in such a well done recap!!
[dydw6wm] (score 2, diepte 0) I am very late to this game, but I'm also getting married at the Jam Factory and I really appreciate your breakdown. Your wedding (and you!) looked gorgeous! Congrats!
[dx3vxcr] (score 1, diepte 0) Corriandor girl is also doing my flowers. We debating getting an arch from them and after seeing yours I'm sold. You're wedding looks stunning, love the vibe!
[dx3w4td] (score 1, diepte 0) Damn you guys are sooooo cute!

Your photos are amazing, so much love. Love your style, and your bridesmaids too! This is all so lovely!
[dx3wnld] (score 1, diepte 1 OP) We felt so cute! We put a lot of work into feeling like our cutest selves, and wanted our wedding party to feel great too. Glad it showed through!
[dx3xt2e] (score 1, diepte 1 OP) They saved me when I was planning, so I was happy to write one up in return!
[dx3xnm7] (score 1, diepte 0) I’m thinking about putting our website/rsvp info on the back of our invite— did any of your guests not see it? That’s what I’m most worried about.
[dx3z6oj] (score 1, diepte 0) Oh wow! We seriously considered the Jam Factory as our venue for our winter wedding too!! It's so neat to see how you guys made the space yours, I love it!!

We ended up doing the whole thing in Ottawa instead of TO, but... any chance you can send me the deets for your calligrapher?? Haha
[dx3zwly] (score 1, diepte 1 OP) Of course! I don't know if she'll travel (she did all the work on site), but she's [Viktoriya Mykytyak](https://www.instagram.com/velvetcalligraphy/). We loved her style!
[dx4m0eb] (score 1, diepte 2) Sweet, thanks!! I could likely travel to her, if I can get things done in advance - My family all live in Toronto so I'm there all the time! 😊

Also, you look absolutely radiant in all of those photos - congratulations!!!
[dx9vcgw] (score 1, diepte 3 OP) YES! It is the most wonderful kind of magic, but it's true and it will work for you too! You. Will. Be. And. Are. Gorgeous.

Also, let me just say that fitting photos are the WORST, especially if your mom or another loved one is taking the photo. Some of the worst pictures I've ever seen of myself are one's my mom took at my fittings. My theory is that they see you through such a lens of love that they can't imagine such thing as a bad photo of you. All photos of you, to them, is a beautiful photo. So they're not wary of your pressure points, and your lowest self-esteem bits in the same way that you, or the professional photographer you'll hire for your wedding will!
[dx45jab] (score 1, diepte 0) Honestly I've been pretty worried about my weight as the months creep up on me but you look so amazing and HAPPY in these pictures it gives me hope that no matter what everything will be okay! :)
[dx48j63] (score 1, diepte 0) A couple of things. 1) Everything is stunning. I’m 5’9” and 217 lbs. I feel like a damn whale on a daily basis. You look incredible. This gives me hope that I won’t look like a baby beluga on my wedding day. That is a gift that is absolutely priceless. Thank you.      
2) Your fur shawl is amazing. Your bridesmaids are gorgeous. Do you mind if I ask where you got their dresses? I want my girls in emerald, as well.       
3) Your wedding is amazing. Goals. Incredible. Thank you for sharing with us!
[dx4fyai] (score 1, diepte 1 OP) 1) Thank you! And I'm sure as long as you're happy, you will look absolutely gorgeous! 

2) I can't remember the name of the style, but this is the colour Juniper from David's Bridal.

3) THANK YOU!
[dx5tzj1] (score 1, diepte 3 OP) That's totally it! Thanks for tracking it down.
(19 reacties met lagere score weggelaten)

=== THREAD 5bd27a ===
SUBREDDIT: r/weddingplanning
DATUM: 2016-11-06  SCORE: 35  REACTIES: 43
TITEL: 6/17/16 - New Orleans French Quarter wedding recap
POST (source_id=post):
This post has been a long time in the making!

It was overwhelming to get started recapping the happiest day of my life and I didn't know quite where to start!

First things first, [here's the album](http://imgur.com/a/OEg6y) if you want to skip my novel!

[Here's our cost breakdown](https://docs.google.com/spreadsheets/d/1FUwWesSbCXrVj2Kc2rwM8jg_iQ7VVBlCX5DtpY7rK4k/edit?usp=sharing) for the wedding and honeymoon.

We were luck enough to have our honeymoon gifted to us by my in-laws. They gave us a week of their time share that we could then exchange in the timeshare's exchange market. We picked Lanzarote, a Spanish owned canary island with lots of unique history that I never would have heard of otherwise!

We were also gone from May 28 - July 7. I flew home the weekend of May 28 to attend a friend's wedding in my hometown and hung out for a week with friends and family who couldn't attend our wedding two weeks later. We then left and attended Bonnaroo where I rang in my 29th birthday. After Roo we flew to New Orleans for our wedding. The next weekend we traveled to Alabama to spend a week at my friend's (and bridesmaid!) parent's lake house to decompress from all those shenanigans. We then flew to Lanzarote and on the way home to Salt Lake City we spent three days in Dublin. It was quite a trip and I loved every second of it!

On to the wedding recap:

We landed in New Orleans on the Tuesday before our Friday wedding. We stayed in an AirBnB on Bourbon St. directly across from our venue to handle final prep with the venue and a few last minute things. The morning of our wedding we checked into the [beautiful, historic French Market Inn](http://i.imgur.com/JgBoLt1.jpg).

I scheduled hair and makeup in the early afternoon and they arrived a few minutes before my photographer. I want to take a second here to say one thing:

THE BOMBASS TOO EXPENSIVE PHOTOGRAPHER IS **ALWAYS** WORTH IT.

We were lucky enough to have our honeymoon trip paid for, so the "too expensive" photographer was suddenly in our price range and she was worth every single penny. Because of a happy accident, the secondary photographer's wife going into labor the morning of my wedding, we ended up with two principle shooters! The owner of the company and her good friend who also owns her own photography company stepped in at the last second. Needless to say, all of our pictures are amazing.

Anyway, here's a shoot of my [dress](http://i.imgur.com/KeWFMPL.jpg), [shoes](http://i.imgur.com/2LjgywL.jpg), [accessories](http://i.imgur.com/sehqYBY.jpg), [program](http://i.imgur.com/Ds5olLR.jpg), [wedding jewelry](http://i.imgur.com/9xrOLuk.jpg), and [second line handkerchiefs](http://i.imgur.com/PjKL5fQ.jpg).

Here are the favors my bridesmaids received: I made them each [charm bracelets](http://i.imgur.com/sjuCPi3.jpg) with personalized charms and wrote them a card explaining why I picked those charms for them specifically. And of course, [flasks](http://i.imgur.com/crYAm6Q.jpg). I also made [each of their bouquets](http://i.imgur.com/dxj8L8k.jpg) with paper flowers and brooches.

After my makeup was done I was emotion bombed when my bridesmaids presented me with a letter he wrote me. [I laughed](http://i.imgur.com/rjsoWgR.jpg), [I cried](http://i.imgur.com/dozxTUO.jpg), I had to have my [make up touched up](http://i.imgur.com/jVQcmGF.jpg).

I decided to share some pics with you ladies that I enjoyed, but didn't make it to facebook. Getting your dress on is... not exactly glamorous. I had to [cover my face with a towel](http://i.imgur.com/RMwXrb9.jpg) to keep my makeup from staining it! But after all the awkward, [I felt like a princess](http://i.imgur.com/qk79hte.jpg).

We decided to do a first look and bridal party photos before the wedding since our ceremony would immediately be preceded by the second line parade and we didn't want to waste any of that time. My photographer was amazing and actually recommended this hotel to us for that reason. It's a block from Jackson Square, our ceremony site, and also she was aware of the grounds and new the perfect spot for [our first look](http://i.imgur.com/q8Vfu4p.jpg). [Another emotion bomb](http://i.imgur.com/fW4RhBs.jpg)!

The first look was amazing. All of our bridal party and parents were there and everyone was in tears. [Approach](http://i.imgur.com/k1VgmJa.jpg), [tap](http://i.imgur.com/b1FkvHs.jpg), [look](http://i.imgur.com/9TuodmH.jpg)! [His face](http://i.imgur.com/bK1516a.jpg) was priceless.

My dress had a cape and I enjoyed flapping it like batman. The photographer [caught me doing that](http://i.imgur.com/rImkdlX.jpg) a lot throughout the day actually! We took a few photos with [the bridal party](http://i.imgur.com/ogML9qM.jpg), I had a [mini-bridal shoot](http://i.imgur.com/15yfj2p.jpg), and a [few posed photos](http://i.imgur.com/Jf8tM4Y.jpg). I also took a break to [drink some wine](http://i.imgur.com/Frt3F32.jpg), ok... a lot of wine, and then we headed off to the ceremony.

This is my favorite photos from the hotel, it's very ["Cinderella lost her shoe"](http://i.imgur.com/y6e2XI3.jpg). And then very ["Cinderella found her prince"](http://i.imgur.com/xoc7IHj.jpg).

My dad, for various reasons, wasn't invited to the wedding. I knew 100% I had picked the right man to marry when, as I was fretting about who would walk me down the aisle, he said, "[I don't see why we can't enter together](http://i.imgur.com/argcBGx.jpg). No one is giving you to me, it's a celebration of us starting our life together." Cue lots of tears and [we made it so](http://i.imgur.com/qQ2kfo3.jpg).

[We were married in Jackson Square](http://i.imgur.com/oRnNl9q.jpg), it's literally everyone Louisiana girl's dream. The lucky Catholic ones can actually get married **inside** the cathedral, but we're heathens and had to settle with it as just a fancy backdrop ;)

We exchanged vows and his were very sweet. He also [cheated and whipped out his phone](http://i.imgur.com/YqHXMp5.jpg), I have no idea why I didn't think of that! Mine were very short and to the point, as I A. didn't write any and B. knew I would just start sobbing.

We sealed the deal in about 15 minutes. Although it was almost 6PM it was still 90 degrees and a zillion percent humidity. Everyone was hot. Everyone was sweaty. So [we kissed](http://i.imgur.com/sGuFzs4.jpg), [celebrated](http://i.imgur.com/I42e8Dc.jpg), [took a break](http://i.imgur.com/SqXrCuu.jpg), [snapped](http://i.imgur.com/xFZNdyC.jpg) a few [classic pics](http://i.imgur.com/ksYods7.jpg), ok [more than a few](http://i.imgur.com/dcGOx60.jpg), and then the [secondline parade began](http://i.imgur.com/o7Gzloy.jpg)!

For those unfamiliar with a secondline, it's a tradition in New Orleans that originated with funerals in black communities when white funeral homes wouldn't pick up their deceased. The band would play as the community carried the body through the streets and play funeral dirges. (As much as you can play a dirge on brass instruments). Eventually this transitioned to black communities creating their own social clubs and aid societies and secondlines began playing newly married couples throughout the streets. Most neighborhoods in New Orleans have secondline bands that fall together and play for every happy occasion in the community as well as official social clubs.

This was one of my favorite parts of the wedding because I didn't tell anyone not familiar with the tradition about it. On each chair at the ceremony there was a program and a monogrammed handkerchief and they just assumed the handkerchief was a favor. In reality, everyone waves them as they parade with the bride and groom. We had a blast and it was as  fun as [my face is letting on](http://i.imgur.com/ys8UiIg.jpg). We had a police escort headed by two motorcycle cops and in the rear a patrol car. Everyone stopped, took photos, congratulated us, handed us trinkets, cash, etc. [The band played](http://i.imgur.com/xMREFVl.jpg) [and the cape flowed](http://i.imgur.com/PiQcrx2.jpg), of course.

A pit stop during our second line was to [Attiki Bar & Grill](http://i.imgur.com/3244gE0.jpg). The first time I took my husband home to visit with me I took him to Attiki, as it's one of my [favorite places on earth](http://i.imgur.com/tOuAp2A.jpg). We arranged with them to accommodate us halfway through the parade so we could cool down and [have a drink](http://i.imgur.com/nR0QwX0.jpg) before arriving at the venue. We [snapped a pic](http://i.imgur.com/dbMKNIb.jpg) and then [headed out again to our venue](http://i.imgur.com/KyO47HC.jpg).

Our venue was [Bourbon Vieux](http://i.imgur.com/2t8wvS3.jpg). It's an amazing place on Bourbon Street that we were lucky enough to stumble upon by accident on a previous trip. The venue was AMAZING. We paid ~$9,000 for a dinner buffet and open bar for 150 people. The dinner had three proteins, stuffed fish, crawfish etoufee, and blackened chicken (for the guests scared of the food). The sides were salad, green beans, and something else I've forgotten with rolls and the soup was gumbo. The deserts provided was an assortment of petit fours and we also catered [a cupcake tower](http://i.imgur.com/tswOZHz.jpg) instead of a wedding cake. We were going to be traveling immediately after, so we had no way to store a wedding cake.

Included in the price we paid they [decorated to our specifications](http://i.imgur.com/70PQ0X9.jpg), including a lighting package in our blue and orange theme. We were also given access to 50 feet of the [corner balcony](http://i.imgur.com/QSQZa5B.jpg) right [above Bourbon Street](http://i.imgur.com/bTOxhG6.jpg).

They made our plates for us, so as our guests were going through the buffet line we were able to [stuff our faces](http://i.imgur.com/KuWbxVP.jpg) and not worry about anything. By the time everyone was done eating we went right into speeches. My [maid of honor/bestie reduced us to tears](http://i.imgur.com/ZoyYOcB.jpg) and then went right into [our first dance](http://i.imgur.com/zF9Krzm.jpg).

Holy, emotion bomb, Batman. [I did not expect to start sobbing](http://i.imgur.com/uvuldJZ.jpg). But, all of a sudden it became very real that I was married to my best friend. Speaking of, my other [bestie/bridesmaid sobbed](http://i.imgur.com/YZfs3Hi.jpg) waaaayyy more than I did the whole day. We kept poking fun of her and it was true, every pic of her she's crying her eyes out. It was very sweet!

For the rest of the night we danced the night away and the open bar definitely helped everyone have a great time. Here are some other photos that I didn't post to social media, but I love because they really show me in my natural state. [This was me when my friend/DJ played my favorite song](http://i.imgur.com/OOovjRN.jpg).

In Louisiana (and I think a lot of other places in the south) there is a tradition called the money dance. The bride and groom start dancing and then people butt it in for a chance to dance with either of them for money. We made ~$400 in our money dance!

When it became time to really get the party started, I changed into my reception dress and we ended the night with [a dance party with our closest friends](http://i.imgur.com/zZatxL4.jpg). I think by then the crowd had thinned down to about 75 people or so. Which was great because [at some point my dress kept falling down](http://i.imgur.com/uIqZtYl.jpg), but I didn't seem to care too much.

I'm not into the whole spectacle of throwing the bouquet or the garter. So, we did neither. I posed for a few photos with the garter and sat on the best man's (my new BIL!) lap for a pic, but that's it. It always wigs me out when people do that, especially when the groom makes a big spectacle about rooting around under the dress. Dunno why, but it rubs me as really icky.

[We made our exit](http://i.imgur.com/Hud2XvF.jpg), [took some final photos](http://i.imgur.com/atowvDP.jpg), and then stayed out til 7am on Bourbon Street with most of the bridal party and our friends.

Now, on to tips:

We were pretty bare bones about everything. The venue contacted me a lot about my preferences for things and I just told them whatever they thought would work best. I picked champagne colored table clothes and mercury candle centerpieces with blue and orange lights and literally nothing else. Most people in the business know what they're doing, so I left it to them.

The things I found most important were having a good time with my friends, getting fantastic photos, and feeling like a princess. NOLA is a great city for that because of the traditions like the secondline. Every time we were on the balcony above Bourbon people were cheering for us and tossing us beads or just saying congratulations. I don't usually thrust myself in the spotlight, but my wedding day made me feel like the most important person on the planet for just one day.

I also kept things parred down for the things you're "supposed to do". We're both developers, so we made [our wedding site](http://www.jamesandashton.com). For our guests seating charts we [wrote their names on postcards](http://i.imgur.com/CQDTdBP.jpg) we printed. At the table there was [a second postcard](http://i.imgur.com/vnJTLWg.jpg) we asked them to write their favorite memories on and either send back to us or drop in a box on their way out. We got about 60 of them back and that was a really nice thing to return from the honeymoon to. Printing both sets of cards was ~$20.

When shopping for flights I saved us about $3k total. I purposely mapped the routes we wanted and bought regional airline tickets even if it meant a 4 hour layover and switching terminals at the airports. Well worth having that $3k in our pockets!

We splurged on the things that meant a lot to us:

* Photography

* Party

* Memories

* Traveling for the honeymoon

And spent very little on things that didn't:

* Seating charts

* Decor

* Guest favors

* Cupcakes instead of a cake. 8 dozen cupcakes was like $300 including a delivery fee and deposit on the stand

We did heartfelt things for the bridal party:

**Bridesmaids**

* Custom charm bracelets with a note explaining why those charms were picked

* Flasks

* Silk robes

* Paper flower and brooches keepsake bouquets

**Groomsmen**

* Moscow mule copper cups

* Keychains with charms and a note explaining why that charm was picked

* Matching pocket squares

We had a few things go wrong, but at the end of the day, it didn't matter.

* I lost some weight in the two weeks between my last fitting and the wedding and my dress didn't fit as form fitting as I wanted it to, but you can't really tell all that much

* I may or may not have drank too much on Bourbon St and not made paper boutonnieres for the groomsmen.

* One of my bridesmaid was -super- hungover, but she made it through and was a champ!

* My mom hid the fact that my sister, who I hadn't spoken to for over a year and did not RSVP to the wedding, was coming as her +1. I found out when she tagged me on fb at the airport with the caption "Surprise bitch" 36 hours before my wedding.

* Said sister also brought her infant to the wedding even though I explicitly said NO KIDS and everyone else politely, without a fight abided by that rule. I didn't even know if the baby would be allowed in the venue and who brings a one year old to Bourbon Street?!

* I lost my passport on the very first flight out of SLC. I had to pay $200 for an emergency one. Luckily, our first stop was my hometown where I paid $13 for a birth certificate same day since I was born there. The New Orleans passport office printed me one in less than a day.

* I forgot flip flops to wear during the parade when we left the hotel and my AMAZING Maid of Honor gave me hers and did the whole parade in 6in stilettos. I'll never be able to repay her for that.

Anyway, that's it! The day was amazing! I'm happy to answer questions if anyone has any to ask :D

Edit to add vendors:

Photography: [Studio Tran](http://studiotran.com/james-ashton-new-orleans-french-quarter-wedding/)

Secondline Band: [Treme Brass Band](https://www.facebook.com/TremeBrassBand/)

Hotel: [French Market Inn](http://www.frenchmarketinn.com/)

Reception: [Bourbon Vieux](http://www.bourbonvieux.com/)

Hair & Make Up: [Glam NOLA LLC](https://www.facebook.com/glamnolallc/)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d9nj2jx] (score 9, diepte 0) I am out and about right now and only had a moment to scan pics and I cannot wait to get home and deep dive in to this magnificent beast of a post.  I live for these recaps!
[d9nl9ng] (score 6, diepte 0) Amazing recap and photos!!!
Things that look especially amazing:
1. YOUR CAPE!  Who knew you could have a cape?!  Awesome!
2. Your first look is so sweet!
3. The secondline!  What a great tradition!  

Your wedding looks all around awesome and your photos captured it perfectly!  Congratulations!!
[d9njf87] (score 5, diepte 1 OP) I get nervous about putting my life on the internet, so I made this post and am off to attend a party. I hope I come back to lots of comments and questions!
[d9nkm0a] (score 4, diepte 0) why did no one tell me about bridal capes BEFORE I brought my dress? it looks so amazing and fun!! your wedding looks to be perfection.
[d9njlgp] (score 3, diepte 2) Haha  Yea, its terrifying but take some comfort knowing an internet stranger is going to pop a bottle of wine and enjoy reading through!
[d9nqty3] (score 3, diepte 0) Oh my gosh! Love it!! 


I'm getting by married in New Orleans in March and this post just got me even more excited!

We are getting married in Jackson Square as well. Did you guys have the gates to the park closed at all? What about all of the people in/around the park? How was it?!?! One thing my fiancé and I are curious about are all the spectators!

Congrats :)
[d9nthl9] (score 3, diepte 0) Teal hair and a cape?! You're amazing.
[d9nlf0s] (score 2, diepte 3) So enjoyable to look through! Congrats bride! What an awesome day. I really hope that couples walking down the aisle together becomes more popular as its so adorable looking and so meaningful. I get why people walk with their dads (I will) but I also feel like FH and I would have enjoyed walking in together.
[d9po76z] (score 2, diepte 4 OP) Thanks! It actually made the day much more special I think! Plus we have those photos to cherish forever!
[d9njh9a] (score 2, diepte 0) I'd love to know who all of your vendors were!
[d9njmce] (score 2, diepte 1 OP) Oh I forgot! I'll add it now!
[d9nlcb9] (score 2, diepte 1) Such a nice modern take on the veil I think!
[d9pobfb] (score 2, diepte 1 OP) Thanks! I specifically said, "I want a cathedral veil, but not a cathedral veil." And taaaadaaa
[d9nkm9n] (score 2, diepte 0) Yea, this is totally awesome- you look SO HAPPY.
[d9poaa8] (score 2, diepte 1 OP) That cape, tho! I went into the bridal shop and said I wanted a cathedral veil, but I really didn't want to have anything in my hair especially not all night because of dancing. This was the third caped dress I tried on and I almost didn't because the shop was really hot and trying on dresses is a sweaty, tiring business already.

It fit like a glove off the rack and I bought it that day. I only even went to the shop to help one of my bridesmaids get a dress and had no intention of shopping for myself that day!
[d9nrvh3] (score 2, diepte 0) I LOVE your recap! Having the pictures in the text rather than scrolling through the album later makes for a great vivid recap! You looked beautiful and it looks like you had a lot of fun! Congrats!
[d9ponde] (score 2, diepte 1 OP) You guys sure know how to make a girl feel special. Thanks!
[d9q5a79] (score 2, diepte 2) Omg that was our first dance song!! Love it <3
(25 reacties met lagere score weggelaten)

=== THREAD 66bqyx ===
SUBREDDIT: r/weddingplanning
DATUM: 2017-04-19  SCORE: 54  REACTIES: 39
TITEL: 4/15 Wedding Budget and Recap! (long)
POST (source_id=post):
Wedding Recap!!

Here's the budget and wedding recap for my 4/15 wedding! It was fantasy/scifi book series themed and took place in a historic library. I always loved reading these to see how real weddit weddings went down, and am here to give my own! We went in with a low budget because (now!) DH didn't want to spend a bunch of money on a wedding. Full disclosure: we really weren't trying to stick to a budget throughout the process. 

Guests: 100

Original Budget: $15,000

Updated Budget (when we picked our venue): $30,000

Total Spent: $41,276


Budget Breakdown (not all inclusive, but the major items)

* Venue: $24,588 -  Included catering, DJ, cake, 4 hours full bar service

* Photographer: $3,800 - Included Engagement photos, 8 hours, second shooter, Italian-made Album, and LIMITED videography (we'll get unedited video files)

* Officiant: $650 - Actor Stephen Macht was our officiant. He wrote our entire ceremony script which was personalized off of our love story. It was amazing!

* Dress: $1,145 - Casablanca 1992 dress

* Headpiece/Veil: $366 total for both. They barely stayed in my super fine hair all night.

* Flower Girl Baskets: ~$100 for 2 baskets

* Shoes: $196

* Save the Dates: $185 - Magnet save the dates from Minted

* Florist: $850 - Included 1 bridal bouquet, 2 bridesmaids bouquet, 1 toss bouquet, bouteneers & corsages for immediate family, and other flowers for the centerpieces, arch, etc.

* Child Attendant (3) Favors: $115.55 - Included 2 getting ready robes, 2 personalized hangers, 3 personalized tumblers, and 2 Evenstar Necklaces for the flower girls to wear.

* Parents Favors: $277 - Included hangers, robes, and MOB dress.

* Bridesmaids Favors (2): $178 - Included hangers, robes, and a bracelet

* Groomsmans Favors (2): ~$60 - Personalized beer steins (DH bought these with his own CC so I don't know the actual amount)

* Bridesmaids Dresses (2): $327 - Azazie Kinley dresses in lilac & samples

* Groom & Groomsmans Suits (3): ~$600 (DH bought these with his own CC so I don't know the actual amount)

* Cake Topper: $132 - Completely personalized design

* Invitations: $477 - included foil-pressed Minted invites & rsvp, as well as materials to put wax seal on envelope

* Photobooth: $461 - Included 4 hours of unlimited photo booth time, 2 prints per strip, 6 personalized props (the faces of our cats XD), and a photo album

* Hair: $250 - included trial and day-of (both $125)

* Makeup: $285 - Included trial ($90) and day-of ($195)

* Ceremony & Reception Decor: $734 - Included lanterns ($113), personalized signpost ($166), and picture frames ($45), Books ($188 accounted for), Sand Ceremony Materials ($156), The One Ring Bearer Outfit ($82)

* Wedding Bands: $2,200 - Included platinum band for me ($1,600) and White Gold carved band for him ($600)

* Wedding Favors: $816 - Sugarfina Rose champagne gummy bears

* Ceremony Programs: $53 - 125 Zazzle programs

Overall, the wedding was an amazing success! There were minor things that went wrong but they were mostly things I didn't care about and put much planning into. 

What Went Wrong: 

* I was 40 minutes late for the first look (it was a bit of an ambitious timeline for the getting ready photos). The first look was planned for 3 PM, the ceremony at 5 PM, so there was still plenty of time for early photos.

* My hair was too fine to hold both my veil and metal floral hair comb. We got some photos before the ceremony and first look, but we ended up taking the comb out and leaving the veil in for the ceremony, and then switching them during the reception. When we switched them, the comb still wouldn't stay in very well and ended up taken out sometime during dancing. 

* My bridal bouquet was not overflowing as I had wanted. Flowers were really pushed to the wayside in my planning and it really wasn't a big deal to me. I noticed it, shrugged it off, and moved on.

* The florist had flowers coming straight out of the entirety of the door of the lanterns. I had wanted them cascading out the bottom of the door. *Shrug*

* My shoes caused blisters, and one of them popped on the way to the sand for some sunset beach photos. As soon as I stepped in the sand, it got ground into the open blister and hurt like a mofo. I immediately took my shoes off and didn't put them on the rest of the night.

* DH and I went out to get the sunset pictures during dinner, before we were served the main course but after the salad. When we got back in during dinner, everyone had food EXCEPT us. We sat there for like 10-15 min without food while everyone was eating. What we think happened is that the wait staff saw we weren't at our seats when they went to serve us and put our food back to keep in warm--I would have preferred cold food with more time to eat then waiting around for food the one chance we had to eat it.

* I barely ate anything that day, and when presented with dinner couldn't eat much. The prime rib I got was pretty tough, and my dress was tight and I was past the point of hungry from not eating pretty much all day.

* They almost sent me down the aisle at the complete wrong time!! So I had my own wedding coordinator, and then the venue came with one. The venue coordinator we had been communicating with had not been present at the rehearsal--her assistant was. We thought maybe she doesn't do the day-of stuff. Well the assistant wasn't at the wedding, and the coordinator didn't come to the rehearsal. We decided that my queue would be one of the groomsmen starting to play my bridal processional on his guitar. I couldn't hear the wedding party processional very well from where I was standing. The venue coordinator and my personal coordinator were off and away to queue their assistants to send me. The venue coordinator's assistant told me to go, and I took one step... and was like no wait there's no way the GM got set up and ready to play in that much time. My coordinator's assistant said she hadn't queued us yet. When the GM started playing though, he used his own amp and it was super loud, so I knew exactly where to start.

* I have no idea what happened to the cake they didn't serve. They definitely didn't bring out the sheet cake. But we had wayy more cake then necessary and I didn't really want to come home with an entire sheet cake so it's all good.

* The accessories to the sand ceremony box I got got thrown away (the sand keeper plate and adhesives for a photo). I bought replacements for $10, but they charge $14 shipping -_-;

* I sent a few people to go get my flip flops to replace my awful shoes. They come back with the heels i wore for the rehearsal dinner. -_-;

* Didn't get to talk to as many people as we would have liked. I think they were too intimidated to join us on the dance floor. But a lot did come around the edge and we talked and danced a bit before they continued onward.

* Afterwards, people mentioned their favors disappeared. Some had half eaten boxes on the table that when they got back were gone. DH and I spent time with his sister two days after the wedding and we mentioned how we were a little bummed we didnt get any gummy bears (we live close enough to the store to just pick some up though). She mentioned how MIL ran around from table to table collecting them from "people who left"...or apparently were on the dance floor and photo booth. SIL grabs a few to give to us and at least one was already opened and half eaten...hmm...

* We didn't make it through some of the songs I wanted to hear during dancing. I had one last-minute request that wasn't even on the list the DJ printed out. 

* My parent's shady bounced the day after the wedding. I called them up at 8am to maybe get breakfast before the 8 hour drive back, and they had already left. My dad wanted to avoid traffic or something. On a Sunday. 

What Went Right:

* DH's friend had flip flops I could wear in his car for the walk to the bar at the after-party!

* Nobody got too drunk! 

* DH and I didn't know each other's vows. We had my MOH read them (english major) to make sure they weren't so noticeably different in format and timing etc. Our vows were EXACT FOILS OF EACH OTHER. DH promised not to bring home any cats. Except maybe the orange one. I told him he wasn't allowed. It was awesome. 

* Everyone complimented how beautiful the ceremony was. It was completely personalized to us and the officiant basically told the story of our relationship. We both ended up tearing up at one point or another, which I wasn't sure was going to happen...I'm hit or miss with emotions.

* We were ahead of schedule so had plentyyy of time for dancing. 

* The photobooth was a huge hit. A couple of friends groups took majority of the pictures, but they had great fun. DH and I even got in a few photos after being dragged over there

* Everyone loved the gummy bears (who didn't have theirs taken hahaha)! 

* Child Attendants made it down the aisle! The two flower girls (almost 6yo) walked down the aisle hand in hand with their brother (18mo). Their mother told them whatever you do DONT LET GO OF HIS HAND. At a certain point when they got a couple rows into the chairs, the ring bearer stops. He looks around at the people. The flower girls look confused and liek what do I do??? He eventually continues walking again and makes it all the way down :)

* We had only 2 no-shows (that we hadn't heard about in the days before). Some other members of the family made it, but I didn't catch the explanation other than "something came up". NBD. 

* DH wanted Closer by Nine Inch Nails to be the last song of the night. I totally vetoed it. We joked with the DJ about it. During dinner he came up and asked if he was the one that wanted that song.. and mentioned he had a karaoke instrumental version and if we wanted him to play it. DH got Closer at our wedding. 

* The Groom's Cake was amazing (BIL made it). We succeeded in cutting the actual wedding cake with the Sword of Gryffindor. It was awesome. We did the limbo with the sword during dancing later.

* Most of the photos we had displayed around the room as favors got taken. We had about half photos of just DH and I, and half were photos of us with friends. Only 2 photos with us with friends were left, and a small stack of photos of just us were left. I wasn't sure if people would actually take them :)

* Walking down the aisle to GM playing guitar was awesome! He messed up at one little part (and played through it as a seasoned musician would) but it's ok. The timing was a bit off (The walk ended up shorter than the time of the song I wanted played) but that's ok, and we figured that would happen at the rehearsal. 

* We had 17 people at the bar for the after party! 

* My SIL (Brother's wife) was at the after party with us. At about 1:20 (bars close at 2), she said "OK you guys need to leave. Now. You shouldn't be here still". So we were like ok, started trying to gather our friends who were at the same hotel saying lets go back then, and she goes "No! Leave *by* *yourselves*. Alone." So we walked hand in hand back to the hotel room

* Back in March, Aunt Flo was scheduled to arrive 2 days before the wedding. She miraculously decided to arrive *10 days* before the wedding! And we actually made use of the "lover's kit" the hotel provided in the suites. Before the wedding I put it at 50/50 we'd be too exhausted ;)

* We went to Disneyland the day after for our minimoon (before the real honeymoon in 3 weeks) and didn't die of exhaustion! We are annual passholders so it wasn't anything too intense. 

Overall the wedding was amazing. My MOH commented how I was not bridezilla at all, and how she was probably a bit more MOHzilla than I was. I got to see good friends and family, had a great time, and can't wait to see the photos in 3 weeks!!

Photos (I dont have as many of decor and whatnot):

Child Attendants: http://imgur.com/a/uZdnv
                          http://imgur.com/a/YeXJs

Ceremony: http://imgur.com/a/bgZti

Wedding Cake: http://imgur.com/a/M0Z97

First Dance: http://imgur.com/a/uBjib

Signpost at Entrance to Reception: http://imgur.com/a/BYhNb

Best Man, Bridesmaid, and MOH with ALL OUR CATS: http://imgur.com/a/bkT1g

Walk back to the hotel: http://imgur.com/a/QZJ9H

Disneyland!: http://imgur.com/a/mY0mI

Harry Potter table centerpiece: http://imgur.com/a/VR0cQ

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dghcvcs] (score 15, diepte 0) I'm glad to see I'm not the only one who had an initial budget, then updated once we picked the venue, then also a "here's what we actually spent instead"!

It sounds like you guys had an awesome weekend!
[dgh86ir] (score 7, diepte 0) Guest count? Great - detailed write-up! Any pics?
[dgha6gn] (score 5, diepte 0) That's a super unique officiant! Did you know him personally or find through another source? Thanks for the write up!
[dghffbq] (score 5, diepte 0) I don't normally gush over signs but I love that signpost!
[dgh87m1] (score 3, diepte 1 OP) Ah sorry! 100 guests! I'll try to slip some links to photos in there
[dgh8ior] (score 3, diepte 2) Nice! Budget situation sounds very similar to ours ($15K plan, $30K budget now that we found our venue, will probably end up being closer to $40K) but we have ~150 guests!
[dghemfk] (score 3, diepte 1 OP) In the Los Angeles area of California.
[dgh7wxk] (score 2, diepte 1 OP) So I had that number in my budgeting thing... I just went to go look up the receipt (yeah it seemed expensive). It was actually $366.24 for both. I think the clip was ~$150 and the veil was ~$200 (including tax). The $548 was the down payment for the dress at the same boutique haha.
[dghelh0] (score 2, diepte 0) Out of curiosity, what state did your wedding take place in? Congrats!
[dghfr71] (score 2, diepte 1 OP) https://www.etsy.com/shop/DevcoDesigns

I had to put them on my own signpost, but that was easy compared to making the signs themselves :)
[dghfzfq] (score 2, diepte 0) How many sugarfina bears did you give everyone?? I was considering them for favors, but the bulk boxes are $45 each... I was thinking of getting 2-3 of those bulk boxes and putting bears in sheer organza bags for people. Topping out at $150 max. How'd you get to $816? I'm worried I'm underestimating what comes in the boxes!
[dghi5zl] (score 2, diepte 4) I definitely appreciate the tip, but my favors budget is $150, so I'm stuck with the champagne ones! But I've had them before and loved them, and haven't had the rose ones... so I'll just pretend I don't know they're better!
[dghj8jn] (score 2, diepte 6) now THAT is a good idea! my bridesmaid and I will eat those while we put the champagne ones in the little bags... bahaha.
[dghofxt] (score 2, diepte 6) https://www.sugarfina.com/shop/baby-champagne-bears/

You can also get regular sized ones, I just think the minis are extra cute! Also, the bulk discounts are awesome. One 2.5lb bag is $45, but 2 are $75, and 3 are $112.50.
[dghlr94] (score 2, diepte 1 OP) My own coordinator helped me plan the wedding, and helped me pick the venue. She also had a hand in helping me pick out the decor and knew what was going on at the wedding, as well as referred me to vendors to use as florists, makeup artists, and the photo booth people. 

The venue coordinator didn't even come to the rehearsal. Need I say more?
[dghsqar] (score 2, diepte 1 OP) Actually at my brother's wedding, they had a bunch of leftover favors. I think it's hit or miss. They set the favors as part of the place setting so that probably helped
[dghshlr] (score 2, diepte 0) LOL I'm kinda sad you didn't want to end the night with "I wanna fuck you like a mailman." :P

Edit: ughhhh auto correct. Mailman is funnier.
[dghsloh] (score 2, diepte 1 OP) I thought it was hilarious but totally inappropriate. One of those things I had to veto out of principal. If he had somehow convinced the DJ to do it I wouldn't have been upset though lol
[dghclil] (score 1, diepte 1 OP) No we didn't know him! He showed up on wedding websites advertising as an officiant lol
[dghgagn] (score 1, diepte 1 OP) The rose flavor doesn't (didn't??) come in bulk (i.e. massive bags), which is what we originally wanted to do, so we had to go with the small individual boxes. They were $8.50 each on sugarfina's site, and the bulk discount (5 cents, yay?) started at 250 boxes and we only needed 100. I found that Nordstroms sold them in 6-packs for 48 dollars ($8 each!), so we bought 17 6-packs from Nordstroms online. They shipped directly from Sugarfina -_-;

We then added personalized stickers to either side of the box (~$20 for the stickers)
[dghgfe3] (score 1, diepte 2) Oooh, gotcha. I'll stick with the regular champagne ones, then! Good to know.
[dghgi2y] (score 1, diepte 3 OP) Just fyi... the rose ones are wayyy tastier ;)
[dghil4j] (score 1, diepte 5 OP) Good plan. You should order a box of the rose ones for yourselves imho though :)
[dghn3y6] (score 1, diepte 5) I freaking love the champagne gummies. And thanks for the insight on being able to buy them in bulk. I was only able to find then in the small individual boxes.
[dghlmmh] (score 1, diepte 0) Do you regret having both the DOC and venue coordinator? If so, which one would you choose?
[dghnzwr] (score 1, diepte 0) See, this is why I don't want to do favors. People are thieves and will run around grabbing them! F that.
[dghocvr] (score 1, diepte 0) I love the ring bearer's LoTR cape!
[dghos1b] (score 1, diepte 1 OP) Thanks! We dubbed him the One Ring bearer (he had it around his neck). The flower girls had the Evenstar necklaces to match :)
[dghsrkk] (score 1, diepte 1 OP) Redondo Beach Historic Library
[dghxdg3] (score 1, diepte 0) Congratulations! Everything looks gorgeous! How did foil on the Minted invitations turn out?
[dghxpfj] (score 1, diepte 1 OP) Beautiful! At first I wanted to cheap out on invitations, but then I found these foil pressed silver invitations with a lilac watercolor pattern. If I didn't get foil the details would be gold, so I had to get foil since the colors were silver and lilac :)
[dghza6x] (score 1, diepte 0) Where/how did you print out the pictures of your cats for the signs? Incredibly tempted to steal this idea.
[dghzljr] (score 1, diepte 1 OP) The photo booth company printed them for me! I have a prosumer Nikon D5600 and tried to take close up, high resolution photos of them. The photo booth company printed them out and put them onto paint mixing sticks. They charged $2 per custom print
[dgk6nhd] (score 1, diepte 0) Thank you for the write up! Your RB wedding looked like so much fun! Where did you get the cat photobooth things?
[dgk6thr] (score 1, diepte 1 OP) The photo booth company (creative photo booths) offered to print custom props for $2 each. So I got super high resolution photos with my Nikon D5600 and photoshopped the background/body out and sent them to the company to be printed :)
[dghmn9n] (score 0, diepte 2) Nope.  Lol
[dghspzu] (score 0, diepte 0) What's the name of the venue?
[dghtcm0] (score 0, diepte 2) Thanks! Adding this to my venue spreadsheet!
[dgh7kza] (score -8, diepte 0) How do you spend $548 on a veil and headpiece???

