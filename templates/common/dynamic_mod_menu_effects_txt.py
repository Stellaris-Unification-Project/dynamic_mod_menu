from templates.utils import settings, templater

template = """
dmm_mod_{main_event}_{secondary_event} = {{
    potential = {{
        has_global_flag = dmm_mod_{main_event}_{secondary_event}_active
    }}
    allow = {{
        NOR = {{
            has_global_flag = dmm_mod_{secondary_event}_opened
            has_global_flag = dmm_mod_{secondary_event}_disabled
        }}
    }}
    effect = {{
        hidden_effect = {{            
            country_event = {{
                id = dmm_prepare_mod.{secondary_event}
            }}
        }}
    }}
}}"""


def process(publish_dir):
    mod_lines = []
    for i in range(1, settings.items_per_page + 1):
        for j in range(i, settings.total + 1):
            mod_lines.append(template.format(main_event=i, secondary_event=j))

    templater.process_file(
        publish_dir + "/common/button_effects/dynamic_mod_menu_effects.txt",
        effects=mod_lines)
