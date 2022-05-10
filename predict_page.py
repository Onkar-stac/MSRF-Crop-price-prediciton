import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl','rb') as file:
        mod = pickle.load(file)
    return mod
        
deploy = load_model()
regressor = deploy['model']
le_com = deploy['le_c']
le_s = deploy['le_s']
le_d = deploy['le_d']
le_m = deploy['le_m']

def predict():
    st.backgroundColor = 'blue'
    st.title("Crop Price Prediction")
    st.write("Please choose from the following:")
    com = ('Ajwan', 'Alasande+Gram', 'Amaranthus', 'Amla(Nelli+Kai)',
       'Amphophalus', 'Antawala', 'Apple', 'Arhar+Dal(Tur+Dal)',
       'Ashgourd', 'Avare+Dal', 'Banana', 'Banana+-+Green',
       'Barley+(Jau)', 'Beans', 'Beaten+Rice', 'Beetroot', 'Betal+Leaves',
       'Bitter+gourd', 'Black+pepper', 'Bottle+gourd', 'Brinjal',
       'Broken+Rice', 'Cabbage', 'Capsicum', 'Cardamoms', 'Carrot',
       'Cashewnuts', 'Castor+Seed', 'Cauliflower', 'Coconut',
       'Chapparad+Avare', 'Chennangi+Dal', 'Chikoos(Sapota)', 'Chili+Red',
       'Chilly+Capsicum', 'Cloves', 'Cluster+beans', 'Cocoa',
       'Coconut+Oil', 'Coconut+Seed', 'Coffee', 'Colacasia', 'Copra',
       'Coriander(Leaves)', 'Corriander+seed', 'Cowpea(Veg)', 'Cotton',
       'Cucumbar(Kheera)', 'Cummin+Seed(Jeera)', 'Drumstick',
       'Dry+Chillies', 'Dry+Fodder', 'Dry+Grapes', 'Duster+Beans', 'Egg',
       'Elephant+Yam+(Suran)', 'Field+Pea', 'Firewood', 'Fish', 'Garlic',
       'Ghee', 'Gingelly+Oil', 'Ginger(Dry)', 'Ginger(Green)', 'Grapes',
       'Green+Avare+(W)', 'Green+Chilli', 'Green+Fodder', 'Green+Peas',
       'Ground+Nut+Seed', 'Groundnut', 'Groundnut+(Split)',
       'Groundnut+pods+(raw)', 'Guar', 'Guava', 'Gur(Jaggery)', 'Hen',
       'Hybrid+Cumbu', 'Indian+Beans+(Seam)', 'Isabgul+(Psyllium)',
       'Jack+Fruit', 'Jamun(Narale+Hannu)', 'Jowar(Sorghum)', 'Jute',
       'Karbuja(Musk+Melon)', 'Knool+Khol', 'Kulthi(Horse+Gram)',
       'Lak(Teora)', 'Leafy+Vegetable', 'Lemon', 'Lime', 'Linseed',
       'Litchi', 'Long+Melon(Kakri)', 'Mahua', 'Maida+Atta', 'Maize',
       'Mango', 'Mango+(Raw-Ripe)', 'Mashrooms', 'Masur+Dal',
       'Methi+Seeds', 'Methi(Leaves)', 'Millets', 'Mint(Pudina)',
       'Moath+Dal', 'Mousambi(Sweet+Lime)', 'Mustard', 'Mustard+Oil',
       'Myrobolan(Harad)', 'Nutmeg', 'Onion', 'Onion+Green', 'Orange',
       'Paddy(Dhan)(Basmati)', 'Paddy(Dhan)(Common)', 'Papaya',
       'Papaya+(Raw)', 'Peach', 'Peas+cod', 'Peas+Wet', 'Peas(Dry)',
       'Pepper+garbled', 'Pepper+ungarbled', 'Pineapple', 'Plum',
       'Pomegranate', 'Potato', 'Pumpkin', 'Raddish',
       'Ragi+(Finger+Millet)', 'Rajgir', 'Rice', 'Ridgeguard(Tori)',
       'Round+gourd', 'Rubber', 'Safflower', 'Snakeguard', 'Soanf',
       'Soyabean', 'Spinach', 'Sponge+gourd', 'Sugar', 'Sunflower',
       'Surat+Beans+(Papadi)', 'Suva+(Dill+Seed)', 'Suvarna+Gadde',
       'Sweet+Potato', 'Sweet+Pumpkin', 'T.V.+Cumbu', 'Tamarind+Fruit',
       'Tapioca', 'Taramira', 'Tender+Coconut', 'Tinda', 'Tobacco',
       'Tomato', 'Toria', 'Turmeric', 'Turmeric+(raw)', 'Turnip',
       'Water+Melon', 'Wheat', 'Wheat+Atta', 'White+Peas',
       'White+Pumpkin', 'Wood', 'Yam+(Ratalu)', 'Bamboo', 'Yam',
       'Kodo+Millet(Varagu)', 'Goat', 'Pear(Marasebu)', 'Balekai',
       'Gram+Raw(Chholia)', 'Cow', 'Same/Savi', 'Sugarcane',
       'She+Buffalo', 'Sheep', 'Soji', 'Chow+Chow', 'Pigs', 'Calf',
       'Duck', 'Ox', 'Dhaincha', 'Season+Leaves', 'Cock', 'Hippe+Seed',
       'Tamarind+Seed', 'Other+Pulses', 'Coca', 'Niger+Seed+(Ramtil)',
       'Ram', 'Thondekai', 'Galgal(Lemon)', 'Honge+seed', 'Lotus+Sticks',
       'Neem+Seed', 'Bran', 'Cherry', 'Mace', 'Kartali+(Kantola)',
       'She+Goat', 'Alsandikai', 'Mahedi', 'Bull', 'Thogrikai', 'Khoya',
       'Seetapal', 'Almond(Badam)', 'Butter', 'Rose(Loose)', 'Kinnow',
       'He+Buffalo', 'Marigold(loose)', 'Mataki', 'Sajje',
       'Marigold(Calcutta)', 'Ambada+Seed', 'Chrysanthemum(Loose)',
       'Cotton+Seed', 'Seemebadnekai', 'Gramflour',
       'Persimon(Japani+Fal)', 'Lint', 'Indian+Colza(Sarson)', 'Sabu+Dan',
       'Jasmine', 'Gurellu', 'Walnut', 'Bunch+Beans', 'Snake+gourd',
       'Ridge+gourd(Tori)', 'Dalda', 'Sabu+Dana', 'Tube+Rose(Loose)',
       'Rose(Local)', 'Seetafal', 'Siddota', 'Lukad', 'Sunhemp',
       'Alasande Gram', 'Amla(Nelli Kai)', 'Anthorium',
       'Apple', 'Arecanut(Betelnut/Supari)',
       'Arhar (Tur/Red Gram)(Whole)')
    state_names = ('Gujarat', 'Madhya Pradesh', 'Rajasthan', 'Karnataka', 'Kerala',
       'Punjab', 'Uttar Pradesh', 'Chattisgarh', 'Haryana',
       'Himachal Pradesh', 'Maharashtra', 'NCT of Delhi', 'Odisha',
       'Uttrakhand', 'West Bengal', 'Assam', 'Manipur',
       'Jammu and Kashmir', 'Meghalaya', 'Nagaland', 'Tripura',
       'Telangana', 'Tamil Nadu', 'Andhra Pradesh', 'Pondicherry',
       'Jharkhand', 'Goa', 'Mizoram', 'Andaman and Nicobar')
    district_names = ('Amreli', 'Banaskanth', 'Jamnagar', 'Mehsana', 'Neemuch',
       'Chittorgarh', 'Bagalkot', 'Bangalore', 'Gadag', 'Panna',
       'Ernakulam', 'Kollam', 'Thiruvananthapuram', 'Thirssur',
       'Alappuzha', 'Kozhikode(Calicut)', 'Kasargod', 'Palakad',
       'Malappuram', 'Pathanamthitta', 'Kottayam', 'Kannur', 'Wayanad',
       'Idukki', 'Sangrur', 'Kanpur', 'Chikmagalur', 'Durg', 'Karnal',
       'Faridabad', 'Hissar', 'Bhiwani', 'Kaithal', 'Fatehabad',
       'Sonipat', 'Kurukshetra', 'Mahendragarh-Narnaul', 'Jind',
       'Panipat', 'Mandi', 'Kangra', 'Sirmore', 'Solan', 'Harda',
       'Chandrapur', 'Kolhapur', 'Nashik', 'Pune', 'Delhi', 'Mayurbhanja',
       'Faridkot', 'Ferozpur', 'Gurdaspur', 'Hoshiarpur', 'Patiala',
       'Tarntaran', 'Ajmer', 'Ganganagar', 'Udaipur', 'Agra',
       'Ambedkarnagar', 'Aligarh', 'Maharajganj', 'Banda', 'Auraiya',
       'Azamgarh', 'Badaun', 'Ballia', 'Balrampur', 'Unnao', 'Barabanki',
       'Baghpat', 'Bareilly', 'Basti', 'Mainpuri', 'Etawah', 'Bijnor',
       'Fatehpur', 'Bulandshahar', 'Muradabad', 'Kannuj', 'Etah',
       'Faizabad', 'Farukhabad', 'Saharanpur', 'Ghaziabad', 'Gonda',
       'Gorakhpur', 'Hardoi', 'Jyotiba Phule Nagar', 'Jalaun (Orai)',
       'Jaunpur', 'Jhansi', 'Chitrakut', 'Mau(Maunathbhanjan)', 'Mathura',
       'Lakhimpur', 'Lalitpur', 'Lucknow', 'Mahoba', 'Meerut', 'Mirzapur',
       'Muzaffarnagar', 'Siddharth Nagar', 'Pillibhit', 'Rampur',
       'Bahraich', 'Shahjahanpur', 'Firozabad', 'Sitapur', 'Sultanpur',
       'Padrauna(Kusinagar)', 'Haridwar', 'UdhamSinghNagar',
       'Garhwal (Pauri)', 'Dehradoon', 'Kolkata', 'Nalbari', 'Mysore',
       'Shimoga', 'Sagar', 'Buldhana', 'Mumbai', 'Bishnupur',
       'Imphal West', 'Imphal East', 'Thoubal', 'Allahabad', 'Hathras',
       'Hamirpur', 'Varanasi', 'Puruliya', 'Birbhum', 'Rajnandgaon',
       'Narmada', 'Sirsa', 'Rohtak', 'Yamuna Nagar', 'Kullu', 'Bilaspur',
       'Chamba', 'Srinagar', 'Burhanpur', 'Jalgaon', 'West Garo Hills',
       'East Khasi Hills', 'Jalandhar', 'Bhatinda', 'Mohali',
       'kapurthala', 'Raebarelli', 'Nanital', 'Darjeeling', 'Ahmedabad',
       'Bharuch', 'Surat', 'Sundergarh', 'Dhenkanal', 'Ganjam',
       'Sant Kabir Nagar', 'Chhatarpur', 'Dausa', 'Bundi', 'Tonk',
       'Hanumangarh', 'Kota', 'Sikar', 'Rajkot', 'Junagarh', 'Kolar',
       'Satara', 'Dimapur', 'Koraput', 'Nagaon', 'Kheda', 'Davangere',
       'Narsinghpur', 'Kamrup', 'Dahod', 'Vadodara(Baroda)', 'Panchkula',
       'Ambala', 'Jammu', 'Chhindwara', 'Indore', 'Jhabua', 'Ujjain',
       'Aurangabad', 'Nayagarh', 'Khurda', 'Cuttack', 'Bolangir',
       'Jajpur', 'Fazilka', 'Moga', 'Muktsar', 'Ludhiana', 'Sepahijala',
       'Khowai', 'Jalpaiguri', 'Dakshin Dinajpur', 'North 24 Parganas',
       'Coochbehar', 'Medinipur(E)', 'Medinipur(W)', 'Madikeri(Kodagu)',
       'Navsari', 'Valsad', 'Gurgaon', 'Dhar', 'Khandwa', 'Badwani',
       'Sheopur', 'Nagpur', 'Ahmednagar', 'Jalore', 'Sonbhadra',
       'Gautam Budh Nagar', 'Ghazipur', 'Rajgarh', 'Dewas', 'Guna',
       'Mandsaur', 'Shajapur', 'Sholapur', 'Ratnagiri', 'Bargarh',
       'Sonepur', 'Boudh', 'Kendrapara', 'Jagatsinghpur', 'Amritsar',
       'West District', 'Nadia', 'Burdwan', 'Bankura', 'Murshidabad',
       'Howrah', 'Nowarangpur', 'Morbi', 'Shimla', 'Hyderabad',
       'Mahbubnagar', 'Udupi', 'Gajapati', 'Ariyalur', 'Kurnool',
       'Kachchh', 'Bhavnagar', 'Surendranagar', 'Gandhinagar',
       'Sabarkantha', 'Patan', 'Porbandar', 'Anand', 'Mewat', 'Dindori',
       'Hassan', 'Erode', 'Dindigul', 'Coimbatore', 'Madurai', 'Salem',
       'Tumkur', 'Karaikal', 'Namakkal', 'Baran', 'Bijapur', 'Dharwad',
       'Raichur', 'Beed', 'Wardha', 'Villupuram', 'Karimnagar', 'Khammam',
       'Adilabad', 'Warangal', 'Barnala', 'Narayanpur', 'Cuddalore',
       'Haveri', 'Chitradurga', 'Cuddapah', 'Bellary', 'Shivpuri',
       'Amarawati', 'Nanded', 'Dhule', 'Vashim', 'Yavatmal',
       'Thiruvannamalai', 'Nalgonda', 'Nagaur', 'Visakhapatnam', 'Bidar',
       'Mandya', 'Jalana', 'Jaipur', 'Khargone', 'Latur', 'Parbhani',
       'Osmanabad', 'Raigad', 'Nandurbar', 'Sangli', 'Thane', 'Bhilwara',
       'Dhubri', 'Uttar Dinajpur', 'Malda', 'Damoh', 'Mahasamund',
       'Kanker', 'Dhamtari', 'Raigarh', 'Dantewada', 'Jashpur', 'Korba',
       'Sonitpur', 'Panchmahals', 'Belgaum', 'Ratlam', 'Virudhunagar',
       'Ranga Reddy', 'Medak', 'Chittor', 'Alirajpur', 'North Tripura',
       'Bhind', 'Swai Madhopur', 'Jhalawar', 'Bharatpur',
       'South District', 'Raipur', 'Janjgir', 'Balodabazar',
       'Karwar(Uttar Kannad)', 'Balaghat', 'Bhandara', 'Kancheepuram',
       'Vellore', 'Thanjavur', 'Nizamabad', 'Hooghly', 'Singroli',
       'Kaushambi', 'Cachar', 'Koppal', 'Hingoli', 'Akola', 'Dharmapuri',
       'Rajasamand', 'Champawat', 'Surguja', 'Koria', 'Surajpur',
       'Nawanshahr', 'Shravasti', 'Khiri (Lakhimpur)', 'Gwalior',
       'Chandauli', 'Balasore', 'Kohima', 'Deoria', 'Angul', 'Barmer',
       'Malkangiri', 'Fatehgarh', 'Gomati', 'Mansa', 'Ropar (Rupnagar)',
       'Kalahandi', 'Gadchiroli', 'Sounth 24 Parganas', 'Bhadrak',
       'Betul', 'Una', 'Unokoti', 'Ashoknagar', 'Rewa', 'Jharsuguda',
       'Gulbarga', 'Hoshangabad', 'Hailakandi', 'Goalpara', 'Chandel',
       'Karimganj', 'Nongpoh (R-Bhoi)', 'Sivaganga', 'Bastar',
       'Kabirdham', 'Udhampur', 'Sehore', 'Morena', 'Pratapgarh',
       'Chamrajnagar', 'Satna', 'Raisen', 'Jhajar', 'Puri', 'Vidisha',
       'Pondicherry', 'Keonjhar', 'Alwar', 'Garhwa', 'East Jaintia Hills',
       'North Goa', 'Ramanathapuram', 'Rayagada', 'Barpeta', 'Giridih',
       'Seoni', 'Churu', 'East Godavari', 'West Godavari', 'Jabalpur',
       'Aizawl', 'Jorhat', 'Anupur', 'Pali', 'Nicobar', 'Wokha',
       'Gondiya', 'Sukma', 'Botad', 'Mokokchung', 'Kondagaon',
       'West Jaintia Hills', 'Mandla', 'Karauli', 'Kandhamal', 'Anantnag',
       'Longleng', 'Tikamgarh', 'Peren', 'Balod', 'Nuapada', 'Guntur',
       'Kathua', 'Sambalpur', 'Pulwama', 'Dhalai', 'Baramulla', 'Bikaner',
       'Gariyaband', 'Koderma', 'Mungeli', 'Sidhi', 'Kokrajhar',
       'South Goa', 'Vijayanagaram', 'Bangaigaon', 'Zunheboto', 'Phek',
       'Darrang', 'The Dangs', 'Bhopal', 'Kiphire', 'Tuensang', 'Rewari',
       'Sirohi', 'Umariya', 'Palwal', 'Jodhpur', 'Bemetara', 'Shehdol',
       'Anantapur', 'Krishnagiri', 'Thiruchirappalli', 'Dibrugarh',
       'Jaisalmer', 'Nagapattinam', 'Thiruvarur', 'Pathankot', 'Marigaon',
       'Katni', 'Datia', 'Golaghat', 'Jhunjunu', 'Lohardaga', 'Rajouri',
       'Theni', 'Dholpur', 'Badgam', 'Bhadohi(Sant Ravi Nagar)',
       'Mangalore(Dakshin Kannad)')
    
    commodity = st.selectbox('Commodity', com)
    state = st.selectbox('State',state_names)
    district =  st.selectbox('District',district_names)
    market = st.selectbox('Market',district_names)
    min_price = st.slider('Minimum price of the commodity per 1kg',0,500,100)
    max_price = st.slider('Maximum price of the commodity per 1kg',0,1000,700)

    result = st.button('Predict the price')
    if result:
        X = np.array([[commodity,state,district,market,min_price,max_price]])
        X[:,0] = le_com.fit_transform(X[:,0])
        X[:,1] = le_s.fit_transform(X[:,1])
        X[:,2] = le_d.fit_transform(X[:,2])
        X[:,3] = le_m.fit_transform(X[:,3])
        calc = regressor.predict(X)
        st.subheader(f'The estimated price is Rs.{calc[0]:.2f} per Kg')