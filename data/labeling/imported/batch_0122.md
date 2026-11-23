# Label-batch batch_0122

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
Schrijf het resultaat naar `batch_0122.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: mqzgsz, 1lkzorf, 10veoq0, rt6ep7).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD mqzgsz ===
SUBREDDIT: r/weddingplanning
DATUM: 2021-04-14  SCORE: 68  REACTIES: 24
TITEL: Budget Breakdown/Wedding Recap: $20K HCOL (Chicago) Spring Saturday Wedding
POST (source_id=post):
I loved the budget breakdowns when I was planning so figured I would share my own from April 2021 in Chicago. We planned for around a year and a quarter, no postponements; though we did have to make arrangements for dealing with covid-19.

A couple photos focusing on photographer stylized shots and showcasing a bit of the venue (I LOVED her work, I usually hate how I look in most photos and loved these).

[Adriane's photo style was amazing. I've never felt prettier.](https://preview.redd.it/bfd7i4leu6t61.jpg?width=1125&format=pjpg&auto=webp&s=8587283a6a937d4892e29972d1a82288250bc9e7)

SUMMARY

**The wedding**: 40-person, Saturday Evening in April 2021 in Chicago, where we live and the majority of our friends and family live close by. Flights were required for 5 attendees.

**About us:** late 20s professionals

**Length of relationship/engagement**: 5.5 years / 18 months

**Original Budget:** 30K

**Actual Spent:** $20,596

**Wedding Vibe:** For us, our relationship has been about food and travel. Living in Chicago for us has been about food and beautiful architecture/old buildings. We wanted to prioritize these things in our wedding. Our main focus was Venue and Food.

**Invited: 54**

We only invited immediate family and close friends. Aunts/Uncles/Cousins didn’t make the cut with the exception of our officiant and his parents. We both live a few hours drive from our home towns, and our friends have mainly stayed in the area with a few branching out. Guest list was 23 people in-town (plus 7 plus ones), 9 people who could drive 4-6 hours (plus 1 plus one), 8 people with a 2-6 hour flight (4 plus ones), and 2 who drove 14 hours because my MOH was too pregnant to fly. Anyone in a relationship got a named invitation for their partner and we gave everyone else a plus one. We assumed most of these unnamed plus ones would go unused (9)

**RSVP’d yes: 42**

This was very close to what we anticipated. Most of the no’s were plus-one declines (8), one couple that was worried about Covid and didn’t have their vaccine yet, and a great-Aunt and great-Uncle we invited because we “had to” but knew they wouldn’t come.

**Attended: 40**

One of our flight-requiring friends ended up having to work, so she and plus 1 didn’t make it. They informed us the day after the wedding.

COSTS

All numbers include tip and tax.

***Venue: $3750***

* **Ceremony and Reception venue: $3750 ($3500 plus $250 tip)**
   * [Colvin House](https://colvinhouseevents.com/): We held both our ceremony and reception at Colvin House, a beautiful, architecturally eclectic Chicago mansion from 1909. We booked the whole first floor and got a groom’s suite and bridal suite included in the package. The living room was used for the ceremony and reception, and the dining room was used for cocktail hour. Dancing was in the central space, and the courtyards in the back and front patio were set up to hang out.
   * We got use of the antique furniture they’ve collected which made the ceremony and reception look super cool.
   * The venue coordinator was amazing. This woman loved her job. Every time we checked in she had a new project she was working on to improve the house: new furniture for the groom’s suite, new furniture for the bridal suite, new rugs, new furniture for use downstairs.

***Food and Drink: $7669***

* **Catering and Dessert: $6027 (includes tax and gratuity)**
   * [Jordan’s Food of Distinction](https://www.jfod.com/): Food was one of our top priorities (if not THE top), and it was EXTRAORDINARY. I wish I could eat my wedding day meal again. May have to order some food to go at some point. We got compliments on the food all night, they were incredibly accommodating of us and our foodie tastes. We had 4 passed apps at cocktail hour, soup and salad at the start of dinner, 3 entrée choices, and a cookie and ice cream bar for dessert. (This number included our 2 vendor meals, linens and bartender). Edit: Sidenote, they brought us hors d'oeuvres while we were taking photos during cocktail hour. SO THOUGHTFUL!
* **Bar: $1117**
   * We bought all of our own alcohol and mixers from Costco and Binny’s and admittedly bought WAY too much; we’ll be having a summer party/housewarming on our deck later to use some of it up. We included champagne, multiple types of  red wine, white wine, beer, Brandy, Gin, Rum, Tequila, Whiskey, Vodka and an assortment of mixers. Jordan’s Food of Distinction provided the bartender and the garnishes.
* **Coffee Caterer: $625 (525 plus $100 tip)**
   * Event Espresso Catering: My husband is an espresso enthusiast and we make some espresso based drinks every night together. It's our own little ritual. So for fun we added an espresso bar to our wedding. They were there from cocktail hour until about 8PM and served tea and espresso drinks. It was a huge hit and they were very easy to work with.

https://preview.redd.it/7jb73tvj97t61.png?width=627&format=png&auto=webp&s=98ae38a399c86a2971983d80be8263cb719286dc

* **Late Night Snack: $0**
   * This is the only part of the wedding I would say went wrong. We placed a doordash pre-order for White Castle to be delivered to the house. At the delivery time we had people outside at both doors and no one ever showed up. We got the money refunded but were a little disappointed we never got our late night snack. I’m still craving fries and sliders.

**Attire: $2197**

* **Bride’s Attire: $1134**
   * I wore [Rebecca Ingram’s Elsie](https://www.maggiesottero.com/rebecca-ingram/elsie/16205) dress in Ivory over soft Pearl from (now closed) Klassic Bridal. I did get a discount at her grand opening which the price above reflects. My original budget was $1000 but the dress was just it. I’m planning to either alter it to a cocktail dress or donate it.
* **Brides alterations: $330**
   * Alternations were done by [Javonica](http://www.javonicachicago.com/). She did a phenomenal job. The dress fit like a glove. Got a single point bustle and had it hemmed to fit me at 5’1” plus heels.
* **Bride’s accessories: $529**
   * I bought my accessories ($158) at Klassic Bridal because I wanted to support her grand opening. Bought earrings, bracelet, veil and hair piece. Ended up swapping out the earrings for a pair I already own.
   * Shoes ($371 with a discount) I spent a long time looking for and they’re by far my favorite piece from this, they’re so versatile. [Marion Parke: Must Have 85 Pump](https://www.marionparke.com/product/must-have-85-white-nappa-leather-classic-high-heel-pump/) in white Nappa leather. Landed on these particular shoes because they were designed by an orthopedic surgeon and swear to god they’re the most comfortable heels I own. No blisters, no pain, I broke them in beforehand but honestly could’ve gone without. HIGHLY recommend.
* **Groom’s Attire: $384**
   * My Husband wanted to buy custom suits for him and his groomsmen (see groomsmen gifts below). He and his groomsmen went to [Indochino](https://www.indochino.com/suits/personalization) and he bought a 3-peice suit in grey and they all got matching lining. He used a white shirt he already owned.
* **Groom’s Accessories: $0**
   * Husband opted to use shoes, socks, watch, and a belt that he already owned.

***Beauty: $735 ($635 plus $100 tip)***

* **Trial: $225**
   * Did my trial and wedding hair and makeup with [Elle Artistry](https://www.elle-artistry.com/). Highly recommend doing a trial and then going out and doing something to test it. I did end up finding things I wanted to change for the day that I wouldn’t have known otherwise.
* **Hair and Makeup: $225**
   * The hair and makeup artists came to the venue to do our hair and makeup in the bridal suite. I did a half-up-half down do and traditional makeup with lashes.
* **Bridesmaid: $185**
   * I paid for my bridesmaid’s hair and makeup. My bridesmaid opted for a simple blowout/curl and airbrush makeup.

***Rings: $500***

*This section is where we saved the most money. We budgeted 2k, and spent 25% of that.*

* **Bride’s ring: $227**
   * We bought both of our rings from [Hitched](https://tryhitched.com/). I went with a simple 2mm platinum [band](https://tryhitched.com/collections/womens/products/platinum-flat-2mm) to compliment my E-ring. I now can't find it on their website.
* **Groom’s ring: $273**
   * Groom ended up going with a black Tungsten beveled [ring](https://tryhitched.com/collections/tungsten/products/tungsten-beveled-edge-8mm) with a silver edge in 8mm AND got a second “beater” ring in the same style and color but in ceramic ($99).

[His ring, my ring and my E-ring in the bridal bouquet.](https://preview.redd.it/lfmk7q83v6t61.jpg?width=1125&format=pjpg&auto=webp&s=2ccb7e32a73b3de8eca617f0ecdf8ca83d085595)

***Stationary: $323***

* **Save the dates: $77**
   * Save the dates we designed ourselves and printed at a print shop near us. They were a simple postcard, double sided in an envelope.
   * Stamps: $20
* **Invitations: $246**
   * Invitations ($143) we bought online at [Truly Engaging](https://www.magnetstreet.com/) by Magnet Street. Cost includes 30 foldover pocket style invites in satin with silver embossing, 30 information card inserts, and 30 envelopes with liners, Guest and Return addressing, and envelope tape.
   * We bought wax, 2 wax stamps, and a wax melter/spoon to seal the invites ($83 Amazon).
   * Stamps: $20
* **Thank You cards: TBD**
   * We still need to do these
* **Programs: $0**
   * We did not have programs.

***Officiant and Licensing: $275***

* **Officiant: $210**
   * My cousin officiated. We bought him a nice bottle of whiskey as a thank you.
* **License: $65**

***Photography: $849***

* **Photographer: $849 ($749 plus $100 tip)**
   * We got a package with [Adriane Dean](https://adrianedeanphotography.com/) for 6 hours plus an engagement shoot. She shot us getting ready, ceremony, family photos, couples portraits, first dances and toasts, and 30 minutes/1 hour into dancing. She was INCREDIBLE. So efficient and got some amazing shots. She captured everything, even the 2 of us ugly crying at the altar, and sent us every photo in digital form and on a flashdrive (1000+ photos). She edited a select few and let us choose some to be edited. Since we booked her last year, she has left Chicago for Rockford but did our wedding anyway.

***DJ and lighting: $300***

* **DJ and lighting: $300**
   * Groom owns a DJ and lighting company. He ran around setting up all the lights and speakers the morning of the wedding and he hired one of his DJs for the night for $300.

***Flowers: $1511***

* **Flowers: $1511**
   * We used [An English Garden](https://www.anenglishgardenweddings.com/) per the recommendation of one of our couple friends and they did not disappoint. We gave them loose guidelines and a few specifics and they ran with it so well. This includes one bridal bouquet ($225), one bridesmaid bouquet ($70), 3 boutonnieres ($39), boutonnieres/corsages for parents ($120) ,centerpieces for 6 rounds and the head table ($395), and a large arrangement for the fireplace ($250). Delivery and taxes were $412.
   * Note: We had them drop off the reception flowers and family and catering set them up. Our actual centerpieces (large mercury glass candle holders that we bought separately) disappeared, so my FIL innovated and made new centerpieces from the loose tulips we requested.

[This was either the bridal bouquet or the bridesmaid's bouquet](https://preview.redd.it/jnhkqy50v6t61.jpg?width=1125&format=pjpg&auto=webp&s=3ebb34b0873f1771da8445e533360ba9d8cba026)

***Decor: $937***

* **Dishes/Glassware/Flatware: $600**
   * We found that buying all our dishes at a restaurant auction was cheaper than renting them. We bought enough dishes for 50 people (plus extras because of lot sizes) including bread/butter plates, salad plates, soup bowls, dinner plates, and dessert bowls. At the end of the night we donated them to the venue. Found the same went for buying glassware and flatware. We bought champagne flutes and wine glasses from Ikea and flatware from a commercial kitchen supply company.
* **Centerpieces: $136**
   * West Elm Mercury Glass Vases. These never got used because they were misplaced but are now sitting in our house.
* **Candles for Centerpieces: $25**
   * Bought an assortment of unscented pillar candles from Ikea to place in the vases.
* **Namecards: $176**
   * Bought gold namecard stands on Amazon and placed the wax seals on the corner in different colors to indicate meal choices.

***Gifts: $1002***

* **Groomsman gifts: $682**
   * We bought the custom suits from Indochino for the 2 groomsmen. Groom picked out the fabric and the groomsmen got to choose their own style. They both went for 2 piece suits. They all
* **Bridesmaid gifts: $320**
   * My original plan to buy a fancy pair of shoes for my MOH fell through when she got pregnant and her feet swelled. So I tried to quickly pivot and settled on buying a message and mani-pedi for my MOH and then splurged on her baby shower gift.

***Accommodations and Transport: $194***

* **Hotel night: $120**
   * We stayed at the hotel closest to our wedding venue which ended up being a Hampton Inn.
* **Transportation: $74**
   * We set aside $500 in Uber credit for our guests to travel to and from the hotel. Only $74 of that ended up being used. We also had free access to the parking lot attached to the venue, so a couple families drove.

***Misc:  $254***

**Rehearsal Dinner: $???**

* My parents paid for the rehearsal dinner which covered dinner for 15 people. We went to Simply Pasteur for phenomenal Thai Food. I have no idea how much they ended up paying. Apologies since this doesn’t help with budgeting.

**COVID contingency: $254**

* We ended up with a few extra costs associated with Covid-19 that we didn’t originally budget for.
* Covid supplies ($152) included a wall mounted temperature sensor, 50 personal size hand sanitizer bottles, an automatic hand sanitizer dispenser, 2L of hand sanitizer, 50 paper masks individually bagged.
* To comply with Chicago guidelines for covid-19 we had to decrease table size to 6 and add an extra table ($12 rental), an additional centerpiece ($62), and an additional tablecloth ($28).

***Wrong Estimates and Forgotten Items:***

* **Under-estimated items:**
   * Dress
   * Hair and Makeup (and trial)
   * Flowers
   * Invitations
* **Forgotten Items**
   * Flowers for parents
   * Delivery fee for flowers
* **Items not in budget**
   * Honeymoon
   * Engagement ring
   * Rehearsal Dinner

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[guj66q5] (score 14, diepte 0) Thank you so much. So comprehensive and inclusive. This is what i want to see! Congrats on coming in 9K under budget.
[gukboqo] (score 7, diepte 0) Your friends only let you know the day after your wedding that they weren’t showing?? I’d’ve lost my shit
[gujkvho] (score 5, diepte 1 OP) Thanks! I was stunned, but my husband is a bargain shopper and did a ton of work figuring out how to cut costs without cutting quality!
[gujaqcl] (score 5, diepte 0) Beautiful - thank you for sharing and congrats!! So jealous you found a platinum band for $227. No wonder they don’t sell it anymore that’s a steal
[guka5o8] (score 5, diepte 0) We also booked the Colvin House and postponed from 4/24/21 to 10/9/21. Sarah, the coordinator, is fantastic! We plan on using her services for floral, food, cake, and decor/ linens/ rentals. Congratulations!
[gujbbk5] (score 4, diepte 0) Gorgeous!  I used to live right by the Colvin House.  Such a great area fo photos too.
[guljsar] (score 4, diepte 1 OP) I'm giving her the benefit of the doubt. She's young. Like just graduated from undergrad and is now starting grad school. I think this is the first wedding she's had to RSVP for herself and doesn't quite understand.
[gukjn3u] (score 4, diepte 0) This is so helpful! I'm shocked at how inexpensive your photographer was. I'm in the bay area and all the decent ones are at least $3k. Your pictures (and dress) are gorgeous!

Any tips for finding a caterer? Food is our top priority, but I'm having a hard time finding someone that can do a great farm-to-table meal but isn't over the top fancy.
[gujqmr3] (score 3, diepte 1 OP) It really is! And we got lucky with the weather in April so could take outdoor photos at the beach and little park next door.
[gulkadm] (score 3, diepte 3 OP) We didn't even think of taking any in the purple bathroom!!! My favorite photos are from the stair case. Wanted to use the sun room and the side room with the black windows and black tables but we ended up with tables in the sun room and the caterer was using the side room. Side note: we wish we had taken family photos out front and not in the back. It's prettier out front, but my mind went "light is on the back let's go there"
[guj6ewp] (score 2, diepte 0) Wow! Thank you! This gives me a lot of insight
[gujpmro] (score 2, diepte 0) This is so detailed and super helpful, thank you!!
[gujpzc7] (score 2, diepte 0) Your wedding sounds lovely and so delicious, omg! As a fellow foodie-and-travel Chicagoan I can't wait until we can do more of both again.
[gukac51] (score 2, diepte 1 OP) Congratulations to you as well! Sorry you had to postpone. Sarah is amazing! We didn't use many of her other services, but I'm sure she's great for the rest of them too! Best wishes for your wedding!!!
[gukq82h] (score 2, diepte 2) We wanted our wedding to be as “normal” as possible, so the best decision for us was to postpone. We’re hoping for no more than 80 guests. We absolutely adore the venue and are so excited! What were some of your favorite areas of the house for couple photos? We’re digging the purple bathroom on the second floor!
[gumuz3c] (score 2, diepte 4) Thanks for sharing! I definitely agree— family photos out front if possible (depending on lighting). The stair case is simply stunning. I hope you got some amazing shots there!
[guqer09] (score 2, diepte 2) Thanks for the advice! My fiancé is from Chicago and now I’m tempted to just move our wedding over there :)
[gylfhu9] (score 2, diepte 2) That photographer cost is a STEAL. Ours (also Chicago) is $3600 for proposal + engagement shoots, 8h day of with a 600-800 photo guarantee, a second shooter, and some prints, and we're pretty happy with how low that turned out for the quality of the photos so far. Anything I was looking at that cost like under 2k seemed like garbage quality and photos are super important to me. So impressive!
[gyli2hp] (score 2, diepte 3 OP) 100% agree. We were shocked that her cost was so much lower than everything else we looked at while still having quality photos.
[gum0641] (score 2, diepte 0) I'm so excited to have Jordan's catering our event now! We loved their food at the trial and loved the owner. I'm so excited! What were the entrees you chose??
[gum0nj2] (score 2, diepte 1 OP) We did:

-dry aged beef with thyme parsnip puree and house steak sauce (my choice)

-slow braised chicken thighs with creamy poblano chili sauce and cilantro oil (groom's choice)

-japanese crusted spinach risotto cake with shallot parsnip puree and grilled green beans (each almost chose this)

I legit want to see if I can order these as take away for our 1 year anniversary. They were that good.
[gujkylm] (score 1, diepte 1 OP) Yeah I don't know if I ended up with a pricing error or what but now it's $500! For a TINY ring (size 4)
[gukag9n] (score 1, diepte 1 OP) Haha I just realized your budget breakdown is the one I modeled mine after. Thanks for posting yours!!!
(2 reacties met lagere score weggelaten)

=== THREAD 1lkzorf ===
SUBREDDIT: r/gout
DATUM: 2025-06-26  SCORE: 1  REACTIES: 0
TITEL: gout or arthritis?
POST (source_id=post):
Hey everyone! So, first off, no one in my family has gout. But at the end of March, I noticed my big toe joint on my left foot was turning blue in the bath, like a bruise or something. Didn't think much of it because it didn't hurt. But then in April, my toe basically stopped bending, and that's when my whole doctor saga started, lol.

I saw a rheumatologist in April. The ultrasound showed bursitis, and she prescribed chondroprotectors (pills and a cream). She thought it was because my shoes were too loose, but I'd already switched to different shoes a month before that. Nothing helped, and it actually got worse – the skin on my foot started peeling off in chunks. Gross!

I decided to get my uric acid levels checked myself, and they were 460 (normal is under 360). My new doctor put me on allopurinol. After 3 weeks on a diet and 300mg of allopurinol, I got my levels down to 250, and now I'm keeping them around 300. But here's the thing: it's been two months, and my toe STILL won't bend!

I went to a surgeon who said it was tendinitis, then to an orthopedic doctor who diagnosed me with unspecified arthritis. A physical therapist prescribed magnet therapy and exercises. The magnet therapy helped a little, but not completely. The joint's a bit less red and the swelling looks like it's gone down a little. My toe can move down, but it still won't bend. Then I got sent back to the rheumatologist, and she said it was gouty arthritis, and to take NSAIDs and allopurinol. She also sent me to a hematologist because I have high white blood cell counts (but I don't have rheumatoid diseases, I got tested).

After that, I saw ANOTHER rheumatologist, and he told me to relax, keep doing the exercises, and take allopurinol – that's all I need. Honestly, I'm so tired of going to doctors and taking meds! It's so frustrating. I'm starting to feel hopeless; I have a whole pharmacy at home and nothing seems to be working. Has anyone else dealt with something similar? ( My English isn't great, so sorry if it was hard to understand)  
P.S I can include a picture, if you're not too squeamish heh

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

=== THREAD 10veoq0 ===
SUBREDDIT: r/rheumatoid
DATUM: 2023-02-06  SCORE: 24  REACTIES: 79
TITEL: What shoes have you found to not hurt your feet?
POST (source_id=post):
I need house shoes since I’m on hardwood floors a lot throughout the day.  Not able to wear sneakers or flip flops.  

Has anyone found shoes that don’t hurt their feet?  My feet feel in fire in the morning w/needles, sharp pains and sometimes ankle swelling.  

Thank you in advance

Edit:  thank you everyone for your responses!!  Looking forward to shopping tonight.  Have already started checking out your recommendations!!  

In the summer I wear OluKai sandals to the beach!  

https://olukai.com/collections/womens-sandals

Maybe some of you would like them!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j7h25om] (score 28, diepte 0) Crocs. They ugly and I live in them.
[j7hopgd] (score 15, diepte 0) I wear Birkenstocks most of the time if I’m wearing shoes at home. I’ve been wearing them since 1991 so am obviously accustomed to them. My feet like the support 99% of the time.
[j7h2qo1] (score 14, diepte 0) I really really love my Oofos sandals. I used to wear Dansko clogs (which I still do at work along with my Brooks). BUT for bad days, and I need to come home and cook dinner (and not use up the last of my “spoons”) I wear my sandals a lot. I have tried their version of clogs.. but they aren’t as great. They’re pricey.. but if you can find them on Expert Voice or some other discount app.. I don’t know what I’d do without them. My little one likes to copy me and put her shoes on too :)
[j7hb9s7] (score 8, diepte 1) Yes to this. And I've found the lined crocs (more like slippers) seem to have extra arch support compared with regular crocs! I keep both types around.
[j7h2dx7] (score 8, diepte 0) I also have hardwood floors so shoes are a definite must.  I wear cloud slides constantly at home.  I have a couple pairs and they are hands down my favorite shoes.  Some days I even end up having to wear them to work because I just can't handle regular shoes.

Oh and they form to your feet and stretch a little so swelling doesn't usually matter.  If they start getting a little loose I throw em in the washing machine and let them air dry and they are like new.
[j7h5pdx] (score 7, diepte 0) I decided to try Merrell and now I won't wear any other shoes. They are pricey, but I used to have such awful foot pain that I couldn't stand very long. Since I started wearing them, I have had no issues.
Side note: I also always have extremely cold feet, so I bought a pair of their winter boots and now I have no cold feet during winter.
[j7hq1oi] (score 7, diepte 0) hoka walking/ running shoes
[j7hg2w5] (score 5, diepte 0) I agree with Oofos, those are great recovery sandals! Orthofeet has great shoes, they are orthotic, come in a variety of sizes/widths, have lots of different ways to customize the fit, and I can usually wear them straight out of the box!
[j7iq108] (score 5, diepte 0) Adidas Stan Smiths, they are basically magic to my knees and feet.
[j7hj107] (score 4, diepte 2) Yes! I get the fleece lined ones. I use em around the house. I’d not be able to walk somewhat normal in the morning if I didn’t have my crocs to slip into next to the bed
[j7hh2oq] (score 4, diepte 2) Yes they are very comfy. They're [these ones](https://www.merrell.com/US/en/snowcreek-tall-polar-waterproof/53162W.html?dwvar_53162W_color=J001804#cgid=womens-winter-boots&start=1). I also wear boot socks with them.
[j7hgila] (score 4, diepte 0) Sketchers go walk with the memory insoles.
[j7h5gzh] (score 3, diepte 0) Personally, I found that heydudes are great shoes since they’re extremely light weight and soft, I use them mainly when going out to casual events. Shoes I would recommend for using at home are cloud slippers (can find them on amazon), they’re not the best looking but are very comfortable!
[j7hgip8] (score 3, diepte 1) Which Merrell winter boots did you buy? Are they comfy as well? My feet gets extremely cold as well. I need to use those foot/hand warmers when I'm out for longer than 15 minutes.
[j7hj2wa] (score 3, diepte 3) They look so warm!! I'll probably need to try them on in person because I'm not sure if I can pull up the zippers. Laces are hard on my fingers too 😔
[j7h8u1u] (score 3, diepte 0) Dunham makes great, wide, shoes.
[j7hdpxn] (score 3, diepte 0) I’ve found that sketchers slip ons are pretty comfortable and supportive and you can also machine wash them. My feet end up hurting after long periods of time or if I’m in a flare with those shoes but I’ve noticed I tend to be able to wear them longer than most other shoes I have. They can be a little expensive depending on your budget and which ones you get ( I can’t remember which ones I got sorry).
[j7hiqpj] (score 3, diepte 0) I use crocs around the house and I’ve found Skechers Max Cushioning series to be great! I recently got these in black https://www.skechers.com/skechers-max-cushioning-elite/17693_BBK.html figured, it’s not cute but at least in black I can get away wearing them even with leggings and tunics. I do have a Skechers pair for dresses, they’re not as cute as a lot of dress shoes are, but I really can’t do cute shoes unless they miraculously also are good on my feet. I have these https://www.skechers.com/skechers-slip-ins-on-the-go-flex---serene/136541_BBK.html 
They do have some that looks dressier in their flats section. If you have amazon prime you could use their wardrobe feature and pick 6 pairs of shoes and try ‘em on and walk around at home with them for a bit to find out which ones are a good fit and comfort for you.
[j7i2wu8] (score 3, diepte 0) I love my fit kicks. It's like walking barefoot, which is more comfortable for me. I have 2 pairs, one for nice occasions and the other for everything else.
[j7i76y1] (score 3, diepte 0) Merrill’s I have spent 1000s on shoes and I will never ever buy anything else again
[j7i9vcg] (score 3, diepte 0) Oofos sneakers are heavenly and perfect houseslippers. The sole is the perfect combo of supportive cushy and the elastic material for the body of the shoe is very comfortable.  The heel bends down easily to make is a slip on. 
https://www.oofos.com/products/womens-oomg-canvas-low-shoe-white-taupe?variant=31263002034291
[j7id06s] (score 3, diepte 0) Vionics. They’re worth every penny.
[j7ih11k] (score 3, diepte 0) I don't do crocs because my pinky toe is hammered so since the croc material doesn't really give way as in it doesn't really stretch it hurts my toe. I use Birkenstocks and Hoka one ones both are pretty comfy every doc I visit always compliments my hoka's and say they're the best before showing me the ones they're currently wearing.
[j7ikr4s] (score 3, diepte 0) Adidas Cloud Foam. They are like walking on marshmallows
[j7ilfng] (score 3, diepte 0) Definitely Oofos around the house!
[j7ilxyd] (score 3, diepte 0) Even those soled slippers from Costco are helpful for indoors. anything with a substantial thickness sole.
[j7imktd] (score 3, diepte 0) I love oofos and wear those exclusively, but prior to diagnosis when my feet felt like they were broken, I really liked the support of vionic. They're so stiff my toe joints wouldn't bend when walking which is what I needed. As I was treated and didn't have symptoms, I kind of switched to oofos which are just super cushy.
[j7j4os7] (score 3, diepte 0) Love my Hokas! I work in an orthotic clinic and swear by them.
[j7j4vxo] (score 3, diepte 0) Keen, Merrell, and Chaco.

Do you also have plantar fasciitis? I do, and these three shoe brands have never let me down.
[j7j69k7] (score 3, diepte 0) They got2 be adidas supercloud foam plus slides blak. N white. Marshmallows!!!
[j7kivx1] (score 3, diepte 0) Almost Anthony by Native shoes. The Jefferson is so comfortable and they look cool.
[j7idkvp] (score 2, diepte 1) CROCS!
[j7jb5vz] (score 2, diepte 1) Crocs are like wearable anti-fatigue mats, I have pair just for around the house
[j7h4fm9] (score 2, diepte 1 OP) I’m going to try these too!!  Doesn’t hurt to have several different pairs.
[j7ih60f] (score 2, diepte 1) I second this. I have some ugly AF Oofos that I wear at home. I wouldn’t wear them away from home but they are hella comfortable as house slippers.
[j7imc2z] (score 2, diepte 1) Third oofos. They are phenomenal
[j7h5tqw] (score 2, diepte 1) I also wear Teva sandals in the summer. They're amazing.
[j7ho4hs] (score 2, diepte 4) That makes sense. Have you looked into zipper assistive devices? I haven't personally used them, but I know people who love them.
[j7hw1jy] (score 2, diepte 5) That's a good suggestion. I haven't looked into them yet.
[j8ird8v] (score 2, diepte 3) Just seeing this but want to say thank you for the link… still coping with all of this and transitioning shoes has been impossible.  Everything I had before the diagnosis bruised my feet
[j8j2sbg] (score 2, diepte 4) No problem. I completely get that. I had a pair of winter boots that I loved, but wearing them longer than 30 minutes would cause pain for at least a day after wearing them.
I hope you are able to find something that works for you.
[j7ijiln] (score 2, diepte 1) I wear Merrell waterproof low trail hikers when I go for walks, hikes, and even when I bike ride around town on errands. They don't hurt my feet.
[j7khqxg] (score 2, diepte 1) Yep! I wear Merrill sneakers and Clark's unstructured line for nicer shoes.  Both fit my intense orthotics and provide balanced support that almost nothing else I've tried does.
[j7i6j1w] (score 2, diepte 0) If I can break in a pair of Dr Martens, then a pair of those! I have several older pairs I wear all the time. Otherwise, I wear Birkenstock sandals in the summer and Ugg boots in the winter.
[j7i8abq] (score 2, diepte 2) Okay, I hope something works! Foot pain is the worse pain out of all of this in my opinion. I did get some inserts from Amazon I’ll send the link as well incase you want to try them.
[j7i7rpy] (score 2, diepte 1) Oh no sneakers? Merrill and Tevas
[j7ig89p] (score 2, diepte 0) Kenkoh massaging sandals. I have tile floors and I wore Sketchers for a long time then I found these sandals. I love them! My feet haven’t hurt since I started wearing them.
[j7kk8u5] (score 2, diepte 0) Same as everyone who says crocs around the house. Then I have these thick-ish really contoured sandals I wear at home and out. They’re from target
[j7knunn] (score 2, diepte 0) Bronax bubble slides from Amazon have been a lifesaver for me. They have open or closed toe options and are so comfortable to wear in the house.
[j7ko0rg] (score 2, diepte 0) All I wear at home are Birkenstocks. Always. I wear new balance shoes at work only because I can’t wear my Birkenstocks.
[j7kqkvt] (score 2, diepte 0) Love my Hey Dudes! great shoes!
[j7kv26q] (score 2, diepte 0) Also OOfos sandals for around the house, and Altra walking shoes, they have a wide toe box for my bunion ![gif](emote|free_emotes_pack|feels_good_man)
[j7l2zq1] (score 2, diepte 0) Briekstocks soft foot bed. I own 8 pairs and wear them every single day
[j7l4bpd] (score 2, diepte 0) I will never go back to traditional shoes! I LOOOOOOOOVE my 5 finger Vibram shoes!! 

They have taken away so much of my pain. No more issues with gout! And I never say, "I can't wait to get these off of my feet." I wear them all day. Oh, and they strengthened my angel after spraining it twice.
[j7npedy] (score 2, diepte 1 OP) Looks like a glove for your foot- going to have to give them a try
[j7nrck1] (score 2, diepte 2) It's like walking in bare feet. Your ankles don't pronate the way you think they would without the arch support because there is no false sense of support. I'm able to hike with my dogs!!! They're glorious!
[j7laubg] (score 2, diepte 0) I wear a lot of slip ons and I find that Vans are the most comfortable.  For around the house I have the adidas memory foam slides that are pretty comfortable.
[j7mqinu] (score 2, diepte 0) I’m in the same boat and I have a pair of slip on SKECHERS that I got at Target and repurchased at Kohls and I love them. Memory foam in the bottom.
[j7n8qcv] (score 2, diepte 0) I wear Arcopedico shoes a lot. I especially like the ankle boots because they give me a little bit of ankle support. They use a soft material that molds to the foot and doesn't cause any rubbing or pressure anywhere. They also have styles in stretchy material that are good for feet that swell.
[j7pf15k] (score 2, diepte 0) Hoka Bondi wides and hoka recovery sandles
[j7hg2pj] (score 1, diepte 1) Was gonna say the same thing!
[j7infm8] (score 1, diepte 1) Yep. My tie dye crocs are on my feet right now. They are great house shoes.
[j7jjwea] (score 1, diepte 1) Came here to say this
[j7jw82y] (score 1, diepte 1) Me too
[j7h3smy] (score 1, diepte 1 OP) Thank you they look comfortable- I will give them a try
[j7lakg9] (score 1, diepte 1) Swear by these. I have an indoor and outdoor pair.
[j7iuexj] (score 1, diepte 6) I hope you are able to find something that helps. I am all for assistive devices. I use a shower chair because I get too fatigued standing the whole time and I have a cane for bad flair days.
[j7im2xk] (score 1, diepte 2) I wondered how well the trail hikers were. I actually started buying Merrell this summer at an outlet. I found a pair of their running shoes fairly cheap and took a chance. I'll never go back.
[j7lfxfy] (score 1, diepte 1) Second Sketchers. I have a pair that has extra arch support, love them. I want to try  Max Cushioning type next
[j7hq2vn] (score 1, diepte 0) Boots with good ankle support.
[j7i7wek] (score 1, diepte 1 OP) Ok I’m definitely trying them out-   

The ankle and foot area contains 26 bones, 33 joints and over 100 muscles so every time I try a new shoe another part of my foot hurts- and forget about the surface I’m walking or standing on.  

A friend recommended ON shoes and OMG I was in pain the next day-and it took forever to heal-
Pun intended but true
[j7i8o7u] (score 1, diepte 3 OP) Yes please-
[j7i7i9z] (score 1, diepte 0) This ! Yes Merrill’s after crocs, Danskos, Walmart, shoes for crews, sketchers, etc thousands I own a bakery and I will never ever buy anything else.
[j7igu9v] (score 1, diepte 1 OP) Oh they look comfy and I love the sole with all those things on it
[j7imzqi] (score 1, diepte 1 OP) That’s how my feet feel like I broke some bones in there.  I wore an On sneaker to go for groceries and have been paying the price ever since, especially in the morning.  Will be checking out your recommendations and all of them here thx
[j7ixxi0] (score 1, diepte 0) SAS running shoes.
[j7j31lv] (score 1, diepte 0) Crocs!
[j7janar] (score 1, diepte 0) It really depends on how bad I’m flaring on any other joints (for example my hands, as my grip strength is not the greatest during flares)

Flair Up/General wear - red slip on Vans
Not so flaired but still swollen - white lace up Vans
Not flared at all - Converses

Though not the greatest options, they’re all very comfortable! :)
[j7lamge] (score 1, diepte 0) Also, custom insoles saved me. Flat feet too
[j7ozz8i] (score 1, diepte 0) Oofos sandals, Birkenstocks, Dansko for my “dressy” shoes, Keen hikers and sandals, Altra sneakers.

=== THREAD rt6ep7 ===
SUBREDDIT: r/diabetes
DATUM: 2021-12-31  SCORE: 45  REACTIES: 72
TITEL: My feet!
POST (source_id=post):
Hello! I've had problems with (what feels like) nerve damage in my feet for several months now. I recently bought an at home blood sugar test and sent it into a lab for results and got 12% blood sugar (this is bad apparently). Ever since then I've been doing my best with what I call "internet diabetes dieting" cut out most sugar and carbs etc. Etc.

I'm currently in a waiting process for financial aid to see a doctor because I have no health insurance (7-14 business days during the holidays is taking a long time) 

My basic question is, does the feet pain/nerve damage/swelling ever heal if I can get this under control? (ofc I don't have a diagnosis, and I know asking for one is against the rules) I'm nervous that the time it took me to recognize the symptoms plus the time it's taking me to receive treatment is going to screw my feet over for life. I'm kind of scared. Hopefully I didn't break any rules, I'm just looking for some Hope for my future!

Edit: thanks for all the helpful advice! I'm done replying for tonight, here's to a bright healthy 2022 for everyone! Happy new year and bless you all for your words of encouragement

Edit 2: I'm taking you guys seriously. Woke up this morning feeling terrible and am currently in the ER awaiting results. Thank you

Edit 3: my blood sugar was 330. They gave me an insulin shot and a prescription for metformin, as well as all the information I need. I appreciate you guys, you all most likely saved my life

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hqqzl6w] (score 35, diepte 0) I had started encountering this right before my diagnosis. My a1 was at 11.2. Since then, I changed all my unhealthy eating habits, and essentially just started walking 30-60 min a day. My a1 is now consistently around 5.3, and all the symptoms that I was encountering went away. 

I know it's not the case for everyone, but you have to start making the changes that are going to give you the beat odds
[hqquy8f] (score 29, diepte 2) Okay, that's a measurement that makes sense! Unfortunately, if that is accurate then yes, you absolutely have diabetes. I would see a doctor as soon as you are able, eat as few carbs as you can, and if you vomit, then I would go to the ER immediately (because that could be an indicator that you are developing diabetic ketoacidosis, which can be fatal). 

Once you see your doctor, you'll get a bunch of lab work done that will likely include a test that indicates whether you have type 1 or type 2 diabetes.
[hqqu9pz] (score 27, diepte 0) I'm not sure what test you bought but "12% blood sugar" is not a measurement recognized by any medical people. What you can do today is purchase a meter and test strips, Walmart makes a few meters under their house brand ReliOn that are cheap. Test your blood sugar in the morning before you eat. That will give you a number you can tell your doctor when you see them. 

As for neuropathy pain, a person with diabetes who begins treating their diabetes appropriately will see some improvement, but there's no guaranteed cure.
[hqr3aaf] (score 24, diepte 3) With an A1c of 12 you might wanna go to an insta care asap and not wait for a doctor appointment
[hqquh4a] (score 16, diepte 1 OP) Sorry! I just looked at it again. It says hba1c was 12%
[hqqzsr0] (score 10, diepte 1 OP) Thanks! I love it, all of the encouragement is warm and makes me feel like I can make it!
[hqr9vpa] (score 9, diepte 4) When my blood sugar was 325 at routine bloodwork, my rheumatologist had me call my PCP immediately. It was 375 at that appointment, and they got me in with an endocrinologist 48 hours later. My a1c was 12.5 or 12.7, and I also had nerve tingles in my feet.

I say all of this to say, this was considered an emergency by my providers. I have really worked on my diet, and am on medication, and now my a1c is in the low 6 range.

My feet and calves are better, but if I eat poorly, I can feel it.

I miss real soda SO MUCH.
[hqqvs82] (score 6, diepte 3 OP) Thanks for the info!
[hqqyycw] (score 6, diepte 4) Hba1c 12 is NOK. U need to get medical attention. Get started with a treatment plan. Hba1c of 12 and numbness indicate u have had elevated blood sugar levels for months now.

In my country, general practitioners are able to do follow up of diabetes T2 with referrals to endo when needed. Advice you to start somewhere and immediately please. In the meanwhile watch what you eat and pick up exercise. It can be something as simple as a walk. It makes a huge difference to your general sugar levels. As far the foot issue  - in my 30 years of diabetic experience, I have had numbness disappear when my control improved ( my college days weren't my best years).But I have seen cases leading to amputation too. I don't want to scare the shit out of you. But 

1. Watch what you eat especially sugar and carbohydrate levels in every food.
2. Pick up any form of exercise immediately
3. Go to a doctor for a blood test and to get you started with a treatment plan. 

Good luck ! It is easily doable !
[hqr21vu] (score 6, diepte 0) Personally I have had neuropathy (pain from nerve damage from diabetes) symptoms come and go. I've been told neuropathy can't be cured, but my personal experience is that my symptoms are less as I have gotten my diabetes under better control. There are also medications that your doctor can prescribe to help manage the symptoms.

If you know what your insurance will be, you might be able to make an appointment with a doctor now, in advance, to happen after your insurance starts. See a doctor as soon as you can. In the meantime drink plenty of water and limit sugar, carbohydrates, and fat.
[hqs2mxf] (score 5, diepte 6) Have you tried Zevia? 
Some of their flavours are pretty good and I don’t find there’s the nasty stevia aftertaste that some products have. The ginger ale when sick really hits the spot!
[hqquyqy] (score 5, diepte 0) How can you describe this feet pain? I am having burning sensation on my feet for the past months. But no tingling or any actual “pain” is there. It just feels hot.
[hqqvg85] (score 5, diepte 1 OP) My left foot has patches of numbness along the lateral edge as well as parts of the top of the foot into  the ankle (maybe an inch or 2 above the foot) 

My right foot has constant (probably a month at least) fluid build up in the big toe and pointer toe next to it. 

The left foot is irritating when I'm trying to sleep and the right foot makes me walk slow and limp.
[hqr29v4] (score 5, diepte 2) 6.5 is considered diabetic, 5.5 is prediabetic. 12 is pretty high. Make sure when you get another blood test that they do a c-peptide test to see if you are type one or type 2. It will make a drastic difference in what you need to do going forward.
[hqr30i4] (score 5, diepte 2) hba1c shows what your blood sugar has been over the last 2-3 months, so testing a1c again before a couple of months have passed won't likely give you useful information on if your new habits are working.  A blood glucose meter shows a reading of what your blood sugar is at the moment of testing though (which is good because it gives you faster information, but can also show a higher/lower number because of short term factors).  

Good luck, and I hope that financial aid comes to you quickly and easily.
[hqr5ahc] (score 5, diepte 0) I'd say keep up with the carb cutting. With keto/carnivore eating my HbA1C is down to 4.8 and I'm currently unmedicated.
[hqqvp9g] (score 4, diepte 2) Hmm I never had any of these symptoms. I have an appointment with the doctor on 7th. I hope my burning sensation is just something else. And I hope yours isn’t a serious problem too!
[hqqvqzw] (score 4, diepte 3 OP) Thanks good luck m8
[hqqzmke] (score 4, diepte 5 OP) Thanks for all the info! I definitely need to exercise more. The lethargy and feet pain is the hardest hurdle to overcome in working out but it's been pointed out by many to be extremely beneficial
[hqr187r] (score 4, diepte 6) I state this by experience. It is a vicious cycle. To get ur energy levels up and have a cure for feet issues - please get up and walk.  It will make a world of difference. 45 - 60 mins every day can make a world of difference. It is not an eternal wait either. You will start to notice difference quickly too.  Consistency is all it takes. Good luck !!
[hqr1e8o] (score 4, diepte 7 OP) You are getting me pretty motivated!
[hqr2zmm] (score 4, diepte 8) Give it a shot. U have nothing to lose.

- decent food and 45 mins of walk at max pace u can do

U shud start seeing, feeling a difference I would cautiously say in 1 or 2 weeks. Please try!
[hqrgo79] (score 3, diepte 5) Aspartame gives me migraines.

I’m drinking specialty diet sodas with other sweeteners or just sparkling water, tea or coffee if I need some flavor. 

I miss real sodas too.
[hqs9ull] (score 3, diepte 2) I have nerve damage as well, from years of drinking. The diet is key to limiting those numb toes. I know eat salmon and asparagus 3x every week. In between that I’ll eat a grilled chicken salad. Also limit fruit intake. Eating 2 apples and a banana per day was causing me problems in my feet.

Basically write down all your meals and find what works best for you.

Happy New year.
[hqr0tyj] (score 3, diepte 1 OP) A1c 12 was nov 7th for reference. I've been cutting carbs and sugar drastically since, but have yet to test again. I feel like it's gotta be a bit better, but I honestly have no good frame of reference. (Another commenter told me about some Walmart test strips which I will be purchasing asap)

I wondered if the feet were entirely neuropathy related or if other health issues have arisen before/after.

Just shooting in the dark here, need to get that dr. appointment going.
[hqr29yy] (score 3, diepte 0) I can't speak for anyone else except for my twin brother (we are both type 2 diabetics). Yes, my feet were terrible as well and if you take out the sugar you will heal a lot more than just your feet. Also, eating the right things and boosting your B vitamins will help as well. We don't even take insulin or anything. We just eat a proper diet, and have been doing so for about a year and it's been amazing progress! So give it a shot definitely!!
[hqr2xcl] (score 3, diepte 0) In most cases nerve damage is permanent. You might see a minor amount of positive change but it wont ever heal.
[hqtgv55] (score 2, diepte 6) I’ve become grudgingly addicted to Sparkling Ice Grape Raspberry, and to a lesser degree, Cherry Limeaid. If I really want Pepsi-adjacent, Pepsi Zero is the closest I’ve found. I’ve tried all of the seltzer flavors and brands, and lots of different diet sodas. Disliked most of them, but diet Dr. Pepper and diet A&W root beer weren’t bad. I did all of my taste tests during the first Covid summer, so any of (basically almost all) of the bubbly drinks I didn’t like I’d put on the front porch and send out a neighborhood alert 😂
[hqs56vh] (score 2, diepte 2) Well you’ll have nerve damage at 12 for sure if you lived like that awhile. If you don’t make an immediate change you won’t have a foot.
[hqt1vm5] (score 2, diepte 6) And you do not have to push it when you first start the walking, go slow and then build up. Do what you can tolerate. Good luck.
[hqt1rce] (score 2, diepte 3) It is called neuropathy and quite common with Diabetes. Even burning is cause for concern. Good luck at the GP or endo visit.
[hqtaz9h] (score 2, diepte 4) Oh I’m concerned alright. Thank you for good wishes. I hope that this isn’t diabetes related neuropathy, even if it is, i hope this didn’t cause permanent damage to my feet because I detected it late or sometimes. Either way, no sleep for me until I learn what’s going on at 7th
[hqtg0m9] (score 2, diepte 5) Please get sleep for that no sleep can cause more problems. But great that you are being seen.
[hqtqc3t] (score 2, diepte 3) Also, getting your vitamin B12 level up is really important. A high vitamin B12 level is very helpful if you have neuropathy.
[hqr07jv] (score 2, diepte 0) Have T1. A1C of 12 is bad. Definitely cut carbs and increase cardio a bit by walking.

Foot pain is very common to gout as well consider being tested for it. Gout patients reduce joint and foot pain by reducing the fat in their diet.
[hqr7l49] (score 2, diepte 1 OP) I love meat! Care to elaborate on keto/carnivore eating?
[hqrf4ur] (score 2, diepte 1 OP) It's been almost 2 months of diet since I found out that # would you still recommend? I've considered ER at times of elevated pain but just figured the bills weren't worth it.
[hqrglkb] (score 2, diepte 2) > just figured the bills weren't worth it

The bills would suck but it's pretty cool to not get your feet amputated too.
[hqrfli4] (score 2, diepte 0) So I'm a Type 1 (insulin dependent).  

I have suffered massive levels of neuropathy in my feet as well as ulcers.  It does get better.  If you take care of your Blood Glucose (BG) and your feet/legs.  I had a full on diabetic ulcer heal in two months because I was a hawk on it.  I still have this black mark on my leg.  

Point is there is hope.  Get to the doc, get diagnosed.  And while I can't say if you are in my club or ....ahem....that other club....ahem.....  I'm pretty sure neither of us has agreed on the t-shirt design.  When we do I give you personal assurance membership cards shall be mailed.
[hqrrl1a] (score 2, diepte 2) Finger sticks are annoying, but you do get used to them pretty quick, and the upside of them saving your life or limbs is a pretty big one. And dont feel like being annoyed by anything related to diabetes is dumb. At the end of the day, this is an unfortunate disease to be stuck with, and even the little things can be really dang annoying sometimes. You are justified to feel that way about finger sticks, and you aren't alone in thinking that way about them either 💚
[hqscvwb] (score 2, diepte 0) Okay in the comments I saw a1c of 12. Dude go to the ER ... Your risking your life here. Even with a carb diet you could produce ketones which are highly dangerous. 

Man the us health care system sucks! So sorry for your situation
[hqs8hbc] (score 1, diepte 7) I’ve not given Zevia a try yet. Will pick some up at the grocery this weekend.

Thanks for the recommendation.
[hqs76rx] (score 1, diepte 6) Have you tried Virgil’s Zero? So good and soooooo much better than Zevia.  Like night and day better. No aspartame either. Really good. Find it at target. Haven’t found it anywhere else unfortunately.
[hqs8kzl] (score 1, diepte 7) They carry it at my local Meijer grocery. I’ll pick some up.

I wish someone made a solid root beer. I miss root beer. lol
[hqth7ak] (score 1, diepte 8) Virgil’s Zero indeed does make a root beer. I cant say it’s as spectacular as their regular cane sugar one but it’s pretty good.
[hqtihoc] (score 1, diepte 6) Thanks! I will get some exercises in, reduce or eliminate all sugar intake until I visit the doctor just in case
[hqu6l8d] (score 1, diepte 2) You can get finger pric testers for about $50 at a drug store or Walmart. You need to check the cost per strip though. That's where they get you. In my experience they range $0.30 to $1 each before insurance, I have a high deductible so I paid cash before I got my CGM Continuous glucose monitor. They might be cheap or free on insurance. Also if you have any older family members with type 2 they get the test strips through Medicare for free. Normally their prescription is way in excess of what they use so they may give you some.

&#x200B;

If you don't have insurance I would recommend just getting the tests done at Quest. Their app let's you log in and see your entire test history. I get a full blood panel every 90 days in addition to A1C they test for liver, lipids, cholesterol, etc. The results show you the healthy range too. Some times my cholesterol gets barely on the upper end due to high protein diet so I cut back a it. A doctor is very important and by far your best bet  but in a pintch a full blood panel is going to be your best second runner up. 

&#x200B;

If you are having foot pains also consider looking in to your local Master's swimming club at a community pool. This is low impact and shouldn't bother your feet as much (except using fins). They have 2x a day practices for $40-$60 a month. The coach breaks the simmers in to 3 groups based on skill, gives you exercises and critiques, etc. The gear is about $70 online (pull bouy, fins, hand paddles, goggles). I ended up doing quite a few triathlons after I was diagnosed, you meet really good supportive people in all the group cardio trainings. Road runners club is for running (duh I know) and your local bike shop probably has a group ride weekly. Pick your antidote (not poison).
[hqreaga] (score 1, diepte 2) I had a 12.6 HbA1C and decided to research what I could do about it which lead me to try "Atkins" diet which is a sort of modified Keto. I went further down the rabbit hole there and ended up eating a Keto diet for 7 years and now for the past 3 years a 95% carnivore diet which is meat (Lamb, Beef, Poultry), eggs, fish, dairy but I do have in season strawberries and I like a Greek Salad once or twice a month.    
Incidentally, my 12.6 reading was just after a 7 year stint as a vegan. Never go plant based. It's stupid :)
[hqr6qru] (score 1, diepte 0) Are you drinking and peeing a lot right now? If not, start drinking a lot of water ... like half gallon or more a day. Get on a treadmill and get some walking in.
[hqr7v7u] (score 1, diepte 1 OP) I've been inconsistently drinking as much water as I can manage. Somedays in excess of half a gallon, sometimes 1 bottle. More good advice thank you!
[hqre0fw] (score 1, diepte 0) The neuropathy in my feet gets so bad sometimes that I can't even sleep. I did get prescribed Pregabalin recently and that has helped a lot.
[hqre5se] (score 1, diepte 1 OP) I'm up late at night in pain with you I feel this ♥️♥️♥️
[hqreigc] (score 1, diepte 0) If you have anA1C of 12 you should go to the emergency room tonight.
[hqrgoh5] (score 1, diepte 3 OP) That's a pretty good point!
[hqrr4u1] (score 1, diepte 2) It also really, really depends on if your type 1 or 2. If type 1, diet changes and excercise may help some, but your blood sugars will still be, and this cannot be overstated enough, very, very dangerously high. If your type 2, diet and excercise will likely help out a pretty significant amount, but it isnt enough for everyone. Some type 2s require medication and insulin to get levels where they need to be. If you can test again and get another A1C test and your levels are doing better, you could *maybe* scrape by a little longer without the medical bill's (I dont know what your financial situation is like, but I really, really, really would not reccomend ignoring hospital visits unless you have no other choice) but you will need to go at some point. If you test and your levels are still high or only slightly better, you have to go to the hospital or wherever you can get medical care ASAP. Bill's won't matter if you aren't here to deal with them.
[hqrg0n1] (score 1, diepte 1 OP) Thanks! Great advice and a good positive story outcome! I doubt my financial assistance will cover the t-shirt though, I might have to fundraise :p
[hqrjh6z] (score 1, diepte 2) Ah tsk tsk.  The fundraising is for group t-shirts!  

Seriously though I'm not one to usually (I'm in US) tell someone get to the doc right now but your symptoms are classic.  Best of luck to you.
[hqrpvy0] (score 1, diepte 2) Hey if a design is ever agreed upon I got you covered  :) and good luck on starting the beetus journey, it's a hell of a time but it'll only get better from here, both for your mental health and your feet
(12 reacties met lagere score weggelaten)

