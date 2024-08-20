import numpy as nOptions
import matplotlib.pyplot  as plt
import string, random

labels = ["Virginia minimum wage",
            "UVA CS stipend Tier 1",
            "UVA CS stipend Tier 2",
            "UVA CS stipend Tier 3",
            # "Charlottesville living wage"
]

values = [24960.00,
            35022.00,
            36504.00,
            38012.00,
            # 38688.00
]

def vertical_bar():
    # creating the dataset
    data = {"Virginia \nminimum wage": 24960,
            "CS stipend Tier 1": 35022,
            "CS stipend Tier 2": 36504,
            "CS stipend Tier 3": 38012,
            }
    courses = list(data.keys())
    values = list(data.values())
    
    fig, ax = plt.subplots(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon', width = 0.4)
    
    plt.ylabel("Yearly income before tax", fontsize=18)
    plt.yticks([0, 10000, 20000, 30000, 40000],
                ["0", "$10,000", "$20,000", "$30,000", "$40,000"],
                fontsize = 12, 
                rotation=20
              )
    # Add x, y gridlines
    plt.grid(axis = 'y')
    ax.tick_params(axis='both', which='major', labelsize=12)
    # Show top values
    # ax.invert_yaxis()
    
    # # Add annotation to bars
    # for i in ax.patches:
    #     plt.text(i.get_width()+0.2, i.get_y()+0.5,
    #             str(round((i.get_width()), 2)),
    #             fontsize = 10, fontweight ='bold',
    #             color ='grey')
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i,y[i]+125,
                        # f"${y[i]:.2f}",
                        f'${int(y[i]):,}',
                        fontsize = 12, 
                        # fontweight ='bold', 
                        ha='center')
    
    ax.hlines(y=[38688.00], xmin=-0.5, xmax=len(courses)-0.5, colors='purple', linestyles='--', lw=1, label="Charlottesville \nliving wage")

    addlabels(courses, values)

    # plt.title("Students enrolled in different courses")
    plt.show()
    plt.legend(loc=2, prop={'size': 12})
    randomhash = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    plt.savefig(f"temp-{randomhash}.png")


vertical_bar()