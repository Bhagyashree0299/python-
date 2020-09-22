next = True
while next == True:
    print(''' From all the mentioned Zodiac Signs
    1) Aries
    2) Tauras
    3) Gemini
    4) Cancer 
    5) Leo
    6) Virgo
    7) Libra
    8) Scorpio
    9) Sagittarius
    10) Capricorn
    11) Aquarius
    12) Pisces
    ''')

    s = int(input("Pick your sign number and Press Enter to know your future :\n"))

    if s == 1:
        print('''    This is not the day to either sell or buy property. Your reluctance in spending money on
         something you accord a lower priority may not be right. A new project will proceed smoothly
         as you get help from all quarters. Good will power in sticking to the exercise regime will
         help you in coming back in shape. Drudgery of domestic chores may make you long for a break.
         Those opting for higher studies will be able to gather their focus and energy. A short vacation
         just to let your hair down cannot be ruled out.''')
    elif s == 2:
        print('''       Your mood swings can make you miss a profitable opportunity, so do something about it. 
            You will be able to put across your points effectively on the professional front. Be considerate 
            of a family member in all your domestic decisions. Tread carefully while discussing a property issue. 
            Students appearing for examination will do well to maintain their tempo of studies. Make things exciting 
            on the family front by undertaking a short journey. Growing financially strong is indicated, but efforts 
            will have to be made. ''')
    elif s == 3:
        print('''       Moneywise, you will find yourself more secure now, than before. Good diet and regular exercise will 
            keep you both physically and mentally robust. You may have to share the burden of domestic chores. 
            Those into buying and selling property must focus on discounts. Completing a challenging task successfully 
            will add to your professional reputation. Those seeking admission in a premier institute are likely to 
            get the call. You may get busy at work and may have to spend time out of town. ''')
    elif s == 4:
        print('''       Money will not be a problem for you, so shop till you drop! It may be difficult to make a client accept 
            your views on the professional front. Good physical condition will make strenuous activities, a child’s play. 
            Good returns are foreseen from a rented property. Some of you will need to regain lost ground on the 
            academic front by burning the midnight oil. Accompanying family for a fun trip is on the cards. Those 
            undertaking a journey by road need to exercise caution. ''')
    elif s == 5:
        print('''       A family youngster may make you proud by his or her achievement. This is a favourable day to seal a 
            property deal. Your professional skills are likely to be acknowledged at work. You will have enough 
            to purchase a major household item. Those planning for higher studies are likely to find the day eventful. 
            Those handling gym equipment must do so under the supervision of a fitness expert. A comfortable journey 
            is foreseen for those travelling long distance. ''')
    elif s == 6:
        print('''       It is time you turned your attention to saving by becoming more careful of your spending. 
            You will be able to give a good account of yourself by solving workplace problems. A few new 
            exercises will benefit those trying to bring specific body parts in shape. A property deal 
            promises to bring in big money. Whatever you have achieved academically, you stand to lose 
            due to sheer negligence. A function at home can keep you busy and entertained. A comfortable 
            journey is foreseen for those travelling long distance. ''')
    elif s == 7:
        print('''       An outdoor activity is likely to give you a chance for sweating out. A child may need guidance, 
            so spare some time for him or her. You are likely to burn the bridges by a few wrong professional moves, 
            if you are not careful. Don’t lose touch with reality in your eagerness to earn more money, as you may lose 
            old clients. Students will excel by providing full focus to the work at hand. A short vacation is on the 
            cards for some and will prove most enjoyable. A house rented out is likely to give good returns. ''')
    elif s == 8:
        print('''       A new source of income is likely to make your financial worries disappear. A change of medication 
            will save those unwell from side effects. Professionally you are assured of whatever is due to you 
            in terms of promotion or increment. Happiness prevails at home, as friends and relatives drop in. 
            Students appearing for examinations or competitions can heave a sigh of relief. You may need to plan 
            a journey in the coming few days. A property deal shows all signs of turning favourable. ''')
    elif s == 9:
        print('''       Chance to earn big money may present itself to those running their own business. Home remedies come 
            in real handy for those suffering from minor ailments. Some desperate measures on the job front are in 
            the offing, but you will not be affected. Efficiency will be the keyword for homemakers. You can feel 
            apprehensive about an impending course or task, but your fears will be unfounded. A business trip is 
            likely to bag you a good deal. Your fears about a property matter will be laid to rest. ''')
    elif s == 10:
        print('''       On the financial front, a new source of income is likely to be tapped soon that may get your coffers 
            brimming! Successfully completing an assigned job will give you the edge at work. Those down with an 
            ailment will be on the path to full recovery. Spouse may need emotional support, so be there for him 
            or her. There is no need to become big hearted where property is involved. Those preparing for 
            competitions need to retain their focus and avoid distractions. Those trying their hands on driving 
            on the road for the first time are likely to build more confidence. ''')
    elif s == 11:
        print('''       You may choose to wait for better investment options, before committing your money. New dimensions 
            open up on the professional front as you handle more than one project. Sticking to your exercise 
            regime will begin to show positive results. Homemakers may have their hands full in doing up the house. 
            A good day is foreseen for students appearing in a competitive exam. An out of town trip cannot be ruled 
            out for some. A property matter may not get resolved due to delay in paperwork. ''')
    elif s == 12:
        print('''Financially, your position remains sound and opportunities to earn materialise. Adopting a disciplined 
             life and change in lifestyle will help in restoring energy and health. A family business may require new 
             insights and strategies to be restored to its past glory. You will feel quite at home in a new 
             environment. Students preparing for competitions can face a tough time in resisting distractions. 
             You may become part of a leisure trip and enjoy your heart out. Landlords will find a tenant for their 
             house. ''')

    else:
        print("Hey You sure about the number?")

    next = True if input("\nShall we do it again? (Y/N) :") == "Y" else False

