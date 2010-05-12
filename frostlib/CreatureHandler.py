# -*- coding: cp1252 -*-
import frostlib
class CreatureHandler(object):
    def load_creatures(self):
        """
        Lädt Creatures aus der Datenbank
        """
        resultcount = self.cursor.execute("SELECT * FROM creature_template")
        p = frostlib.ProgressBar(int(resultcount), "Loading Creature Template...")
        pold = str(p)
        count = 0
        result = self.cursor.fetchall()
        for entry in range(0,resultcount):
            currentres = result[entry]
            creature_entry = int(currentres[0])
            creature_name = str(currentres[1])
            creature_subname = str(currentres[2])
            creature_info_str = currentres[3]
            creature_flags1 = int(currentres[4])
            creature_type = int(currentres[5])
            creature_family = int(currentres[6])
            creature_rank = int(currentres[7])
            creature_killcredit1 = int(currentres[8])
            creature_killcredit2 = int(currentres[9])
            creature_male_displayid = int(currentres[10])
            creature_female_displayid = int(currentres[11])
            creature_male_displayid2 = int(currentres[12])
            creature_female_displayid2 = int(currentres[13])
            creature_unknown_float1 = float(currentres[14])
            creature_unknown_float2 = float(currentres[15])
            creature_leader = int(currentres[16])
            creature_questitem1 = int(currentres[17])
            creature_questitem2 = int(currentres[18])
            creature_questitem3 = int(currentres[19])
            creature_questitem4 = int(currentres[20])
            creature_questitem5 = int(currentres[21])
            creature_questitem6 = int(currentres[22])
            creature_pathid = int(currentres[23])
            creature = frostlib.classes.creature(creature_entry,
                                                 creature_name,
                                                 creature_subname,
                                                 creature_info_str,
                                                 creature_flags1,
                                                 creature_type,
                                                 creature_family,
                                                 creature_rank,
                                                 creature_killcredit1,
                                                 creature_killcredit2,
                                                 creature_male_displayid,
                                                 creature_female_displayid,
                                                 creature_male_displayid2,
                                                 creature_female_displayid2,
                                                 creature_unknown_float1,
                                                 creature_unknown_float2,
                                                 creature_leader,
                                                 creature_questitem1,
                                                 creature_questitem2,
                                                 creature_questitem3,
                                                 creature_questitem4,
                                                 creature_questitem5,
                                                 creature_questitem6,
                                                 creature_pathid)

            self.wcreatures[creature_entry] = creature
            count += 1
            p.update_time(entry)
            if str(p) != pold:
                frostlib.slogger.info(str(p))
                pold = str(p)
        frostlib.slogger.info(">>> Loaded " + str(count) + " Creatures")
                        
