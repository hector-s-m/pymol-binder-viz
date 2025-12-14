from pymol import cmd

# Preliminary settings
cmd.bg_color("white")
cmd.remove("hydrogen")
cmd.remove("solvent")
cmd.set("render_as_cylinders", "on")
cmd.set("alignment_as_cylinders", "on")
cmd.set("dash_as_cylinders", "on")
cmd.set("line_as_cylinders", "on")
cmd.set("mesh_as_cylinders", "on")
cmd.set("nonbonded_as_cylinders", "on")
cmd.set("ribbon_as_cylinders", "on")
cmd.set("stick_as_cylinders", "on")
cmd.set("dot_as_spheres", "on")
cmd.set("antialias", 2)
cmd.set("antialias_shader", 2)
cmd.set("ray_trace_mode", 0)
cmd.set("ray_shadows", 1)
cmd.set("shininess", 10)
cmd.set("ambient", 0.25)
cmd.set("direct", 0.9)
cmd.set("reflect", 0.1)
cmd.set("specular", 0)
cmd.set("fog", 0)
cmd.set("transparency", 0.6)
cmd.set("stick_as_cylinders", "on")
cmd.set("cartoon_dumbbell_length", 1.4)
cmd.set("cartoon_sampling", 14)
cmd.set("ribbon_sampling", 10)
cmd.set("stick_quality", 15)
cmd.set("cartoon_ladder_mode", 1)
cmd.set("stick_radius", 0.3)
cmd.delete("hbonds")
cmd.hide("everything")
cmd.hide("sticks")
cmd.show("cartoon")
cmd.hide("labels")
cmd.color("teal", "all")
cmd.util.cnc("all")

def binder(chains, _self=cmd):
    cmd.hide("sticks", "all")
    cmd.delete("hbonds")
    
    if "+" in chains:
        chain_list = chains.split("+")
        binder_sel = " or ".join([f"chain {c}" for c in chain_list])
    else:
        binder_sel = f"chain {chains}"
    
    target_sel = f"not ({binder_sel})"
    
    cmd.color("salmon", binder_sel)
    cmd.color("teal", target_sel)
    cmd.show("sticks", f"byres (({binder_sel}) within 4 of ({target_sel}))")
    cmd.util.cnc("all")
    

def interface(*args, _self=cmd):
    cmd.hide("sticks", "all")
    cmd.delete("hbonds")
    
    if not args:
        chains = cmd.get_chains()
        entities = [[c] for c in chains]
    else:
        entities = []
        for arg in args:
            if "+" in arg:
                entities.append(arg.split("+"))
            else:
                entities.append([arg])
    
    colors = ["salmon", "teal", "lightblue", "palegreen", "wheat", "lightpink", "paleyellow", "lightorange"]
    
    for i, entity in enumerate(entities):
        color = colors[i % len(colors)]
        entity_sel = " or ".join([f"chain {c}" for c in entity])
        cmd.color(color, entity_sel)
    
    interface_residues = []
    for i, entity in enumerate(entities):
        entity_sel = " or ".join([f"chain {c}" for c in entity])
        other_entities = [e for j, e in enumerate(entities) if j != i]
        
        if other_entities:
            other_chains = []
            for other_entity in other_entities:
                other_chains.extend(other_entity)
            other_sel = " or ".join([f"chain {c}" for c in other_chains])
            interface_residues.append(f"(({entity_sel}) within 4 of ({other_sel}))")
    
    if interface_residues:
        full_sel = f"byres ({' or '.join(interface_residues)})"
        cmd.show("sticks", full_sel)
        cmd.util.cnc("all")
        
        for i, entity in enumerate(entities):
            entity_sel = " or ".join([f"chain {c}" for c in entity])
            other_entities = [e for j, e in enumerate(entities) if j != i]
            
            if other_entities:
                other_chains = []
                for other_entity in other_entities:
                    other_chains.extend(other_entity)
                other_sel = " or ".join([f"chain {c}" for c in other_chains])
                cmd.distance("hbonds", f"({entity_sel}) within 4 of ({other_sel})", f"({other_sel}) within 4 of ({entity_sel})", cutoff=3.5, mode=2, label=0)
        
        cmd.hide("labels", "hbonds")
        # cmd.zoom("hbonds", 1)

def zoom_interface(_self=cmd):
    cmd.hide("sticks", "all")
    cmd.delete("hbonds")
    
    chains = cmd.get_chains()
    entities = [[c] for c in chains]
    
    colors = ["salmon", "teal", "lightblue", "palegreen", "wheat", "lightpink", "paleyellow", "lightorange"]
    
    for i, entity in enumerate(entities):
        color = colors[i % len(colors)]
        entity_sel = " or ".join([f"chain {c}" for c in entity])
        cmd.color(color, entity_sel)
    
    interface_residues = []
    for i, entity in enumerate(entities):
        entity_sel = " or ".join([f"chain {c}" for c in entity])
        other_entities = [e for j, e in enumerate(entities) if j != i]
        
        if other_entities:
            other_chains = []
            for other_entity in other_entities:
                other_chains.extend(other_entity)
            other_sel = " or ".join([f"chain {c}" for c in other_chains])
            interface_residues.append(f"(({entity_sel}) within 4 of ({other_sel}))")
    
    if interface_residues:
        full_sel = f"byres ({' or '.join(interface_residues)})"
        cmd.show("sticks", full_sel)
        cmd.util.cnc("all")
        
        for i, entity in enumerate(entities):
            entity_sel = " or ".join([f"chain {c}" for c in entity])
            other_entities = [e for j, e in enumerate(entities) if j != i]
            
            if other_entities:
                other_chains = []
                for other_entity in other_entities:
                    other_chains.extend(other_entity)
                other_sel = " or ".join([f"chain {c}" for c in other_chains])
                cmd.distance("hbonds", f"({entity_sel}) within 4 of ({other_sel})", f"({other_sel}) within 4 of ({entity_sel})", cutoff=3.5, mode=2, label=0)
        
        cmd.hide("labels", "hbonds")
        cmd.zoom(full_sel, 2)

def color_by_b(_self=cmd):
    cmd.spectrum("b", "rainbow", "all")
    cmd.show("cartoon", "all")
    cmd.cartoon("automatic", "all")
    cmd.set("cartoon_putty_radius", 0.3)
    cmd.set("cartoon_putty_scale_min", 1.0)
    cmd.set("cartoon_putty_scale_max", 5.0)
    cmd.set("cartoon_putty_transform", 0) # High B = Thick
    cmd.set("cartoon_putty_range", 1.0)
    cmd.cartoon("putty", "all")
    cmd.rebuild()
    cmd.util.cnc("all")

def color_by_plddt(*args, _self=cmd):
    if not args:
        sel = "all"
    else:
        chains = []
        for arg in args:
            parts = arg.split('+')
            chains.extend([p.strip() for p in parts])
        
        sel_list = [f"chain {c}" for c in chains]
        sel = f"({' or '.join(sel_list)})"

    cmd.alter(sel, "q = b")
    cmd.alter(sel, "b = 100 - q")
    cmd.spectrum("q", "red_white_blue", sel, minimum=50, maximum=100)
    cmd.show("cartoon", sel)
    cmd.cartoon("automatic", sel)
    cmd.cartoon("putty", f"{sel} and (q < 85)")
    cmd.set("cartoon_putty_radius", 0.3)
    cmd.set("cartoon_putty_scale_min", 1.0)
    cmd.set("cartoon_putty_scale_max", 5.0)
    cmd.set("cartoon_putty_transform", 0)
    cmd.set("cartoon_putty_range", 3.0)
    cmd.rebuild()
    cmd.util.cnc(sel)
    cmd.alter(sel, "b = q")

def clean(_self=cmd):
    cmd.hide("sticks", "all")
    cmd.delete("hbonds")
    cmd.hide("surface", "all")
    cmd.hide("mesh", "all")
    cmd.hide("labels", "all")
    cmd.show("cartoon", "all")
    cmd.cartoon("automatic", "all")
    cmd.color("teal", "all")
    cmd.util.cnc("all")
    cmd.zoom("all")

cmd.extend("binder", binder)
cmd.extend("interface", interface)
cmd.extend("zoom_interface", zoom_interface)
cmd.extend("color_by_b", color_by_b)
cmd.extend("color_by_plddt", color_by_plddt)
cmd.extend("clean", clean)
