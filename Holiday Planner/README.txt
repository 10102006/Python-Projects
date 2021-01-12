date : 1-12-2020

what has been done:
    1. I initialised a basic stucture of the state info with the dict
    2. Making a seperate class for the dict handling of the state details was a good idea
    3. This is an overview of the function made
        1. Starting from the end I firstly made the hotel dict and returned
        2. Then made the function to intialise a tourist place with details as its attributes
        3. I made so that I can add the above made hotel dict in the tourist destination dict
        4. Then like previous point 2. I made a function for state dict intialisation also I ensured that the dict is stored in a main database
        5. Adding the tourist places was a problem but it is solved for now make it more intutive
        6. Lastly I made the function for adding tourist destination to the state dict this has a similar approach as the adding hotel function but this need a check if the return is none or not otherwise it will be a prob
    4. Overall this a basic structure for the tourister (this is the name I am considering)
    5. Next step is to make it file friendly


? Dict Manupulation Stuffs
*    n_bang, d_bang = init.Make_TouristPlace('Pune', 'Good place for business and tech hub.', ['Bus', 'Train', 'Aeroplane'])
*    n_belg, d_belg = init.Make_TouristPlace('Mumbai', 'Very good place less pollution and good people.', ['Train', 'Aeroplane'])

*    nh_pune, dh_pune = init.Make_Hotel('Puneri Suit', '7/10', 1500)
*    nh_mumbai, dh_mumbai = init.Make_Hotel('Mummbai Grandeour', '9/10', 2000)
*    nh_mumbai_2, dh_mumbai_2 = init.Make_Hotel('Mast Mumbai Hotel', '8/10', 800)

*    init.Add_Hotel(d_bang, nh_pune, dh_pune)
*    init.Add_Hotel(d_belg, nh_mumbai, dh_mumbai)
*    init.Add_Hotel(d_belg, nh_mumbai_2, dh_mumbai_2)

*    Maharashtra = init.Make_State(database, 'Maharashtra', 'Very good place intelligent audience as the community.')

*    init.Add_TouristPlace(Maharashtra, n_bang, d_bang)
*    init.Add_TouristPlace(Maharashtra, n_belg, d_belg)
