from pymol import cmd

# Preliminary settings
cmd.bg_color("white")
cmd.remove("hydrogen")
cmd.remove("solvent")

# Consolidated cylinder settings
for setting in ["render", "alignment", "dash", "line", "mesh", "nonbonded", "ribbon", "stick"]:
    cmd.set(f"{setting}_as_cylinders", "on")
cmd.set("dot_as_spheres", "on")

# Ray tracing settings
cmd.set("antialias", 2)
cmd.set("antialias_shader", 2)
cmd.set("ray_trace_mode", 0)
cmd.set("ray_shadows", 1)

# Material properties
for prop, val in [("shininess", 10), ("ambient", 0.25), ("direct", 0.9), 
                   ("reflect", 0.1), ("specular", 0), ("fog", 0), ("transparency", 0.6)]:
    cmd.set(prop, val)

# Cartoon/stick quality
for prop, val in [("cartoon_dumbbell_length", 1.4), ("cartoon_sampling", 14), 
                   ("ribbon_sampling", 10), ("stick_quality", 15), 
                   ("cartoon_ladder_mode", 1), ("stick_radius", 0.3), 
                   ("dash_radius", 0.15)]:
    cmd.set(prop, val)

# Initial display
cmd.delete("hbonds")
cmd.hide("everything")
cmd.show("cartoon")
cmd.hide("labels")
cmd.color("teal", "all")
cmd.util.cnc("all")

# Helper function
def parse_chains(chain_arg):
    """Parse chain argument into selection string."""
    if "+" in chain_arg:
        return " or ".join([f"chain {c}" for c in chain_arg.split("+")])
    return f"chain {chain_arg}"

def cleanup(_self=cmd):
    """Common cleanup operations."""
    cmd.hide("sticks", "all")
    cmd.delete("hbonds")

def binder(chains, _self=cmd):
    cleanup()
    binder_sel = parse_chains(chains)
    target_sel = f"not ({binder_sel})"
    
    cmd.color("salmon", binder_sel)
    cmd.color("teal", target_sel)
    cmd.show("sticks", f"byres (({binder_sel}) within 4 of ({target_sel}))")
    cmd.util.cnc("all")

def interface(*args, zoom=False, _self=cmd):
    cleanup()
    
    entities = []
    if not args:
        entities = [[c] for c in cmd.get_chains()]
    else:
        for arg in args:
            entities.append(arg.split("+") if "+" in arg else [arg])
    
    colors = ["salmon", "teal", "lightblue", "palegreen", "wheat", "lightpink", "paleyellow", "lightorange"]
    
    # Color entities
    for i, entity in enumerate(entities):
        entity_sel = " or ".join([f"chain {c}" for c in entity])
        cmd.color(colors[i % len(colors)], entity_sel)
    
    # Build interface selection
    interface_residues = []
    for i, entity in enumerate(entities):
        entity_sel = " or ".join([f"chain {c}" for c in entity])
        other_chains = [c for j, e in enumerate(entities) if j != i for c in e]
        
        if other_chains:
            other_sel = " or ".join([f"chain {c}" for c in other_chains])
            interface_residues.append(f"(({entity_sel}) within 4 of ({other_sel}))")
    
    if interface_residues:
        full_sel = f"byres ({' or '.join(interface_residues)})"
        cmd.show("sticks", full_sel)
        cmd.util.cnc("all")
        
        # Add hydrogen bonds
        for i, entity in enumerate(entities):
            entity_sel = " or ".join([f"chain {c}" for c in entity])
            other_chains = [c for j, e in enumerate(entities) if j != i for c in e]
            
            if other_chains:
                other_sel = " or ".join([f"chain {c}" for c in other_chains])
                cmd.distance("hbonds", f"({entity_sel}) within 4 of ({other_sel})", 
                           f"({other_sel}) within 4 of ({entity_sel})", 
                           cutoff=3.5, mode=2, label=0)
        
        cmd.hide("labels", "hbonds")
        
        if zoom:
            cmd.zoom(full_sel, 2)

def zoom_interface(_self=cmd):
    interface(zoom=True, _self=_self)

def color_by_b(_self=cmd):
    cmd.spectrum("b", "rainbow", "all")
    cmd.show("cartoon", "all")
    cmd.cartoon("automatic", "all")
    
    # Putty settings
    for prop, val in [("cartoon_putty_radius", 0.3), ("cartoon_putty_scale_min", 1.0),
                       ("cartoon_putty_scale_max", 5.0), ("cartoon_putty_transform", 0),
                       ("cartoon_putty_range", 1.0)]:
        cmd.set(prop, val)
    
    cmd.cartoon("putty", "all")
    cmd.rebuild()
    cmd.util.cnc("all")

def color_by_plddt(*args, _self=cmd):
    if not args:
        sel = "all"
    else:
        chains = [p.strip() for arg in args for p in arg.split('+')]
        sel = f"({' or '.join([f'chain {c}' for c in chains])})"

    cmd.alter(sel, "q = b")
    cmd.alter(sel, "b = 100 - q")
    cmd.spectrum("q", "red_white_blue", sel, minimum=50, maximum=100)
    cmd.show("cartoon", sel)
    cmd.cartoon("automatic", sel)
    cmd.cartoon("putty", f"{sel} and (q < 85)")
    
    for prop, val in [("cartoon_putty_radius", 0.4), ("cartoon_putty_scale_min", 1.0),
                       ("cartoon_putty_scale_max", 5.0), ("cartoon_putty_transform", 0),
                       ("cartoon_putty_range", 3.0)]:
        cmd.set(prop, val)
    
    cmd.rebuild()
    cmd.util.cnc(sel)
    cmd.alter(sel, "b = q")

def clean(_self=cmd):
    cmd.hide("sticks", "all")
    cmd.delete("hbonds")
    for rep in ["surface", "mesh", "labels"]:
        cmd.hide(rep, "all")
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

