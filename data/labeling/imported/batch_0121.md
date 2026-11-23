# Label-batch batch_0121

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
Schrijf het resultaat naar `batch_0121.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: bxz8hf, 9836ow, o999l5, 4658lj).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD bxz8hf ===
SUBREDDIT: r/weddingplanning
DATUM: 2019-06-07  SCORE: 96  REACTIES: 28
TITEL: 15k Wedding Recap, Budget Breakdown & Pictures! Southwestern Ontario Restaurant Wedding, 60 Guests - May 4th, 2019
POST (source_id=post):
Yay we're married! Just over a month ago we had the best day of our lives! Weddit was my number one source of inspiration and support, and I can honestly say my day wouldn't have been what it was without you guys. I know this is going to be really long (it's turned into an actual novel), but I pride myself on my detail tracking and budgeting so if it helps one person, that's all that matters. I've included pictures along the way because my photographer is an angel and gave us all pictures back in one month, and links to vendors I was extremely happy with!

&nbsp;

**About us**: Late twenties professionals, renters, 23 month engagement. We've been together 5 years, and were engaged just after the 3 year mark. We live together on our own in the GTA with one dog child.

**Location**: An Italian restaurant in Windsor, Ontario (my hometown - about 4 hours from our home in the GTA). This venue had an event room above the main restaurant with a kitchen, bar & full bathrooms. We were able to do everything upstairs and all in one place - both the ceremony and reception.

**Date**: May 4th, 2019

**Guest Count**: 81 invited, 58 RSVP'd Yes, 57 attended (one person couldn't make it as his SO ended up in the hospital). I did an in-depth RSVP breakdown in another post [HERE](https://old.reddit.com/r/weddingplanning/comments/b2xxfz/rsvp_breakdown_small_restaurant_wedding_in/?ref=share&ref_source=link), if you want to take a peek.

**General Timeline/Vibe**: Morning set-up, get ready, first look & all posed photos 3-4:30pm, 5pm ceremony, 30 min cocktail hour, sit down plated dinner, dancing. Very easy going, I wanted to make it a priority to enjoy my own wedding, spend time with guests, eat and drink. 

&nbsp;

[**PICTURES FIRST OF COURSE!!**](https://imgur.com/a/4ofU0Eq)

&nbsp;

**Budget Notes**: 

* We had initially begun the wedding planning with a goal of keeping it under $10k CAD - we live in a very HCOL area, and with student loans and other debt, we wanted to keep it as low as possible. As we got deep into planning, and discovered things we didn't want to compromise on, the final budget came out to somewhere around the $14k CAD range.

* We are extremely lucky that my parents are very well off, and offered to pay for a large majority of the wedding. We honestly couldn't have had the wedding we did without their support.

* I made it a point to research as much as possible to make sure we were getting the best vendors we could within our budget (vision, aesthetic, personality).

* All of the prices reflected below are in Canadian dollars


&nbsp;

**Final Total: $15,711.09** (~$11.8k USD)


&nbsp;
    **Venue: $560.00**
    
* Rental Fee: $500

     - We had less than their ideal amount of 75 guests, so they did charge us a room fee. Had we bumped the guest list, the venue would have been FREE.
* Ivory napkins: $60

 - They provided black napkins for free, but I was willing to shell out the $60 for ivory napkins to better match the decor and aestheic.

&nbsp;
    **Food & Beverage: $5,918.47**

*  Food: $2,622.41 (incl. tax & gratuity)
   
 - 4-course meal which included Bruschetta, Antipasto, Salad & Main (Chicken, Salmon or Vegetarian).

 - The food was ABSOLUTELY AMAZING. This was one of the places I was not willing to compromise too much. I was adamant I did not want a buffet or family style and I wanted something different than the usual "chicken, pasta & vegetables" that shows up at most banquet hall weddings. This is the reason we went with a restaurant and not a hall.
 - I ate to much and could barely breathe in my dress lol

* Bar: $2,978.71 (incl. tax & gratuity)
 - Full open bar with a prosecco toast before dinner (with my parents' speech)
 - This ended up being more than I had budgeted, but everyone had a great time.

* Dessert: $317.35 (incl. tax)
 - We ended up choosing [Riverside Pie Cafe] (https://www.riversidepiecafe.com/) to do our dessert table and we don't regret it one bit
 - They baked everything fresh the morning of the wedding and delivered it to the venue for free
 - We ended up ordering 126 servings of pie (made up of 1 full size apple pie for cutting, a variety of tarts - pecan, apple, lemon and strawberry-rhubarb, as well as raspberry danishes and walnut brownies)
 - Almost everything was eaten, and I literally had one bit of the pie we cut, and one bit of lemon tart - I regret eating so much at dinner because I was too full to enjoy the dessert!

&nbsp;
    **Attire: $2,216.50**

* Dress & Alterations: $1,422.10
 - My dress was Mori Lee by Madeline Gardiner style 5276 ($1,322.10) and I felt like an absolute princess.
 - Alterations were done by a nice older lady who came recommended by my mom's friend & boss. She only charged me $100 for hemming the EIGHT layers of my dress, taking in the bust, and added a simple loop bustle. I was shocked when she only asked for $100.

* Bride's Accessories: $151.45
 - I got a simple single layer cathedral veil from Amazon ($14.62) and it was perfect.
 - My jewellery was from Jon Richard Jewellery ($72.61) - my parents happened to be in the UK and I asked them to pick up a hair comb and earrings while they were there as this is a British company.
 - I chose to go with flats for my wedding shoes as I knew I would be uncomfortable in heels and would likely take them off sooner than later anyways. I didn't want to hem my dress to heel height and then be tripping over the dress when I took them off, so I chose to stick with flats and hemmed the dress to my height (5' 4"). I went with rose gold t-strap flats from Mod Cloth ($64.22)

* Groom's Attire: $642.95
 - My Husband could not decide on a suit for the longest time. He initially wanted blue, then dark green, then burgundy.. He also thought about getting something custom made, but ultimately decided it wasn't worth the cost as he only wears a suit maybe once a year. He found it difficult to find anything he liked in a colour that he liked for months on end - but finally decided on a blue tuxedo from Simon's ($367.25) which included free hemming of his pants.
 - Shoes from Steve Madden ($135.60)
 - Shirt from Moore's, Bowtie & Suspenders from Le Chateau, Cufflinks from Simon's ($140.10)

&nbsp;
    **Rings: $762.15**

* Bride's: $454.25
 - 14k rose gold & diamond band

* Groom's: $454.25
  - 10k rose gold 5mm comfort fit band

* This is one of the places where we regret the vendor. We went with an independent, local jeweller and we had a fantastic inital purchase. But the customer service in the following visits and months was appalling. We purchased warranties with each ring but really don't feel comfortable using them again and trusting the store with our rings - super unfortunate and a waste of money for the warranty.

&nbsp;
    **Hair & Makeup: $215.00**

* I used this makeup artist for my engagement shoot, and rehired her for the wedding.
* She recommended a hair stylist and I went forward to book her as well.
* They both came to my parent's house on the day of the wedding with assistants, and took amazing care of everyone getting their hair and makeup done.
* I didn't require anyone to have either done, and everyone paid their own share


&nbsp;
    **Photographer: $2,150.00**

* 6 hours shooting time, 2 photographers, engagement shoot, USB with all edited photos and a glass presentation box with a few prints
* One of our favourite vendors throughout this whole process - she was our age and we just vibed with her so well
* We got 15 sneak peek pictures within a week of the wedding and the full gallery of 656 photos a month later!
* If anyone is in that area I HIGHLY recommend her: [Jessica Ruxton Photography] (http://www.jessicaruxtonphotography.com/)

&nbsp;
    **Invitations & Paper: $297.53**

* We are huge supporters of Vistaprint and have been using them for years without issue. This time was no different and we are extremely happy with the results.
* I waited for a good discount day and was able to get 50% off of our invitation suites (invite, rsvp & detail cards, envelope seals) for $96.00 (50 sets)
* Even though I love Vistaprint, I am not in love with the thickness of their envelopes, so I ordered cream A7 envelopes and pink A2 envelopes from Paper Garden ($58.75) - worth the upgrade for wedding invites in my opinion
* Vellum for belly bands: $12.31
* In addition to invites, we also ordered menus (60) and little thank you cards (100) for each setting from Vistaprint ($56.57) with a 30% off coupon
* Postage ended up costing us $73.90

&nbsp;
    **Florals: $1,184.24**


* I was initially going to do all the flowers myself using a combination of Costco and bulk online florists, but over the months of planning I decided it would be too stressful for me and too much work (I have ZERO experience flower arranging) in the few days before the wedding
* This is a case of "ask your dream vendor for a quote, even if their website says wedding start at double your budget". I had stalked this florist for YEARS before I even got engaged, and thought she would be out of my budget
 - I reached out to her (and a few other florists) and was surprised at the price she was quoting me - she was actually the lowest quote I got back - huzzah! She was an absolute gem to work with - even after having a baby only a month before my wedding! [Stefanie at Bourbon Rose Floral Design] (https://www.thebourbonrose.com/)
* I went with super simple greenery runners, white florals for the bouquets and some accent greenery throughout the space
* All in all, here's how the cost broke down:
 - Bride's bouquet: $175.00
 - Bridesmaid's bouquet: $85.00
 - Corsages (2) and boutonnieres (2): $120.00
 - Reception decor (ceremony arch, welcome/dessert table greenery): $138.00
 - Guest table greenery runners (8): $480.00
 - Delivery & Tax: $186.24

&nbsp;
    **Officiant & License: $515.00**

* We reached out to a group of officiants and was put in contact with one who was available, had a Skype call with him as we live in the GTA, and went over the general timeline and how he works
* Along with his services, we also had access to a website that provided help in writing a ceremony with all potential elements (both religious and non). I worked through the website, choosing bits and pieces I liked in the months leading up to the wedding, and met up with him a few days prior to the wedding to go over it
* Officiant fee: $375.00
* Marriage License: $140.00

&nbsp;
    **Weekend Accommodations: $327.41**

* I booked us a whole house AirBnb from the Friday night before the wedding until Monday morning (3 nights).
* It was a 10 minute walk from the venue and a perfect place for us to have a little time alone
* My husband also used this as his place to get ready on the day of the wedding and it ended up being great for photos

&nbsp;
    **Decorations & Misc: $1,031.38**

* I tried to do most things DIY if I could, which is why this number is so large. But I also put things into my fuck it bucket a lot in this category lol
* This number is made of a bunch of things - especially because I didn't rent anything and made it if I could. I mentioned a few things that I am really proud of below:
 - Seating chart and table numbers I made out of acrylic from the hardware store
 - Placecards (and pie signs) were little acrylic hexagons I got from Amazon [here] (https://www.amazon.ca/UNIQOOO-Count-Clear-Acrylic-Escort/dp/B076SXBBDX/ref=sr_1_1?keywords=hexagon&qid=1559933167&s=gateway&sr=8-1&srs=10526160011)
 - I was adamant I wanted rose gold or copper charger plates but I wasn't willing to rent them for $3-5 per plate, so I ended up buying white chargers from Dollar Tree for $1.25 each, and spray painting them with copper rose spray paint. This one was definitely a labour of love and I am really happy with the end result
 - I made the ceremony arch out of copper pipe from Home Depot, plus a set of curtains from IKEA
 - I spent a lot of time scouring Facebook Marketplace for things, and ended up getting about 1/2 of the candles and holders we used from there - this saved us a lot of money. The other half of the candles were bought at Yummi Candles or IKEA
 - Also from Facebook Marketplace, I bought a dark globe which we used as our guestbook - people signed with gold sharpies. I'm glad I have something we can display in our home!


&nbsp;
    **Favours & Gifts: $533.41**

* Instead of favours, we just did a donation to the local humane society. We adopted our dog from there and as we couldn't have our puppy with us at the actual wedding, it was a nice way to think of him. We did manage to take pictures with him before the ceremony though, which we were so happy with!
* Everything else in this category is gifts for our parents, Maid of Honour, Best Woman, and two friends who helped us out immensely.

 &nbsp;

**What Went Wrong:**

* Almost nothing.
* I kind of regret not doing the "invisible handcuff" thing with my husband. I found we were separated for quite some time - either talking to people we hadn't seen in years, or getting air outside at different times..
* The music and dancing were not what I had envisioned.
 - I used Spotify on an iPad and the venue provided speaker system.
 - Spotify was great and we had a great time, but some guests kept changing the music by themselves and ruining the flow of songs that I had worked for MONTHS on, which to this day still kind of irks me.
 - Not as many people as I had expected got up to dance as much - but that didn't stop me lol

**What Went Right:**

* Almost everything. Really.
* Weather was great - it was raining a few days before, but was beautiful on the day and I was able to keep my plans for outdoor photos before the ceremony
* Food and drinks were fantastic. Ate too much Italian food.
* We had everyone there that we wanted aside from a few family members overseas.
* I married my best friend.

Now that I've literally written more than a lot of my college papers, hopefully this helps or inspires someone else in the journey of wedding planning. Yay!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[eqb4ll5] (score 10, diepte 0) You two are an adorable couple! Thanks for taking the time to do the breakdown. I too am doing a small (50ish) people wedding and thought I could do it for 10k but the budget is pretty much coming in at 14k. I'm in the GTA and just had to accept things cost more here (and I refuse to compromise on things like food and photographer). I'm feeling better about my budget now!
[eqb0v4l] (score 6, diepte 0) Beautiful! Your pictures are so lovely! Thanks for sharing! It's nice to see a local wedding (I'm in Toronto, but Windsor is also my hometown and I'm getting married in Chatham)!
[eqbari3] (score 5, diepte 0) Congratulations! We share the same hometown! It was so bizarre for me to see this post here. Thanks for sharing and really glad that everything went wonderfully for you.
[eqawlzq] (score 3, diepte 0) Amazing recap and beautiful wedding. Congratulations!
[eqbflyx] (score 3, diepte 1 OP) Thank you so much!! Hope your wedding is amazing!
[eqbfqvr] (score 3, diepte 1 OP) Thank you!! I’m glad I could help :)
[eqbfxrg] (score 3, diepte 1 OP) Thank you! Yeah I don’t see too many Windsor or southwestern Ontario posts lol
[eqbe2v3] (score 3, diepte 0) Can I get the info for your seamstress? I live in London Ontario but totally willing to do the drive if shes good and not as expensive!
[eqbowqh] (score 3, diepte 0) Beautiful! Where did you get your welcome sign?
[eqbcu8m] (score 2, diepte 0) Amazing recap! I cannot believe your flowers were that expensive, but I can't believe floral prices in general. You look beautiful!
[eqbgf5o] (score 2, diepte 0) Amazing recap and I loved reading about this chapter in your lives :)
[eqbrgy4] (score 2, diepte 0) Honest to god as I was reading your recap I kept thinking to myself .. “was this my wedding”?! Because there were so many things that we did similarly to yours and things that went similarly wrong at our wedding, like the Spotify playlists! I could definitely relate hard to your wedding lol. Your day looked absolutely beautiful though and those desserts sounded downright amazing. Congratulations!! ☺️
[eqh03e6] (score 2, diepte 0) So jealous of your AirBnB costs lol. We rented a whole house for 3 nights as well, but in Toronto area and it was $1400. I don't regret it at all, but I'm amazed you got a house for a weekend that cheap.
[eqj69ye] (score 2, diepte 0) Your wedding is so amazing!!! I live in the GTA too and was wondering where you wound up getting your dress?? :D
[eqjdpru] (score 2, diepte 2) That’s amazing!! I’ll definitely look them up - I don’t live too far from there! Thank you so much :) Do you happen to remember if they had a decent plus size selection, and if they had a decent selection of under-$2000 dresses? :) Those are my two stipulations and I don’t want to bother going to stores that don’t fit into those two categories!
[eqbfgnj] (score 1, diepte 1 OP) Thank you so much!
[eqmryaf] (score 1, diepte 1 OP) Thank you! 

Yes, florals can get really pricey.. but it was worth it for me to not have the hassle of doing it myself and I completely trusted her to make things look beautiful.
[eqmra9n] (score 1, diepte 1 OP) Absolutely! I’ll PM you :)
[eqmr78q] (score 1, diepte 1 OP) Thank you!!
[eqmr5op] (score 1, diepte 1 OP) Thank you! My very talented brother made the base and I wrote on it :)
[eqjbq42] (score 1, diepte 1 OP) Thank you so much!! I had the best day :)
[eqjbmls] (score 1, diepte 1 OP) Yes we got super lucky with that one.. the whole house was renting for less than two nights in a hotel room!
[eqjb6nn] (score 1, diepte 1 OP) I got it at Avenue 22 on Dufferin just north of Eglinton. They were super nice and let me browse the whole store basically. Definitely recommend!
[eqmt0bm] (score 1, diepte 3 OP) I didn’t specifically go looking for plus size dresses, but I am no where near the sample size in stores. The sales people are great at clipping you in and helping you see what the dress will look like in your size. I think the sample I tried on was a 12, and I ended up ordering an 18? Bridal sizes are whack lol. If I remember correctly they do have a section of the store with plus size dresses.. so I think you should be fine.

As for the under $2000 dresses - absolutely. They have a wide range and the sales people were aware of my budget (1500) and didn’t make me feel like it wasn’t enough. Mori Lee, the designer of my dress, has beautiful stuff on the lower end. Mine was only $1175 before tax!
[eqn9mla] (score 1, diepte 4) Oh, this is so so perfect. I think I’m honestly around your size or perhaps a bit larger, and $1500 is also my budget. I was starting to get anxious that I wouldn’t be able to get a bridal salon experience at my size and for that price. I’m definitely going to add this shop to my list! You’ve really helped me. :) Thank you so much!!!
[eqnwpks] (score 1, diepte 5 OP) You're so welcome!!
[eqnzf8l] (score 1, diepte 6) Also, sorry, another question - is your seamstress in the Toronto area or the Windsor area??
[eqo0fbq] (score 1, diepte 7 OP) The seamstress was in Windsor - just a friend of a friend really. But she did a fine job and was super sweet (and cheap) lol
[k9lnce5] (score 1, diepte 0) Did you do the ceremony and reception at the restaurant?

=== THREAD 9836ow ===
SUBREDDIT: r/rheumatoid
DATUM: 2018-08-17  SCORE: 22  REACTIES: 26
TITEL: Products for staying comfortable
POST (source_id=post):
I thought it might be useful to share some products that have helped me stay comfortable while battling this current flare. Please feel free to add your own! I am very interested in knowing what you find soothing.

[Koo-Care Ice Wrap](https://www.amazon.com/gp/product/B01G7AEAEI/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1) – This ice wrap has straps and is particularly good for backs, shoulders, and knees. 

[Sunbeam Neck and Shoulder Heating Pad](https://www.amazon.com/Sunbeam-Microplush-Shoulder-Settings-Magnetic/dp/B001JCXJTW/ref=sr_1_7_a_it?ie=UTF8&qid=1534518147&sr=8-7&keywords=neck+heating+pad) – Really great if you get a lot of shoulder pain.

[Trtl Pillow](https://www.amazon.com/gp/product/B00LB7REE6/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1) – Designed as a travel pillow, but it is really awesome if (like me) you are prone to falling asleep while sitting up. Definitely less neck pain when I use it.

[Radiant Saunas Portable Sauna](https://www.amazon.com/gp/product/B01LEJACSK/ref=oh_aui_detailpage_o08_s00?ie=UTF8&psc=1) – If heat helps you, I have found this to be a reliable portable sauna. It goes up to 150F. I sit for 45 minutes and find it very soothing, though it does make me a little tired.

[Ivation Foot Spa](https://www.amazon.com/gp/product/B01K371X28/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1) – Foot spas seem to have reviews that are all over the place, so I took a gamble on this one and really like it. It has bubbles, heat, a massage function, and infrared light. If you have toe joint issues, it’s helpful. I also like that it has a big, sturdy handle for carrying.

[OPTP Franklin Fascia Massager Peanut](https://www.amazon.com/OPTP-Franklin-Fascia-Massager-Peanut/dp/B00O5PE8EU/ref=sr_1_1_a_it?ie=UTF8&qid=1534518544&sr=8-1&keywords=spikey+peanut) – My therapeutic/chair yoga teacher recommended this to me after we used it in class. I use it to roll out the bottoms of my feet and it helps to stretch them and improve sensation, which ultimately makes standing and walking more comfortable. If you have sensitive feet, a tennis ball might be better.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[e4dnmnm] (score 5, diepte 0) I’m saving this list, thanks! The only thing I can think of to add is Aspercreme with Liodcaine. It’s the only topical that’s ever done anything for me. I’m sure it’s mostly the lidocaine.
[e4dnj6p] (score 4, diepte 1) I’ve been struggling with swollen feet and toes during the recent flare. After much searching for shoes that were comfy but not grannyish (I’m 26) I settled on the oldie but goodie-birkenstocks (with a strap round the back so I didn’t hurt my toes keeping the flip-flop type on)

I wear them every day and they’re really supportive and comfortable. I can definitely notice a difference in terms of my mobility (knees are bad too) when wearing these compared to more flat footbed shoes

Hope the flare calms down soon
[e4d40xj] (score 3, diepte 0) is there any comfortable shoes out there?

would love some recommendation. my ankles are getting worse. thanks!!
[e4dc1iz] (score 3, diepte 1) [https://www.oofos.com/](https://www.oofos.com/)  Oofos makes what they call "recovery footwear"  I got a pair and they are probably the most comfortable flip flops I have ever worn.  My wife swears by their shoes.  Think of them as crocs for grown ups.
[e4df0ym] (score 3, diepte 1) I can not recommend these enough, every pair is so comfortable right off the bat and my feet no longer hurt and no bunions. If you have a Dillard’s nearby they carry them so you can try them on in store and see if you like them. 

https://www.dansko.com

Having said that, I do not recommend Fit flop. I bought 3 pairs and all off them started falling apart within wearing them literally less than 10 times. What a waste of money.
[e4dniqb] (score 3, diepte 1) I’m loving my new Alegria shoes. The styling is a little fun & funky, which works for me, but might not for everyone. They’re also not cheap, but look like they’re really well made, I’m sure they last forever. And holy cow, on days when my feet/ankles are unhappy, they’re the *best.* Lightweight, too. 

https://alegriashoes.com
[e4dow2j] (score 3, diepte 1) Loving my Obeo shoes. So comfortable and lots of room for swollen toes.
[e4df3ux] (score 3, diepte 0) This is a great list OP.
[e4dpjb4] (score 3, diepte 0) Not quite what eases pain but I love this product for making opening jars, tubes, dials, etc. 
http://www.andreastrivets.com/ 
Silicone jar openers make my life in the kitchen so much easier. Works great for washing machine dials too.
[e4f8kse] (score 2, diepte 1) When my feet were really inflamed the only shoes i could wear were these by Propét. They're made of really stretchable material on the top and it doesn't hurt your foot. Yet they also strap on effectively. Sorry for the ugly URL: https://www.propetusa.com/pc_product_detail.asp?key=CF08F932BAA84C5C8512CECA409DB330
[e4dkx8w] (score 2, diepte 0) The sunbeam heating pad is my go to!
[e4dvbeg] (score 2, diepte 1 OP) Aspercreme makes really good lidocaine patches too. A lot of my pain manifests in back and hips, so they are a lifesaver.
[e4dvge8] (score 2, diepte 1 OP) Oh thanks for this! I use my silicone pot holders to open jars for the same reason.
[e4dx2xz] (score 2, diepte 2) Oh i bet! Im always trying to ice my wrists or hands and I'm constantly trying to take turns with each side.  This will make it way easier!
[e4dz7u4] (score 2, diepte 0) I'm going to try some of these for sure!
[e4ltuvn] (score 2, diepte 0) Salts for a nice bath. Fuzzy socks for aching feet. A cushy recliner. A heated blanket.
[e4gg5nr] (score 1, diepte 2) Thank you! I'll check if they ship to China (Chinese here).
[e4gg8d2] (score 1, diepte 2) Thank you!
[e4gg997] (score 1, diepte 2) Thank you! They look cute :)
[e4gg43s] (score 1, diepte 2) Thank you for your recommendation!
[e4gga61] (score 1, diepte 2) Thank you!
[e4ggb4v] (score 1, diepte 2) Thank you! They look fine!
[e4dvehm] (score 1, diepte 1 OP) I love mine. I originally got it when I had a shoulder impingement to soothe the pain from that and ended up liking it so much I'd just use it to relax.
[e4e1hqy] (score 1, diepte 2) Ooh, that’s good to know, I get hip pain & I’ve got a long flight coming up. Thanks!
[e4dw1gz] (score 1, diepte 0) I can't wait to try those ice wraps - thank you!
[e4dx09n] (score 1, diepte 1 OP) You are welcome! So much easier than ice packs when you want to move around.

=== THREAD o999l5 ===
SUBREDDIT: r/rheumatoid
DATUM: 2021-06-28  SCORE: 5  REACTIES: 25
TITEL: Copper compression gloves?
POST (source_id=post):
Yes or no? I am desperate for some relief as my hands have been especially bad. Thumbs in particular are really not great..wrists too. My fine motor skills are shot because of this and I do a lot of typing and other work involving hands.
Advice?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[h39pvg9] (score 10, diepte 0) The copper is just a marketing gimmick. I think most people here recommend the IMAK gloves.
[h3bqn5d] (score 5, diepte 3 OP) Good to know! I ordered a pair, hopefully they work for me too. Thank you!
[h39vb2b] (score 4, diepte 1 OP) I will look into it, I have nonidea what the IMAK are. Thank you for your comment!
[h3bplwg] (score 4, diepte 2) IMAK is a brand that, at least in the USA, are readily available and affordable. I bought two sizes (medium and large in my case) of compression gloves depending on the severity of my symptoms. I’ve thrown them in the washer and air-dryed a few times (though of course handwashing is probably better) and they held up great.
[h39ylni] (score 4, diepte 0) I got copper ones soley because in the mid range quality gloves they didn't cost anything extra and had the best reviews
[h3a0cjt] (score 4, diepte 0) I have used compressive cotton gloves and they helps a lot
https://www.amazon.com/ComfyBrace/b/ref=bl_dp_s_mw_20047769011?ie=UTF8&node=20047769011&field-lbr_brands_browse-bin=ComfyBrace
[h3awmwx] (score 4, diepte 0) I tried some and they were no good. Just basic cotton compression gloves were much more effective.
[h39zaks] (score 3, diepte 2) They definitely help. The particular ones I got show unavailable now. I also found that during bad flares, switching to a vertical mouse also helps to relieve a lot of strain

https://www.amazon.com/dp/B07T4V83T9?ref=ppx_pop_mob_ap_share

https://www.amazon.com/dp/B07G4ZBW9H/ref=cm_sw_r_cp_apap_6jBbwvI4eWQQN
[h3b3wpi] (score 3, diepte 4) Not as much as you would think, it's still mostly normal mouse movements and clicks
[h3b7ns3] (score 3, diepte 0) I love my compression gloves - I have thermoskin gloves which double as heat therapy and are really most excellent in the winter. I write so typing is one of the most important things for me to be able to do and these are excellent on bad hands days.

side note: I was complaining about my thumbs the most in my rheumy appts and the usual meds weren't working but he added a med for fibromyalgia and I found a good bit of relief. It's not perfect but really, what is?
[h3bhorx] (score 3, diepte 2) low dose nortriptyline. I'm on mtx & xeljanz for ra, vitamins for certain deficiencies, and cbd oil for sleep also.
[h39yy22] (score 2, diepte 1 OP) What kind did you get? Did they help?
[h3a5h3x] (score 2, diepte 3 OP) That is a great advice! Thank you! Did it take a long time to get used to the vertical mouse?
[h3a5ich] (score 2, diepte 1 OP) Thank you, will buy a pair to try them.
[h3b8uyz] (score 2, diepte 1 OP) Thank you!!! What was the med, just curious 🤔
[h3buqnk] (score 2, diepte 2) My med for fibro is an anti-depressant. I had already been taking it and my doc just increased the dose. Seems to be helpful. It's called Duoloxetine. 


You could also ask for Gabapentin, which helps a lot of people (weird, for me, it makes me feel like I've drank 2 gallons of coffee, but for almost everyone else, it makes them sleepy). It's typically prescribed for nerve pain.


In regards to your post, the copper compression gloves never felt any different to me than the usual cotton ones. 

Good luck, OP. I hope you feel better soon!! Xx
[h3bv49z] (score 2, diepte 3 OP) Thank you foe the detailed answer! I will look into those.
[h3c0jgv] (score 2, diepte 0) Try Voltaren cream. Also talk to your prescriber since your current medication regimen isn't managing your symptoms.
[h3cf8a9] (score 2, diepte 2) My MIL has osteoarthritis and says the thin neoprene compression gloves help her.
[h3cibry] (score 2, diepte 0) Recent research shows that that compression gloves make no difference, but gloves do help if your pain responds well to warmth.

The sub won't let me link to the video in the National Rheumatoid Arthritis Society Facebook page but if you search for NRAS on FB you should find the video on their page detailing the full research.
[h3cj1no] (score 2, diepte 1 OP) That is very useful! Thank you! I use only heating pads, I have Sjorgen's and cold is horrible.
[h3cjgum] (score 2, diepte 2) I do have some fingerless compression gloves that I bought years ago and the warmth does help but maybe don't spend money on more expensive 'specialist' gloves. In the future I would probably buy Merino wool gloves instead.
[h3cto4e] (score 2, diepte 0) I tried to use things like compression gloves and splints for my wrists - that's where I experience the worst of my joint pain. Doesn't help a single iota. However, I think anything is worth a try if it might help. Some people find relief that way, others don't. I'd still give it a try to see if it works for you.
[h3cymrj] (score 2, diepte 0) Copper infused stuff is just a gimmick.. I found fingerless gloves where just the thumb has a hole and the rest of the fingers open to like.. a mitten hole really help take my mind off it
[h3c1prz] (score 1, diepte 1 OP) I am just starting on HCQ and my doctor says did takes 3 months to kick in and see a relief. I started it at the beginning of thebyera but had to stop it temporarily,  never reached 3 consecutive months. I am hoping it will kick in soon. Thank you!
[p4qzq2f] (score 1, diepte 0) Copper compression gloves and cotton gloves help reduce pressure.
[lfhtcs4] (score 0, diepte 3) Carpel Tunnel Solution Mouse QuadraClicks RBT

[https://www.quadraclicks.com/](https://www.quadraclicks.com/) Check it out on Amazon.

=== THREAD 4658lj ===
SUBREDDIT: r/rheumatoid
DATUM: 2016-02-16  SCORE: 2  REACTIES: 25
TITEL: Dealing with RA as an art student--do any other hand-workers out there use compression gloves or have any home remedies for hand pain?
POST (source_id=post):
Hi guys, new to this sub and relatively new to RA. 

I am in my early twenties and have had a Raynaud's dx since I was 15, which I always questioned because cold wasn't really why my hands ever hurt, it seemed kind of random and sporadic and happened even in the warmer months. well, 7 years later and the pain remained somewhat mild until the last year when my hand pain grew to moderate then unbearable pretty suddenly. finally got some bloodwork done with my GP and got dx'd with rheumatoid arthritis and put on meloxicam, 15 mg a day for the last month but not helping at all. I would like to see a rheumatologist but it's not affordable at the moment for me unfortunately, I wasn't even able to see my doctor when my blood work came back, we discussed it over the phone. but I should be able to see a rheumatologist in a few months. however until then....

as an art student, long days of classes combined with hours of outside studio work leaves me crying myself to sleep most nights, which is when I'm actually most prone to flareups--hands go bright red, itch like crazy, can't even feel them. my hands are my life, and I need them almost every minute of the day. I've tried Copper compression gloves, but that specific brand was too large on me (size small) and didn't provide any relief at all. I hate trying a bunch of things from google searches to see if they work so I was just wondering if anyone out here who does a lot of hand-work and feels my struggle has any advice to give on things that have actually worked for them :)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d02kauz] (score 8, diepte 0) You need to get in to see a rheumatologist as soon as you possibly can. RA can cause permanent damage to your joints, including erosions in the bone.

Steroids -- prednisone -- help the most but come with some heavy duty side effects. Your doctor can prescribe a medrol pack. Sometimes that's enough to tame back a flare.

Isotoner makes some good compression gloves. That's what I use. I also use alot of heat and ice. But I've had to cut back substantially on how much I use my hands. I'm trying to save the mobility that I have left.

When the disease starts to get you down, remind yourself that one of the greatest artist of all times  lived with RA -- Pierre-Auguste Renoir. He's not the only one, either. Alexej von Jawlensky also had the disease. Just food for thought.
[d02khsz] (score 3, diepte 0) I have decades of experience as an artist, but only a few years with RA. You haven't been really specific about which activities cause you the most pain, so I'll be sort of general. I haven't needed compression gloves yet, but I have been modifying my tools to make them more comfortable to use. Spongy handles, changing the angle I work at to preserve my wrists, pacing myself when it comes to long periods of single activities. That's not easy to do when you're in school and obliged to work in class. Some of the active hand tasks I've upgraded to using more power tools, less me power (because fatigue).  
If it's about gripping drawing implements or brushes, consider splinting, and if it helps to save energy or hand strength, think about making something that mounts pencil, brush, whatever, so you don't have to hold it tightly. Padding a tool, or making a finger harness for your forefinger to hold conte crayons... it would take practice, but if it provides long term relief and preserves functionality it might be worth it.
I'm not writing off gloves, at all. I just haven't tried them. I do hear good things though, and they are on my shopping list!
[d02kr6c] (score 3, diepte 1) Seconding padding your handles and finding/modding tools with comfortable grips. Makes a big difference, and with the right setup you don't lose your ability to do fine detail.
[d02n2oy] (score 3, diepte 0) Meloxicam is the only medication she put you on? You have to see a doctor and probably a new one... that won't do anything but help with the pain. You need a DMARD asap like methotrexate or plaquenil. The usual course is a 2 week high dose steroid taper at the same time you start a DMARD and you can work in any of the other periphery medications like meloxicam.
[d02p0l3] (score 2, diepte 1) Agree re seeing an RA doc asap. The single most important key to remission and reducing damage is early diagnosis and early meds that work

U/jhn107 is wise - they have it covered for you!
[d034qwy] (score 2, diepte 2) To be honest, your doctor had no way of telling whether your disease was mild or not. Bloodwork doesn't tell you that (except the Vectra DA test, but I highly doubt your gp ran that one). He gave you an anti inflammatory, which can help with pain but does nothing to manage disease. Frankly, gp's aren't qualified to diagnose or treat RA, so I second (third?) everyone's advice to see one as soon as you can. 

I know what you mean about being a woman and not being taken seriously. My gp dismissed me too, said it was "probably fibromyalgia or something," gave me some pain meds, and didn't offer to continue treatment. I demanded a referral to a rheumatologist, and got diagnosed with RA immediately.

Good luck to you in the meantime, I hope you find some way to alleviate the pain. Just remember though that until you get on real medication, pain meds are only alleviating your symptoms, not treating disease.
[d03sypg] (score 2, diepte 3 OP) yeah, the more I've thought about it, the more I wished I'd educated myself more before the appointment. I just didn't know what to ask for or what to expect, he didn't bring up anything past the meloxicam or anything about me seeing a specialist and I should have been more informed so I could have brought it up myself.

I've dealt with some crappy health issues for too long from doctors not taking me seriously, which is really distressing sometimes. aside from my GP it's pretty uncommon for me to go back to any kind of specialist after the first visit or two. but I'm hoping to find a really good rheumatologist that I can depend on so I can get all the preventative care I can before this issue gets even worse. 

thank you so much :) definitely going to try to find the right doctor and the right treatment plan.
[d02oy5q] (score 2, diepte 0) That really sucks. Interestingly, my sis has Raynuads and is convinced she has RA (well, interesting to us)

I cannot imagine a single NSAID being enough, have you spoken to your doc about costs and options? If your blood work is coming back with inflammation (would assume so given they put you on an NSAID). 

Ask for something to bridge you until you can afford to see a rheumy, I'm sure a round of prednisone would do the world of good.... But it isn't a fix (nothing is) and has hellish side effects for some people - my point is that there are options out there, better ones than an NSAID 

Afraid I can't help on the hands/artist thing. My hands are buggered, but I don't use them really.... They are there for show :)
[d03snoe] (score 2, diepte 1 OP) I'll definitely, definitely be making an appointment tomorrow. and that is a great idea! I have small/thin hands (aside from my sausagey knuckles) so I don't think there's much hope for me in finding adult gloves that fit. kids gloves is an awesome idea, I'll have to stop by the dollar store soon and pick some up. thank you!
[d02ps41] (score 1, diepte 1 OP) thank you for replying! I will definitely call and get a referral to one as soon as possible because I have heard they're hard to get into and it should be a few months out anyway. 

when I had the appointment we really only discussed it briefly and he said (before doing/seeing any of my bloodwork) that if my bloodwork showed high enough levels he would put me on meloxicam and that would help any pain. so, we didn't really discuss any other options. 
I only worry about seeing a rheumatologist because my levels themselves and areas of pain were enough to warrant me with a diagnosis of "mild rheumatoid arthritis" and he kept emphasizing the "mild" aspect. 
however, with my current lifestyle I'm definitely in a pain I'd consider more than mild even if that's not my diagnosis. I just worry that he wouldn't think I warrant more medication than I'm already on, same for a rheumatologist I've never seen before. with my young age--and female gender--I often feel like doctors take my pain less seriously or think I'm exaggerating. 

I'll definitely check out Isotoner! and yep, I'm known to run to the bathroom all day to heat my hands under the sink. that also reminds me to probably carry around some hand warmers, I haven't got those in a while. and I definitely have those days where I just have to cut back and sit around and do nothing with my hands. it's so unfortunate to have to prevent yourself from using two of the most precious things you have. 

thanks for the support and the answer! sorry for the long reply, I didn't expect to get more than one or two replies on this so I may direct some people to this comment :)
[d03yi0m] (score 1, diepte 4) Don't blame yourself! He should have done his job properly. It infuriates me though because you're obviously a well-educated reasonably intelligent person. Imagine all of the people out there who suffer from disease and are dismissed by doctors, but don't know how to find resources that contradict their doctor's advice. In fact, the tech at my gynecologist's office told me a story very similar to yours when I told her I have RA. *She works at a freaking doctor's office* and didn't recognize how poorly she'd been treated.

Sorry for the rant, but shitty doctors make me mad. :)
[d02xn39] (score 1, diepte 1) This came across my desk a few months ago. I can't watch it too often because his hands look awful - fingers are bent severely sideways, the joints are huge - and he's smoking, which is a particular bugaboo of mine.
[Renoir painting](http://www.openculture.com/2012/07/astonishing_film_of_arthritic_impressionist_painter_pierre-auguste_renoir_1915.html)
[d02q6zd] (score 1, diepte 2 OP) indeed, in the last few months I have lost the ability to use micron pens and do the tiny drawings I used to love :( 
some modding for stability will definitely make a difference. I hadn't really thought about a solution much, just fogged by frustration!
[d02pzlg] (score 1, diepte 1 OP) my current classes include 4 studios and 1 writing course, so all day I'm either writing or printmaking or drawing or painting or doing studio work in the computer labs... basically, I do a lot of work in lot of mediums during the day so I work with a variety of tools. I often use gel pencil grips but I haven't thought about modifying paintbrushes and things like that. I get a little embarrassed to wear gloves in class but some finger grips might not be too noticeable :) 

thinking about all those modifications is so helpful! I actually took a few occupational therapy classes so thanks to you I'll have to get out some of my old handouts that I know list some of those mods! awesome reminder :)
[d02q1py] (score 1, diepte 1 OP) even before I had my bloodwork done at the initial appointment, my doctor said that if my work warranted a diagnosis he would put me on meloxicam. I went over this a bit more if the top comment. I will definitely be making an appointment to see him or a rheumatologist as soon as possible. thank you!
[d02q4ck] (score 1, diepte 1 OP) unfortunately RA, Raynaud's, and carpal tunnel seem to run in my family. I went over this a bit in the top comment but we really only discussed meloxicam at the initial appointment because he was convinced that would relieve me of any of the pain. I will definitely have to see him or a rheumatologist sometime very soon to get on something else. it's definitely not helping me at all. 
thanks for the help :)
[d02qu3j] (score 1, diepte 2) Given your financial considerations, check the reviews of any rheumy you're considering. It helps to ask for referrals from people with the disease. The appointments are costly and the quality of the doctors varies substantially.

My first rheumy told me that he was 100% certain I didn't have the disease. I took him at his word and I have significant joint damage as a result. He's not a bad guy. He's just a checklist doctor who didn't do a thorough enough exam and I didn't know enough at the time to see his weaknesses. And, quiet frankly, I wanted the good news he gave me.
[d03s6qw] (score 1, diepte 3 OP) luckily I'm still young enough to be included on my parents health insurance plan so I do have good enough insurance to be able to see a good rheumatologist in my area. I haven't checked into who exactly I can go to yet but the ones around me seem to have pretty good ratings. 

however appointments and medications do obviously still cost quite a bit that can become difficult to afford all at once, but I'm definitely making it my next step to make an appointment with a rheumatologist tomorrow morning. thanks for the heads up, I usually do tend to believe what doctors tell me and don't often get a second opinion, which definitely isn't a good way to treat a problem like this. I definitely want to get any preventative care I can while I still can.
[d02schm] (score 1, diepte 0) I to have Raynauds and Ra.. Its very important to see a Rheumatologist as soon as possible. With my Raynauds I found that putting the little hand warmers in my pockets to warm my hands help alot, there not expensive and help get the circulation going back in my fingers. Now for my RA I have been juicing now for about 3 years and have been able to get off of my steroids. I make sure that I always have blueberries every morning when I use my nutribullet as I have found that has helped me the most in reducing the inflammation. I researched foods that were good for inflammation and that's how I got started juicing.. it has helped me tremendously.
[d03s9rm] (score 1, diepte 1 OP) thank you, I plan on making an appointment with a rheumatologist tomorrow morning :) I'll have to look up some of those foods, not a fan of blueberries but I'm sure there's probably more there that would help!
[d02xfgo] (score 1, diepte 0) Seconding everyone that has said see a real rheumatologist and get some of the hardcore meds. When my hands were at my worst (and they've done much better with meds, there's hope! My knees bother me way more now and there were times when holding a pen for three seconds to sign my name made me want to cry) I would sleep in the shitty 3-dollar drug store mittens. I got a child-sized pair so they were just a little too small for me and sleeping in them at night worked wonders for me throughout the day. So totally worth a shot in the meantime while you wait to get in to get a more long-term solution.
[d02xv06] (score 1, diepte 0) I hesitate to suggest this, but you might ask your doctor or rheumatologist for a prescription for Percocet, starting out at the lowest dosage (2.5/325). It's got acetaminophen (generic Tylenol) with oxycodone; because of the former there is a maximum daily dose limit.

Percocet and other opioids taken just to relieve pain are rarely addicting; there is a tendency to become dependent - but that's a body thing, not a raving-loony reefer-madness thing. People dependent on them can come off it relatively easily if care is taken to wean slowly.

And damn but the stuff works!
[d067ezv] (score 1, diepte 0) I feel some of your pain, literally! I'm a blogger and one of my loves is cooking/baking. Now with RA, both of those things aggravate my hands all day. I'm sure your situation can feel discouraging not to mention painful. I've found relief during the day by soaking my hands for about 15 minutes in hot water with about 1/2 cup of Epsom Salts mixed in. It relaxes the muscles and calms down some of the inflammation. I sometimes wear a soft wrist brace (inexpensive at Walmart) when I type, just so I keep my hands steady and supported.
I would suggest asking the rheumatologist right away for suggestions - and giving up on your art work should not be one of them! You may have to modify what you do, but you can make it work.
[d0c5vka] (score 1, diepte 0) Like others have said, you should definitely see a rheumatologist - you need to be on medication to prevent the progression of the disease.

I am a student as well, although not an art student. Typing and holding books open all day has my hands very red and swollen in the evenings as well. I find that advil/ibuprofen helps more than any other OTC medication.

I'm not sure what your situation is in terms of legality/personal feelings, but marijuana might provide you with some relief in the evenings. I find that it helps my inflammation a little bit, and also helps me to take my mind off of it.
[d0h675o] (score 1, diepte 0) Hairstylist here. My pain comes and goes. Hands tingle when i apply color and hands get so tired when I cut hair.

I get lympathic massages and take NSAID for pain. (800mg ibuprofen). Epsom salt baths help too.

