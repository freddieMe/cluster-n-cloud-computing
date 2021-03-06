# vedant
# comp90024

from flask import Flask, render_template
import couchdb
import argparse

# configuration
DEBUG = True
USERNAME = 'admin'
PASSWORD = 'admin'
url = 'http://admin:admin@172.17.0.2:5984'

# create our application
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# responses to ui
response_sports = {}
response_gamble = {}
response_tot_persons = {}
response_tweet_score = {}
response_neg_score = {}
response_married = {}
response_tot_persons_score = {}
response_income = {}
response_sports_four = {}


# connecting to couchdb
def connect_db():
    try:
        server = couchdb.Server(url)
        return server
    except Exception as e:
        print(e)


# index page
@app.route('/index')
def index():
    return render_template('index.html')


# first scenario
@app.route('/analysis_one')
def analysis_one():
    try:
        # variables passed to ui
        count_neg_melb = 0
        count_neg_syd = 0
        count_neg_dar = 0
        count_neg_per = 0
        count_neg_ade = 0
        count_neg_bri = 0
        count_neg_hob = 0
        count_neg_can = 0

        server = connect_db()
        db_tweets = server["tweets"]

        # collecting views
        for item in db_tweets.view('group49/melb_neg'):
            count_neg_melb = item["value"]

        for item in db_tweets.view('group49/syd_neg'):
            count_neg_syd = item["value"]

        for item in db_tweets.view('group49/bri_neg'):
            count_neg_bri = item["value"]

        for item in db_tweets.view('group49/can_neg'):
            count_neg_can = item["value"]

        for item in db_tweets.view('group49/ade_neg'):
            count_neg_ade = item["value"]

        for item in db_tweets.view('group49/hob_neg'):
            count_neg_hob = item["value"]

        for item in db_tweets.view('group49/per_neg'):
            count_neg_per = item["value"]

        for item in db_tweets.view('group49/dar_neg'):
            count_neg_dar = item["value"]

        # variable for ui
        melb_neg_mor = 0
        melb_neg_mid = 0
        melb_neg_aft = 0
        melb_neg_eve = 0
        dar_neg_mor = 0
        dar_neg_mid = 0
        dar_neg_aft = 0
        dar_neg_eve = 0
        syd_neg_mor = 0
        syd_neg_mid = 0
        syd_neg_aft = 0
        syd_neg_eve = 0
        bri_neg_mor = 0
        bri_neg_mid = 0
        bri_neg_aft = 0
        bri_neg_eve = 0
        can_neg_mor = 0
        can_neg_mid = 0
        can_neg_aft = 0
        can_neg_eve = 0
        per_neg_mor = 0
        per_neg_mid = 0
        per_neg_aft = 0
        per_neg_eve = 0
        hob_neg_mor = 0
        hob_neg_mid = 0
        hob_neg_aft = 0
        hob_neg_eve = 0
        ade_neg_mor = 0
        ade_neg_mid = 0
        ade_neg_aft = 0
        ade_neg_eve = 0

        #server = connect_db()
        #db_tweets = server["tweets"]

        # collecting views
        for item in db_tweets.view('group49/melb_neg_morn'):
            melb_neg_mor = item["value"]
        for item in db_tweets.view('group49/melb_neg_afternoon'):
            melb_neg_aft = item["value"]
        for item in db_tweets.view('group49/melb_neg_even'):
            melb_neg_eve = item["value"]
        for item in db_tweets.view('group49/melb_neg_midnight'):
            melb_neg_mid = item["value"]

        for item in db_tweets.view('group49/syd_neg_morn'):
            syd_neg_mor = item["value"]
        for item in db_tweets.view('group49/syd_neg_afternoon'):
            syd_neg_aft = item["value"]
        for item in db_tweets.view('group49/syd_neg_even'):
            syd_neg_eve = item["value"]
        for item in db_tweets.view('group49/syd_neg_midnight'):
            syd_neg_mid = item["value"]

        for item in db_tweets.view('group49/dar_neg_morn'):
            dar_neg_mor = item["value"]
        for item in db_tweets.view('group49/dar_neg_afternoon'):
            dar_neg_aft = item["value"]
        for item in db_tweets.view('group49/dar_neg_even'):
            dar_neg_eve = item["value"]
        for item in db_tweets.view('group49/dar_neg_midnight'):
            dar_neg_mid = item["value"]

        for item in db_tweets.view('group49/hob_neg_morn'):
            hob_neg_mor = item["value"]
        for item in db_tweets.view('group49/hob_neg_afternoon'):
            hob_neg_aft = item["value"]
        for item in db_tweets.view('group49/hob_neg_even'):
            hob_neg_eve = item["value"]
        for item in db_tweets.view('group49/hob_neg_midnight'):
            hob_neg_mid = item["value"]

        for item in db_tweets.view('group49/per_neg_morn'):
            per_neg_mor = item["value"]
        for item in db_tweets.view('group49/per_neg_afternoon'):
            per_neg_aft = item["value"]
        for item in db_tweets.view('group49/per_neg_even'):
            per_neg_eve = item["value"]
        for item in db_tweets.view('group49/per_neg_midnight'):
            per_neg_mid = item["value"]

        for item in db_tweets.view('group49/ade_neg_morn'):
            ade_neg_mor = item["value"]
        for item in db_tweets.view('group49/ade_neg_afternoon'):
            ade_neg_aft = item["value"]
        for item in db_tweets.view('group49/ade_neg_even'):
            ade_neg_eve = item["value"]
        for item in db_tweets.view('group49/ade_neg_midnight'):
            ade_neg_mid = item["value"]

        for item in db_tweets.view('group49/bri_neg_morn'):
            bri_neg_mor = item["value"]
        for item in db_tweets.view('group49/bri_neg_afternoon'):
            bri_neg_aft = item["value"]
        for item in db_tweets.view('group49/bri_neg_even'):
            bri_neg_eve = item["value"]
        for item in db_tweets.view('group49/bri_neg_midnight'):
            bri_neg_mid = item["value"]

        for item in db_tweets.view('group49/can_neg_morn'):
            can_neg_mor = item["value"]
        for item in db_tweets.view('group49/can_neg_afternoon'):
            can_neg_aft = item["value"]
        for item in db_tweets.view('group49/can_neg_even'):
            can_neg_eve = item["value"]
        for item in db_tweets.view('group49/can_neg_midnight'):
            can_neg_mid = item["value"]

        response_tweet_score.update({
            "melb_mor": melb_neg_mor/count_neg_melb,
            "melb_aft": melb_neg_aft/count_neg_melb,
            "melb_eve": melb_neg_eve/count_neg_melb,
            "melb_mid": melb_neg_mid/count_neg_melb,
            "syd_mor": syd_neg_mor/count_neg_syd,
            "syd_aft": syd_neg_aft/count_neg_syd,
            "syd_eve": syd_neg_eve/count_neg_syd,
            "syd_mid": syd_neg_mid/count_neg_syd,
            "dar_mor": dar_neg_mor/count_neg_dar,
            "dar_aft": dar_neg_aft/count_neg_dar,
            "dar_eve": dar_neg_eve/count_neg_dar,
            "dar_mid": dar_neg_mid/count_neg_dar,
            "hob_mor": hob_neg_mor/count_neg_hob,
            "hob_aft": hob_neg_aft/count_neg_hob,
            "hob_eve": hob_neg_eve/count_neg_hob,
            "hob_mid": hob_neg_mid/count_neg_hob,
            "bri_mor": bri_neg_mor/count_neg_bri,
            "bri_aft": bri_neg_aft/count_neg_bri,
            "bri_eve": bri_neg_eve/count_neg_bri,
            "bri_mid": bri_neg_mid/count_neg_bri,
            "per_mor": per_neg_mor/count_neg_per,
            "per_aft": per_neg_aft/count_neg_per,
            "per_eve": per_neg_eve/count_neg_per,
            "per_mid": per_neg_mid/count_neg_per,
            "can_mor": can_neg_mor/count_neg_can,
            "can_aft": can_neg_aft/count_neg_can,
            "can_eve": can_neg_eve/count_neg_can,
            "can_mid": can_neg_mid/count_neg_can,
            "ade_mor": ade_neg_mor/count_neg_ade,
            "ade_aft": ade_neg_aft/count_neg_ade,
            "ade_eve": ade_neg_eve/count_neg_ade,
            "ade_mid": ade_neg_mid/count_neg_ade
        })
        return render_template('analysis_one.html', response_tweet_score=response_tweet_score)
    except Exception as e:
        print(e)


# second scenario
@app.route('/analysis_two')
def analysis_two():
    try:
        # tweets based on sports
        melb_sports = 0
        syd_sports = 0
        per_sports = 0
        ade_sports = 0
        can_sports = 0
        hob_sports = 0
        bri_sports = 0
        dar_sports = 0
        server = connect_db()
        db_tweets = server["tweets"]

        # collecting views
        for item in db_tweets.view('group49/melb_sports'):
            melb_sports = item["value"]

        for item in db_tweets.view('group49/syd_sports'):
            syd_sports = item["value"]

        for item in db_tweets.view('group49/bri_sports'):
            bri_sports = item["value"]

        for item in db_tweets.view('group49/can_sports'):
            can_sports = item["value"]

        for item in db_tweets.view('group49/ade_sports'):
            ade_sports = item["value"]

        for item in db_tweets.view('group49/hob_sports'):
            hob_sports = item["value"]

        for item in db_tweets.view('group49/per_sports'):
            per_sports = item["value"]

        for item in db_tweets.view('group49/dar_sports'):
            dar_sports = item["value"]

        response_sports.update({
            "Melbourne": melb_sports,
            "Sydney": syd_sports,
            "Darwin": dar_sports,
            "Hobart": hob_sports,
            "Adelaide": ade_sports,
            "Brisbane": bri_sports,
            "Perth": per_sports,
            "Canberra": can_sports
        })
        # aurin data for gambling and population
        db = server["aurin"]
        rows = db.view('_all_docs', include_docs=True)
        data = [row['doc'] for row in rows]
        for d in data:
            response_gamble.update({d['city']: d['gambling_activities']})
        for d1 in data:
            response_tot_persons.update({d1['city']: d1['total_persons']})
        return render_template('analysis_two.html', response_sports=response_sports,
                               response_tot_persons=response_tot_persons, response_gamble=response_gamble)
    except Exception as e:
        print(e)


# third scenario
@app.route('/analysis_three')
def analysis_three():
    try:
        # variables passed to ui
        count_neg_melb = 0
        count_neg_syd = 0
        count_neg_dar = 0
        count_neg_per = 0
        count_neg_ade = 0
        count_neg_bri = 0
        count_neg_hob = 0
        count_neg_can = 0
        count_pos_melb = 0
        count_pos_syd = 0
        count_pos_dar = 0
        count_pos_per = 0
        count_pos_ade = 0
        count_pos_bri = 0
        count_pos_hob = 0
        count_pos_can = 0

        server = connect_db()
        db_tweets = server["tweets"]

        # collecting views
        for item in db_tweets.view('group49/melb_pos'):
            count_pos_melb = item["value"]
        for item in db_tweets.view('group49/melb_neg'):
            count_neg_melb = item["value"]
        melb_score = count_pos_melb / count_neg_melb

        for item in db_tweets.view('group49/syd_pos'):
            count_pos_syd = item["value"]
        for item in db_tweets.view('group49/syd_neg'):
            count_neg_syd = item["value"]
        syd_score = count_pos_syd / count_neg_syd

        for item in db_tweets.view('group49/bri_pos'):
            count_pos_bri = item["value"]
        for item in db_tweets.view('group49/bri_neg'):
            count_neg_bri = item["value"]
        bri_score = count_pos_bri / count_neg_bri

        for item in db_tweets.view('group49/can_pos'):
            count_pos_can = item["value"]
        for item in db_tweets.view('group49/can_neg'):
            count_neg_can = item["value"]
        can_score = count_pos_can / count_neg_can

        for item in db_tweets.view('group49/ade_pos'):
            count_pos_ade = item["value"]
        for item in db_tweets.view('group49/ade_neg'):
            count_neg_ade = item["value"]
        ade_score = count_pos_ade / count_neg_ade

        for item in db_tweets.view('group49/hob_pos'):
            count_pos_hob = item["value"]
        for item in db_tweets.view('group49/hob_neg'):
            count_neg_hob = item["value"]
        hob_score = count_pos_hob / count_neg_hob

        for item in db_tweets.view('group49/per_pos'):
            count_pos_per = item["value"]
        for item in db_tweets.view('group49/per_neg'):
            count_neg_per = item["value"]
        per_score = count_pos_per / count_neg_per

        for item in db_tweets.view('group49/dar_pos'):
            count_pos_dar = item["value"]
        for item in db_tweets.view('group49/dar_neg'):
            count_neg_dar = item["value"]
        dar_score = count_pos_dar / count_neg_dar

        response_neg_score.update({
            "Melbourne": melb_score,
            "Sydney": syd_score,
            "Darwin": dar_score,
            "Hobart": hob_score,
            "Adelaide": ade_score,
            "Brisbane": bri_score,
            "Perth": per_score,
            "Canberra": can_score
        })
        # aurin data for married people and population
        db = server["aurin"]
        rows = db.view('_all_docs', include_docs=True)
        data = [row['doc'] for row in rows]
        for d in data:
            response_married.update({d['city']: d['married_persons']})
        for d1 in data:
            response_tot_persons_score.update({d1['city']: d1['total_persons']})
        return render_template('analysis_three.html', response_neg_score=response_neg_score,
                               response_married=response_married, response_tot_persons_score=response_tot_persons_score)
    except Exception as e:
        print(e)

# fourth scenario
@app.route('/analysis_four')
def analysis_four():
    try:
        # tweets based on sports
        melb_sports = 0
        syd_sports = 0
        per_sports = 0
        ade_sports = 0
        can_sports = 0
        hob_sports = 0
        bri_sports = 0
        dar_sports = 0
        server = connect_db()
        db_tweets = server["tweets"]

        # collecting views
        for item in db_tweets.view('group49/melb_sports'):
            melb_sports = item["value"]

        for item in db_tweets.view('group49/syd_sports'):
            syd_sports = item["value"]

        for item in db_tweets.view('group49/bri_sports'):
            bri_sports = item["value"]

        for item in db_tweets.view('group49/can_sports'):
            can_sports = item["value"]

        for item in db_tweets.view('group49/ade_sports'):
            ade_sports = item["value"]

        for item in db_tweets.view('group49/hob_sports'):
            hob_sports = item["value"]

        for item in db_tweets.view('group49/per_sports'):
            per_sports = item["value"]

        for item in db_tweets.view('group49/dar_sports'):
            dar_sports = item["value"]

        response_sports.update({
            "Melbourne": melb_sports,
            "Sydney": syd_sports,
            "Darwin": dar_sports,
            "Hobart": hob_sports,
            "Adelaide": ade_sports,
            "Brisbane": bri_sports,
            "Perth": per_sports,
            "Canberra": can_sports
        })
        # aurin data for income
        db = server["aurin"]
        rows = db.view('_all_docs', include_docs=True)
        data = [row['doc'] for row in rows]
        for d in data:
            response_income.update({d['city']: d['median_income']})

        return render_template('analysis_four.html', response_sports=response_sports, response_income=response_income)
    except Exception as e:
        print(e)



# main
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-ip', type=str, help='start or terminate')
    parser.add_argument('-p', type=int, default=1, help='instance count')
    args = parser.parse_args()
    app.run(host=args.ip, port=args.p)
