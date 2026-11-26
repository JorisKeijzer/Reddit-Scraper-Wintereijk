# Label-batch batch_0154

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
Schrijf het resultaat naar `batch_0154.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(2 threads: ali81r, p7kpvu).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD ali81r ===
SUBREDDIT: r/weddingplanning
DATUM: 2019-01-30  SCORE: 3  REACTIES: 60
TITEL: What is everyone wearing on their feet?
POST (source_id=post):
Heels? Flats? Heels, then flats? Can you wear flats for the evening party if your dress is hemmed at a length for heels for the ceremony? Comfortable or sexy? What have you guys decided to do (and if you’re married, was it the right decision)?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[efec05l] (score 7, diepte 0) > Can you wear flats for the evening party if your dress is hemmed at a length for heels for the ceremony?

Yes, but you'll probably be tripping on your dress. I found heels and platform sneakers that were the same height to avoid this problem and switched to said sneakers during the reception.
[efedjd1] (score 6, diepte 0) Kate Spade Keds!
[efe83qf] (score 4, diepte 0) I did heels for pics and ceremony and then sparkly platform keds for the reception.
[efejoc6] (score 3, diepte 1) Yay #teamKeds! I’ll definitely be wearing mine during our honeymoon in Prague too!
[efeewh2] (score 3, diepte 0) Flats! I'm wearing my grandmother's dress and it's JUSSSSSSSSSST long enough, so I couldn't have done heels if I'd wanted, and I didn't want to anyway, even though FH is like 6 inches taller than I am. There's a really lovely photo of the ones I got in my post history if you're interested in tan pointed flats -- they're from Shoe Carnival and wonderfully inexpensive.
[efehu6j] (score 3, diepte 0) Flats! My dress is floor length so I doubt anyone will be able to see them. They're a coppery gold color.
[efeicmm] (score 3, diepte 0) These guys: https://www.dillards.com/p/alex-marie-mairitwo-ankle-strap-wedge-sandals/507709575?di=05255806_zi_new_light_grey_ceylon

I’m 5’9 and my FH is 6’3. I didn’t want too much height, but I’m a klutz and a half in flats. Also getting married on grass, so a traditional heel was a no-go. 

My final consideration was that no one will see them, so I bought something I could wear again in the future. Probably not often, but maybe as a wedding guest or something
[efesqj0] (score 3, diepte 0) I wore flats all day. Didn't want to be tripping over my dress by changing and decided I would much rather be comfortable than taller. I went for some fancyish gold sandals that were super comfortable (and <$20!). They were cute enough given that no one but my bridesmaids saw them lol.
[efevi9p] (score 3, diepte 0) [Merlot booties](https://www.rockport.com/rockport/cobb-hill-aria/chabbottaria.html) 

Super pumped for 1in heels that are basically flats. 

Also have some SUPER PLUSH balega running socks that are spendy but 100% worth it. 

It’s going to be chilly up in the mountains so I wanted my feet covered and boots are my style.
[effrxlk] (score 3, diepte 2) Thanks!
[efea7x5] (score 2, diepte 0) Sanuk Yoga Slings in white
[efeamqj] (score 2, diepte 0) So, I thought it would be impossible to wear flats with a dress hemmed for heels. But, honestly, after seeing how it was hemmed, it's still going to be touching the ground a bit even with heels (and that's after it's been perfectly hemmed for those heels). I don't know about most seamstresses, but that's what my really experienced one did. Given that, I don't think wearing flats is going to damage your dress any more, as long as it's not a safety issue due to tripping.
[efgolih] (score 2, diepte 2) Very! They had a lot of padding on the sole which gave my feet a much needed break, and because they had a platform on the front as well as the back (but not an even one, if that makes any sense?) it still gave my legs that “wearing heels” feel without the forward pitch of my fancy heels.

Word of caution though: make sure if you’re not used to wearing heels that you practice in them. They were so comfortable that i was jumping around in them and my old lady knees were pretty pissed at me by the end of the night. Also if you can take them to your fitting, do.
[efec6zs] (score 2, diepte 0) Flats... As soon as I can find a pair that fit, I like, and don't break the bank. Or I'll just suffer through with my mom's old pair.
[efgnndo] (score 2, diepte 1 OP) No one will see them!!
[efgpnyz] (score 2, diepte 2) True true. They're just a smidge small is all. I was all set to wear her dress afterall, but it didn't survive.
[efech85] (score 2, diepte 0) Heels for me, may bring a pair of back up flats or sandals for the reception just in case.
[efgo15g] (score 2, diepte 2 OP) They are so cute! You will definitely get a lot of wear out there of them
[efgoxrk] (score 2, diepte 3) 😀 yeah for sure! That’s part of the reason why I decided on those.  That and wanting to be comfy on our special day!
[efedyho] (score 2, diepte 0) I'm wearing grey Toms.
[efgni8c] (score 2, diepte 1 OP) Lots of votes for flat sneakers. I think tons, keds and converse are so cute as wedding shoes
[efgnflg] (score 2, diepte 1 OP) I hope you’re planning to wear those socks with them on the day 😉
[efhmivm] (score 2, diepte 2) I might have to ! March in Michigan could be literally any weather 😂
[efgnbkc] (score 2, diepte 1 OP) That sounds lovely. No one will ever see them! I’ve legit never thought about the brides shoes at any other wedding I’ve been to, unless she couldn’t walk in them.
[efezfyt] (score 2, diepte 1) A friend of a friend wears her wedding shoes for their anniversary dinner
[efeozxi] (score 2, diepte 0) I’m going with converse for the entire event, more my style and they are comfortable for long periods of time!
[efgrkhz] (score 2, diepte 2) I’ve considered the sparkly ones but I think I’m going to end up with the classic black high tops. That way I can wear them with my wardrobe after the wedding too!
[efk1xly] (score 2, diepte 2) They had them in champagne and ivory! I got ivory (looks more white) to match my ivory galatea gown (which also looks very white)
[eferqn3] (score 2, diepte 0) Flats! I hardly wear heels and my fiancé and I are exactly the same height anyway
[efgmm09] (score 2, diepte 1 OP) Yes. I like the idea of something a little cute and fancy, but still super comfortable
[efhvvum] (score 2, diepte 2) Yeah, comfort was a huge priority for me. I ordered (and returned) like 40 pairs from Zappos and Amazon so I could try on at home and walk around a bit before deciding lol.
[efgmjaj] (score 2, diepte 1 OP) They’re so cute! Such a good idea, and you can definitely wear them again!
[eff8mge] (score 2, diepte 0) Silver sparkly Converse. I thank this sub so much for making me aware that Converse for wedding shoes was a thing, I hate heels and struggle in strappy shoes and was getting judged for wanting to wear thongs lol.
[efgmenu] (score 2, diepte 1 OP) Haha! I can wear heels all day, but only if they’re in boot and block heel form. I can wear stilettos for about an hour standing up. I think flats like converse are the way to go!
[efh1vxc] (score 2, diepte 2) Comfort is key!
[efgman7] (score 2, diepte 1 OP) Right? I’m getting married outside, and I just know I’m going to be moving around all day. I love the idea of keds!
[efgrevq] (score 2, diepte 2) Plus they’re super pretty 😍
[efgi0gf] (score 1, diepte 1) Was your dress hemmed for your heels or your flats? I am doing heels for ceremony,  glitter keds for the reception. The heels are about 3-4 inches...if it were hemmed for the keds would it look dumb with the heels? I honestly didn't think about it until I saw this post.
[efgqb0f] (score 1, diepte 2) I had my dress hemmed for the heels, but they were not much higher than my keds since I got the platform. But definitely hem for the heels if that’s what you’re doing with pics!
[efgtvqa] (score 1, diepte 3) I got the regular ones, not the platform. I guess I'll bring both when I go in for alterations and ask the tailor what she thinks!
[efgnuup] (score 1, diepte 1 OP) That’s good to know. Are you planning to switch to flats?
[efhnnjs] (score 1, diepte 2) I wasn't actually planning on switching to flats, but that's only because my heels are very comfortable, and I'm pretty used to wearing heels anyways. I'll probably bring some just in case, though!
[efgnrmp] (score 1, diepte 1 OP) PLATFORM SNEAKERS! This is so ingenious. Were they comfortable?
[efgnm96] (score 1, diepte 1 OP) What’s the heel like? Stiletto or block? I wish I could wear stilettos but my feet will divorce me.
[efezk0t] (score 1, diepte 2) Love it! I think I’ll plan on this :)
[efgn881] (score 1, diepte 1 OP) Ah! Okay, I’m 5’8 and my FH is 6’5, and I feel like that is making things more difficult. If he wasn’t so tall, I’d definitely just do flats. Maybe a slight heel is the way to go. They look special but comfortable. Are they comfy?
[efgnjl1] (score 1, diepte 2) I’ve only tried them on for about 10 minutes, and I thought they were!
[efeos4n] (score 1, diepte 0) I’ll be wearing flats/sandals for the ceremony (detail photos will be of the shoes). Then for the reception I’ll change into flip flops I bought from David’s Bridal. They say wifey on them! I always wear flip flops anyways so it’ll be more my style. I had my dress hemmed for flats regardless. Just need to find flats/sandals for the ceremony still...
[efgn0kj] (score 1, diepte 1 OP) Oh you’re way further ahead than me, but I guess it’s not too long until your wedding now! Good luck with the ceremony shoes!
[efgmvku] (score 1, diepte 1 OP) Yes. This seems like the way to go. Are you getting the fancy sparkly ones?
[efer4pi] (score 1, diepte 0) [these](https://www.overstock.com/search?keywords=victorian+bootie&SearchType=Header) for an outdoor desert ceremony.
[efgmtoj] (score 1, diepte 1 OP) I can’t see the link but Victorian booties? They sound cute! What colour are they?
[efgmrmn] (score 1, diepte 1 OP) That’s perfect! I’m finding it tricky because I’m 5’8”, so if I wear heels I’ll feel too tall compared to most guests, but FH is 6’5”, so if I wear flats I don’t want to look too small. 😒
[eflqejc] (score 1, diepte 3 OP) This is what I’ll do!
[eff6o0h] (score 1, diepte 0) Block heels! I find them comfortable to wear and I like how heels make me look. I haven’t found a pair yet.
[efgmg9h] (score 1, diepte 1 OP) Block heels are the only ones I can imagine myself wearing all day. Are you looking for white ones?
[efg1uzn] (score 1, diepte 0) \#teamKeds

Mine are the dark red sparkle to match my bridesmaids' dresses. No one is really going to see my feet in my dress, and we're getting married in a park, so flat and comfortable for sure!
[efh4qwm] (score 1, diepte 0) Block and they are strappy so they kind of hold my feet in better haha.
[eflqgps] (score 1, diepte 0 OP) 😂😂😂
[eflqhx9] (score 1, diepte 0 OP) Good idea!

=== THREAD p7kpvu ===
SUBREDDIT: r/diabetes
DATUM: 2021-08-19  SCORE: 179  REACTIES: 60
TITEL: LPT: If you have diabetes, keep a close eye on your feet hair. It is the first thing to go if you are losing circulation to your feet.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[h9ktf0j] (score 55, diepte 0) Like a good hobbit, my large feet are gloriously tufted with hair.

Now to bolus for second breakfast!
[h9kmg6g] (score 52, diepte 0) Filthy little hobbitses!
[h9kgppm] (score 31, diepte 0) My feet have been hairless my entire life.
[h9lovw6] (score 17, diepte 1) What about elevensies? Luncheon? Afternoon tea? Dinner? Supper?
[h9lom13] (score 14, diepte 1) Oh man, RIP your toes.
[h9kx26l] (score 12, diepte 0) *immediately pulls socks off*
[h9kyjkp] (score 11, diepte 0) I've never had hairs on my feet...
[h9l03et] (score 9, diepte 0) This isn't simply restricted to the feet, I don't think.  I've had poor circulation in my feet and legs for a while, and don't have hair below about 2 inches below my calves, along with other discoloration.

If you get this, see your pcp or a cardiologist.
[h9mdogs] (score 8, diepte 1) This. I don't think it's relevant to some of us.
[h9lsfor] (score 8, diepte 1) Peripheral neuropathy is a possibility. Definitely talk to your doctor.
[h9l1lbb] (score 7, diepte 0) Yay! Even my toes are hairy.
[h9l84cl] (score 6, diepte 0) I'm afraid i have started losing circulation in both my arms and legs, i frequently find them numb (like when you sleep on your arm) except they are not in any unordinary position, i wake up with numb arms even if they are straight and relaxed, it also happens frequently while i sit, this didnt happen before, it does fix if i move the limb around slightly but it still worries me

Even if it is the diabetes causing it, is there anything to do?
[h9kytzu] (score 5, diepte 0) I've never had hairy feet to start with.
[h9lcoiq] (score 5, diepte 1) me...on the toes, and a little spot on the top too. A mild cas of the hobbit if you'd like.
[h9lmog4] (score 5, diepte 1) Yes, make sure you check the hair on your eyeballs!
[h9n1pz8] (score 3, diepte 2) Sounds exhausting frankly
[h9o1jp9] (score 3, diepte 3) well, just have a bit of cheese and read a good book while you recover.
[h9ktl5i] (score 3, diepte 0) When being hobbity is a good thing.
[h9nk18w] (score 3, diepte 1) Huh, that's interesting. I'm T1 and had a heart attack some years ago and ever since the heart attack my lower legs and feet have been really sensitive to touch, it feels tickly. The hair below my knees has thinned out considerably (I also have PCOS so I was pretty hairy!) and now I've read your comment I'm realising it's from about 2 inches below my knee... is that a significant point on the leg for some reason that you know or just conincidence? I'm wondering if I should mention it at some future dr appointment.
[h9nx74n] (score 3, diepte 2) I don't think it's a significant point necessarily, other than just being that far from the heart, and if you have a job where you sit a lot, like I do, that doesn't help the circulation either.  For me, it started in the feet and took years to even get to the ankles, and then suddenly over the last 3 years, it's gone right up the legs.  I'd thought I was wearing bad socks for a while, since it's in that area, but when it went higher than my socks, and I started having other issues, I started pointing it out to my doctors.

I really just made the connection from this post.  My feet have had some discoloration for years, and I had been told it's because of poor circulation there, and it has slowly spread up the legs over the years.  I had some issues with an infection in my leg this spring and the wound care doctor said that the discoloration was likely iron that had leached out of the blood veins due to weak blood vessels and poor circulation.  Now I have a doctor appointment in about a month with my pcp, and hopefully she'll direct me to a cardiologist and we'll see if it's just from diabetes or if there is another issue.  Several doctors have told me that the issues with my legs don't make sense because my A1C has been below a 6.5 for about 5 years now, so it's well controlled, the the issues with the legs have really developed over the last 3 years.

Anyway, yeah I'd not thought to connect the hairlessness part to it until this post, and then it was obvious.

Best of luck!
[h9nyova] (score 3, diepte 3) That's really interesting, thanks for your detailed reply. Good luck to you too!
[h9l3pyv] (score 3, diepte 0) Hmm. How bout from friction? Socks off/on. Barefoot in shoes.
[h9mlo6w] (score 3, diepte 5) Don't rest your elbows or wrists on anything.  It compresses your tendons and/or nerves, and it adds up over time.  Remember getting hit in the "funny bone"?  Now think about where that nerve is and realize that you may be compressing it when you put your elbows on an armrest.

Less common, but don't sit with your knees pressed up against anything, either.
[h9kzz6k] (score 2, diepte 1) Both really, the follicles will die without blood flow.
[h9oykeu] (score 2, diepte 4) I've have the exact issues, no hair 2" below the knee, discoloration from the calves & below. I've been a t1d for 51 years, had a heart attack in 2004 as well. My a1c hasn't been above 6.9 for over 12 years. The poor circulation is in my veins, not the arteries so I was told. Fluid leaches out of the blood and causes the discoloration and swelling. I have been put on a strong water pill which causes me to pee every 20 minutes from the moment I take it thru the next 6 - 8 hours. Hard to make plans for the mornings.
[h9m5foa] (score 2, diepte 1) 1) Talk to your doctor. You will probably need to see a neurologist to rule out or confirm neuropathy and/or address other possible causes for your symptoms.  
2) If it is neuropathy due to diabetes, *and* your BG is not well controlled, changing your treatment and having better BGs may help the nerves heal over time and lead to a reduction in symptoms. It depends on various factors though, especially since nerves are often not very forgiving.
[h9lf0ej] (score 2, diepte 0) Well crap. I've never had hairy feet my entire life so can't tell from that, but noticed in the past few years that I barely have any hair on my legs below the knees now...
[h9lmijf] (score 2, diepte 1) Sit a lot? Long socks (above ankle, below knee)? That could also be doing it.
[h9o1kpd] (score 2, diepte 1 OP) be safe and keep an eye on everything that's nothing to play with
[h9oszei] (score 1, diepte 1) PANIC!!!! :D
[h9ktupm] (score 1, diepte 0) Ah good mine are still there
[h9ku8rh] (score 1, diepte 0) They'll fall off or stop growing?
[h9m6v31] (score 1, diepte 1) This is also a sign of inflammation somewhere in your arms. Things get swollen, it pinches a nerve, your arms go numb. I had it when I had shoulder tendonitis, and it sucked. Either way, you should talk to your doctor!
[h9m9xj6] (score 1, diepte 2) My hands used to go numb after work, I had an office job, no impact or anything… my doc recommended both wrist braces and the cuffs used for tennis elbow.  Apparently something was getting inflamed near my elbow and was causing nerve issues down my arm. It went away after a week or so of using the wrist braces and cuffs, then just the cuffs at work as needed. Fingers crossed it’s a silly nerve thing for you also but it can’t hurt to email your doc and ask about it. You can get the wrist immobilizer braces and the tennis elbow cuff with the little pad in it on Amazon for WAY cheaper than I paid my doc for them.
[h9miycw] (score 1, diepte 3) Do you rest your elbows on your armrests while computing?
[h9mk9ie] (score 1, diepte 4) I used to, I don’t anymore though… huh.
[h9mto41] (score 1, diepte 6) The real LPT is always in the comments, thanks!
[h9nrifc] (score 1, diepte 1) I got diagnosed in April and this has gotten progressively worse since then. Lowering glucose is said to help, but it gets worse before it gets better. I’m fairly disabled for walking and using my hands. You can try to determine the location of pinched nerves and see if that helps. I’m starting to think the issue is inflammation more local to the tendons.
[h9sgtqg] (score 1, diepte 1) It's all about control. If we can tighten up our control, sometimes the neuropathy will heal on its own. Definitely mention it to your doctor.
[h9larf0] (score 1, diepte 0) I don’t have hair on my feet and I don’t have moons on my nails, so I’m doomed. 😂
[h9lewak] (score 1, diepte 0) Hobbit checking in.
[h9lmrt5] (score 1, diepte 2) Sit a decent amount but don't usually wear high socks. Legs have never been particularly hairy but less in recent years.
[h9lkd4l] (score 1, diepte 0) Oh my... I was born with very little hair and have been that way for the last 53 years.  Well, except my ears.... they keep sprouting thick splintery hairs but my ocd habits take care of them when they're long enough.
[h9llvlh] (score 1, diepte 0) I will add keep your eyes under check too since  it will also be hit first too
[h9loxev] (score 1, diepte 0) I've never had hair on my feet, but the other day I wasn't feeling well so I didn't shave my legs before a dr. appt. While he had me on the table he mentioned that it was good that I still had hair on my legs. I apologized for not shaving them before I came in, he said no, that was a good thing for a diabetic to have, it indicated no leg circulation probs. Who knew?
[h9ltvbg] (score 1, diepte 0) Yeah, my endo always comments on them. The first time she said that I was taken a bit aback, like uh... thanks?
[h9lv3mo] (score 1, diepte 0) Good to know!
[h9lzcjk] (score 1, diepte 0) I've had hair in my big toe but that was because of PCOS lol
[h9m91g0] (score 1, diepte 0) Weird!
[h9meu23] (score 1, diepte 0) Mine disappeared years ago
[h9n3er4] (score 1, diepte 0) Well, I'm boned. My toeless compression stockings (for another condition) has worn the hair off my big toe.
[h9n4nlw] (score 1, diepte 0) For once I'm happy with my one thick toe hair
[h9nc2i3] (score 1, diepte 0) I had a bit of hair on my feet, when I went into DKA and after I was treated I noticed my feet lost all the hair, was a little panicked but it came back in a good few weeks.

I was also losing a lot of my hair on the top of my head after I got treated, they said it might have been down to stress, which is a fair assumption to make. I stopped losing my hair and all hair stuffs to normal. 😁
[h9nxh55] (score 1, diepte 0 OP) Ty
I didn't know this

Unrelated:
My daughter, wife and I all got COVID at the same time. They're feeling fine. I am going on day 3 feeling awful -- fever, back pains, congestion, sore throat, etc.
Diabetes sucks, that is all...
[h9odnqi] (score 1, diepte 0) Loss of hair is also a system of neuropathy!!
[h9opnxr] (score 1, diepte 0) Phew… I read this as feet/hair. As a balding man at age 30 I thought I was fucked.
[h9sgg3t] (score 1, diepte 0) I remember noticing that my diabetic uncle's feet and lower legs looked like glassy white porcelain. No hair, no pigment, almost blue-white. Then I noticed a few years ago that I don't have any leg hair, either, after years of being a "furry feminist" who wore pants all the time & had no interest in shaving my legs. They look like they've been through laser hair removal, but...NOPE. It is definitely a sign of poorly-controlled diabetes impacting our nerves & circulation in our extremities. Eeeeps.
[h9l9s6k] (score 0, diepte 0) Wtf who has hair on their feet
[h9lorxn] (score 0, diepte 0) uhh, the post is gone

