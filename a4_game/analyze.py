from unit.base_unit import BaseUnit

def destroy_prob(attacker, defender, current_tile, turns):
    """
    Finds the probability the unit [defender] on [current_tile] will be 
    destroyed by unit [attacker] in at most [turns] turns. Returns a list prob
    where prob[k] gives the probability that [defender] will be destroyed in
    k turns.

    All functions used in this function can be approximated to constant time
    so the only factor that needs to be taken into account in the run time are
    the loops. The turn for loop will run [turns] times. The health loop will
    run 3*[turn]+1 times, which is at most 3*[turns]+1. This is because this is
    the maximum number of possible health values. The bonus loop will run 4 
    times leaving us with O(n*(3n+1)*4) where n is turns. This can be 
    simplified to O(n^2).
    """

    prob = [0]
    base_bonuses = {-1:0.2, 0:0.5, 1:0.2, 2:0.1}
    old_health_prob = {defender.health:1}
    new_health_prob = {}
    base_damage = attacker.get_damage(defender, current_tile)
    for turn in range(turns):
        # Loop through all current possible health values
        for health in old_health_prob:
            # Loop through all bonuses
            for bonus in base_bonuses:
                # Find the health after the damage is applied
                if base_damage + bonus >= 0:
                    new_health = health - (base_damage + bonus)
                else:
                    new_health = health

                # Only allow health to fall to 0 to keep things simple
                if new_health < 0:
                    new_health = 0

                # Add this new health to the probability list
                if new_health not in new_health_prob:
                    new_health_prob[new_health] = 0
                new_health_prob[new_health] += base_bonuses[bonus] * old_health_prob[health]
        
        # Resetting the lists for the next loop iteration
        old_health_prob = new_health_prob
        new_health_prob = {}
        
        if 0 in old_health_prob:
            dest_prob = old_health_prob[0]
        else:
            dest_prob = 0

        # Adding the probability to the return list
        prob.append(dest_prob)

    return prob
            
