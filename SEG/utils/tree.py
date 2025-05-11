from graphviz import Digraph
import SEG.config as cfg

from SEG.state import state


def build_tree():
    dot = Digraph(comment="Evolution Tree")
    for agent in state.all_agents.values():
        birth_year = agent.birth_tick // cfg.ticks_per_year

        if agent.death_tick is None:
            life_str = f"{birth_year}"
        else:
            death_year = agent.death_tick // cfg.ticks_per_year
            life_str = f"{birth_year}-{death_year}"

        label = f"ID:{agent.id}\\nSp:{agent.speed:.2f}\\n{life_str}"
        dot.node(str(agent.id), label, style="filled", fillcolor="#%02x%02x%02x" % agent.color)

        if agent.parent_id:
            dot.edge(str(agent.parent_id), str(agent.id))

    dot.render('evolution_tree.gv', view=True)
