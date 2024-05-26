#this fle containt database related queary 

# from src.flask_app import app
import mysql.connector
from mysql.connector import errorcode
import json
import datetime

config = {
        'user': 'root',#user name
        'password': '', #password
        'host': 'localhost', #host name
        'database': 'fldbms', #database name
        'raise_on_warnings': True
    }


try: 
    database = mysql.connector.connect(**config)
    print("database connected")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

class CreateTables():
    def __init__(self) -> None:
        global database
        if database.is_connected():
            print("database already connected..")
            self.database = database   
        else:
            try: 
                # global database
                database = mysql.connector.connect(**config)
                print("cursor created")
                self.database = database
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)
                        
            # self.database = database
        self.cursor = self.database.cursor()
        try:
            q = self.CreatPlayers()
            self.cursor.execute(q)
        except Exception as e:
            print("Error:" ,e)
        try:
            q = self.TitleSponsor()
            self.cursor.execute(q)
        except Exception as e:
            print("TitleSponsor" ,e)
        try:
            q = self.TeamOwner()
            self.cursor.execute(q)
        except Exception as e:
            print("Error:" ,e)
        try:
            q = self.HeadCoach()
            self.cursor.execute(q)
        except Exception as e:
            print("Error:" ,e)
        try:
            q = self.Teams()
            self.cursor.execute(q)
        except Exception as e:
            print("Error:" ,e)
        try:
            q = self.Umpire()
            self.cursor.execute(q)
        except Exception as e:
            print("Error:" ,e)
        try:
            q = self.Stadium()
            self.cursor.execute(q)
        except Exception as e:
            print("Error:" ,e)
        try:
            q = self.Matchs()
            self.cursor.execute(q)
        except Exception as e:
            print("Error:" ,e)
        try:
            q = self.UmpiredBy()
            self.cursor.execute(q)
        except Exception as e:
            print("Error:" ,e)
        try:
            q = self.IPL()
            self.cursor.execute(q)
        except Exception as e:
            print("Error:" ,e)
        try:
            q = self.TeamDetails()
            self.cursor.execute(q)
        except Exception as e:
            print("Error:" ,e)
        try:
            q = self.YearwisePlayerDetails()
            self.cursor.execute(q)
        except Exception as e:
            print("Error:" ,e)
        try:
            q = self.Played()
            self.cursor.execute(q)
        except Exception as e:
            print("Error:" ,e)
        self.cursor.close()
        database.commit()
        # self.database.close()
        
        
    def CreatPlayers(self):
        queary = """CREATE TABLE IF NOT EXISTS Players(
                    PlayerID CHARACTER(5) PRIMARY KEY,
                    name varchar(50),
                    Nationality  VARCHAR(50) NOT NULL,
                    DoB DATE NOT NULL,
                    Role  VARCHAR(50),
                    StrikeRate DECIMAL(5,2),
                    BowlingStyle  VARCHAR(50),
                    BattingStyle  VARCHAR(50)	
                    );"""
        return queary
    def TeamOwner(self):
        query = """CREATE TABLE IF NOT EXISTS TeamOwner(
                CompanyName VARCHAR(50) PRIMARY KEY,
                BusinessDomain VARCHAR(50) NOT NULL,
                Country VARCHAR(50) NOT NULL	
            );"""
        return query
    def TitleSponsor(self):
        query  = """CREATE TABLE IF NOT EXISTS TitleSponsor(
                CompanyName VARCHAR(50) PRIMARY KEY,
                BusinessDomain VARCHAR(50) NOT NULL,
                Country VARCHAR(50) NOT NULL	
            );"""
        return query
    def HeadCoach(self):
        query = """CREATE TABLE IF NOT EXISTS HeadCoach(
                    CoachID CHARACTER(5) PRIMARY KEY,
                    CoachName VARCHAR(50) NOT NULL,
                    Years_of_Experience SMALLINT,
                    DoB DATE NOT NULL,
                    Country VARCHAR(50) NOT NULL
                );"""
        return query
    def Teams(self):
        query = """CREATE TABLE IF NOT EXISTS Teams(
            TeamID VARCHAR(5) PRIMARY KEY,
            TeamName VARCHAR(50) UNIQUE NOT NULL,
            OwnerCompany VARCHAR(50) NOT NULL,
            FOREIGN KEY(OwnerCompany) REFERENCES TeamOwner(CompanyName)
                ON DELETE CASCADE ON UPDATE CASCADE
        );""" 
        return query
    def Umpire(self):
        query = """CREATE TABLE IF NOT EXISTS Umpire(
                UmpireID CHARACTER(5) PRIMARY KEY,
                Name VARCHAR(50) NOT NULL,
                YearsOfExperience SMALLINT,
                Country VARCHAR(50) NOT NULL	
            );"""
        return query
    def Stadium(self):
        query = """CREATE TABLE IF NOT EXISTS Stadium(
                StadiumName VARCHAR(50),
                City VARCHAR(50),
                Country VARCHAR(50) NOT NULL,
                Capacity INT,
                RentAmount BIGINT,
                PRIMARY KEY (StadiumName, City)
            );"""
        return query
    def Matchs(self):
        query = """CREATE TABLE IF NOT EXISTS Matchs(
                MatchID CHARACTER(7) PRIMARY KEY,
                MatchType VARCHAR(10) NOT NULL,
                Date DATE NOT NULL,
                StadiumName VARCHAR(50) NOT NULL,
                City VARCHAR(50) NOT NULL,
                ManOfTheMatch CHARACTER(5) NOT NULL,
                FOREIGN KEY (StadiumName) REFERENCES Stadium(StadiumName)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (ManOfTheMatch) REFERENCES Players(  PlayerID )
                    ON DELETE CASCADE ON UPDATE CASCADE	
            );"""
        return query
    def UmpiredBy(self):
        query = """CREATE TABLE IF NOT EXISTS UmpiredBy(
                MatchID CHARACTER(7),
                UmpireID CHARACTER(5),
                PRIMARY KEY (MatchID, UmpireID),
                FOREIGN KEY (MatchID) REFERENCES Matchs(MatchID)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (UmpireID) REFERENCES Umpire(UmpireID)
                    ON DELETE CASCADE ON UPDATE CASCADE
            );""" 
        return query
    def IPL(self):
        query = """CREATE TABLE IF NOT EXISTS IPL(
                Year SMALLINT PRIMARY KEY, 
                TitleSponsor VARCHAR(50) NOT NULL,
                ManOfTheSeries CHARACTER(5) NOT NULL,
                ChampionTeam VARCHAR(5) NOT NULL,
                FOREIGN KEY (ChampionTeam) REFERENCES Teams(TeamID)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (TitleSponsor) REFERENCES TitleSponsor(CompanyName)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (ManOfTheSeries) REFERENCES Players(PlayerID)
                    ON DELETE CASCADE ON UPDATE CASCADE
            );"""
        return query
    def TeamDetails(self):
        query = """CREATE TABLE IF NOT EXISTS TeamDetails(
                    TeamID VARCHAR(5),
                    Year SMALLINT,
                    CaptainID CHARACTER(5) NOT NULL,
                        CoachID CHARACTER(5) NOT NULL,
                    SponsorCompany VARCHAR(50) NOT NULL,
                    SponsorAmount BIGINT NOT NULL,	
                    PRIMARY KEY (TeamID, Year),
                    FOREIGN KEY (CaptainID) REFERENCES Players( PlayerID)
                        ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (CoachID) REFERENCES HeadCoach(CoachID)
                        ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (SponsorCompany) REFERENCES TitleSponsor(CompanyName)
                        ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID)
                        ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (Year) REFERENCES IPL(Year )
                        ON DELETE CASCADE ON UPDATE CASCADE
                );"""
        return query
    def YearwisePlayerDetails(self):
        query = """CREATE TABLE IF NOT EXISTS YearwisePlayerDetails(
                    PlayerID CHARACTER(5),
                    Year SMALLINT, 
                    TeamID VARCHAR(5) NOT NULL,
                    TotalWickets INT,
                    TotalRuns INT,
                    MaximumWickets INT,
                    MaximumWicketsRuns INT,
                    MaximumRuns INT,
                    PlayerPrice BIGINT,
                    Out_NotOut BOOLEAN,
                    PRIMARY KEY(PlayerID,Year),
                    FOREIGN KEY (PlayerID) REFERENCES Players( PlayerID )
                        ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (TeamID,Year) REFERENCES TeamDetails(TeamID,year)
                        ON DELETE CASCADE ON UPDATE CASCADE
                );"""
        return query
    def Played(self):
        query = """CREATE TABLE IF NOT EXISTS Played(
                MatchID CHARACTER(7),
                TeamID VARCHAR(5),
                TeamRuns INT NOT NULL,
                4s INT NOT NULL,
                6s INT NOT NULL,
                Wickets INT NOT NULL,
                Winner CHARACTER(1) NOT NULL, 
                PRIMARY KEY(MatchID,TeamID),
                FOREIGN KEY (TeamID) REFERENCES Teams(TeamID)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (MatchID) REFERENCES Matchs(MatchID)
                    ON DELETE CASCADE ON UPDATE CASCADE
                    );"""
        return query
    # def Pionts(self):
    #     query = """Create table if not exists points(
    #     team varchar(20) NOT NULL,
    #     matches INT NOT NULL,
    #     win int NOT NULL,
    #     loose int NOT NULL,
    #     pts int NOT NULL,
    #     nrr float(2,4) NOT NULL
    #     PRIMARY KEY(MatchID,TeamID),
    #     FOREIGN KEY (TeamID) REFERENCES Teams(TeamID)
    #     ON DELETE CASCADE ON UPDATE CASCADE,
    #     );
    #         """

    
class QuearyExe():
    def __init__(self):
        global database
        if database.is_connected():
            print("database already connected..")
            self.database  = database   
        else:
            try: 
                database = mysql.connector.connect(**config)
                print("Database connected")
                self.databse  = database
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)
                        
        
        # else:
        #     self.database.close()
    def Stduim_details(self):
        self.cursor = self.database.cursor()
        query = "SELECT * FROM Stadium;"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        column_names = [i[0] for i in self.cursor.description]
        json_result = []
        for row in results:
            record = {column_names[i]: row[i] for i in range(len(row))}
            json_result.append(record)
        self.cursor.close()
        return json_result
    def Player_details_by_name(self, team_name):
        query = """select * from Players where name = %s;
        """
        self.cursor = self.database.cursor()
        self.cursor.execute(query, (team_name,))
        results = self.cursor.fetchall()
        column_names = [i[0] for i in self.cursor.description]  
        json_result = {team_name: []}
        
        for result in results:
            player_data = {column_names[i]: str(result[i]) for i in range(len(result))}
            json_result[team_name].append(player_data)

        self.cursor.close()
        return json_result

    
    def TeamPlayer(self,team_name):
        query = """SELECT DISTINCT 
                p.Name, 
                t.teamname
            FROM (
                SELECT 
                    playerid, 
                    teamid
                FROM yearwiseplayerdetails
                GROUP BY playerid, teamid
                HAVING COUNT(DISTINCT teamid) = 1
            ) AS r2
            NATURAL JOIN yearwiseplayerdetails
            NATURAL JOIN players AS p
            JOIN teams AS t ON r2.teamid = t.teamid
            WHERE t.teamname = %s;"""
        self.cursor = self.database.cursor()
        self.cursor.execute(query,(team_name,))
        results = self.cursor.fetchall()
        column_names = [i[0] for i in self.cursor.description]  
        json_result = {}
        
        for j in range(0,len(results)):
            h={}
            for i in range(0,len(results[0])):
                
                h[column_names[i]]=results[j][i]
            json_result[team_name].append(h)
        print(results)
        
        self.cursor.close()
        return json_result
    def getTiltleSponser(self):
        query = "select * from TitleSponsor;"
        self.cursor = self.database.cursor()
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        column_names = [i[0] for i in self.cursor.description]  
        # json_result = {}
        json_result  =[]
        for j in range(0,len(results)):
            h={}
            for i in range(0,len(results[0])):
                
                h[column_names[i]]=str(results[j][i])
            json_result.append(h)
        print(results)
        
        self.cursor.close()
        return json_result


