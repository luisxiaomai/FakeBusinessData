from .. import Provider as CampaignProvider


class Provider(CampaignProvider):
    
    name_list = ["Black Friday","Christmas Day","New Years Day","Abraham Lincolns Birthday","St Valentines Day","St Patricks Day ","Easter Day Easter Sunday",
    			 "April Fools Day","Mothers Day","National Flag Day","Fathers Day","Independence Day","Labor Day","Eve of All Saints Day","All Souls Day","Thanksgiving Day",
    			 "Forefathers Day","Veterans Day","Columbus Day","Early promotion","Year-end sales promotion","Midyear sales promotion","Anniversary"]

    campaign_list = ['{} Campaign'.format(a) for a in name_list]
