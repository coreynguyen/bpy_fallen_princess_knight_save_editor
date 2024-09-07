import bpy
import csv
import os

# Path to the CSV file, dynamically get current user
user = os.getlogin()
csv_path = f"C:/Users/{user}/AppData/LocalLow/mico/FallenPrincessKnight_Steam/savedata.csv"

# Waypoint data (positions and directions)
waypoints = {
    'GOBLIN_CAMP': (572.4157, 3.07945, 443.9324, 234.3869),
    'CHURCH': (372.9255, 3.653744, 577.4875, 328.0068),
    'WELL': (395.1996, -0.05015767, 557.8172, 269.9218),
    'PALE_CAVE': (360.8039, 4.011928, 513.6289, 205.5965),
    'INN': (408.9104, -1.291299, 514.69040, 174.7735),
    'BLACK_SMITH': (415.3052, -1.342147, 531.8901, 17.37041),
    'VILLAGE_ENTRANCE': (448.938, -0.9348211, 493.482, 308.186)
    }

# Function to read the CSV file, handling the UTF-8 BOM
def read_csv(file_path):
    data = []
    if os.path.exists(file_path):  # Check if the file exists
        print(f"File found: {file_path}")
        with open(file_path, mode='r', newline='', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        print("CSV data loaded successfully.")
    else:
        print(f"File not found: {file_path}")
    return data

# Function to write to the CSV file with UTF-8 BOM
def write_csv(file_path, data):
    with open(file_path, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print("CSV data saved successfully.")

# Function to update the position and direction based on the selected waypoint
def update_waypoint(self, context):
    waypoint = self.fpk_location
    if waypoint in waypoints:
        pos_x, pos_y, pos_z, angle = waypoints[waypoint]
        context.scene.fpk_pos_x = pos_x
        context.scene.fpk_pos_y = pos_y
        context.scene.fpk_pos_z = pos_z
        context.scene.fpk_angle = angle

# Function to load values from the CSV and set them to the properties
def load_csv_values(scene):
    data = read_csv(csv_path)
    
    # Flatten the single-row CSV data
    if len(data) > 0:
        data = data[0]  # Flatten the data into a single list
    
    # Correct for base-1 indices by subtracting 1 when accessing data
    try:
        # Experience and Stats fields
        if len(data) > 7:
            scene.fpk_sex = int(data[7])
        if len(data) > 8:
            scene.fpk_vaginal_ejac = int(data[8])
        if len(data) > 9:
            scene.fpk_oral_ejac = int(data[9])
        if len(data) > 10:
            scene.fpk_menstruation = int(data[10])
        if len(data) > 11:
            scene.fpk_ovulated = int(data[11])
        if len(data) > 12:
            scene.fpk_fertilized = int(data[12])
        if len(data) > 13:
            scene.fpk_implanted = int(data[13])
        if len(data) > 14:
            scene.fpk_childbirth = int(data[14])
        if len(data) > 15:
            scene.fpk_raped = int(data[15])
        if len(data) > 16:
            scene.fpk_prostitute = int(data[16])
        if len(data) > 17:
            scene.fpk_yobai = int(data[17])
        if len(data) > 18:
            scene.fpk_fellatio = int(data[18])
        if len(data) > 19:
            scene.fpk_cunnilingus = int(data[19])
        if len(data) > 20:
            scene.fpk_imprisonment = int(data[20])
        if len(data) > 21:
            scene.fpk_battle = int(data[21])
        if len(data) > 22:
            scene.fpk_pushed_down = int(data[22])
        if len(data) > 23:
            scene.fpk_defeat = int(data[23])
        
        # Position and Direction
        if len(data) > 34:
            scene.fpk_pos_x = float(data[34])
        if len(data) > 35:
            scene.fpk_pos_y = float(data[35])
        if len(data) > 36:
            scene.fpk_pos_z = float(data[36])
        if len(data) > 38:
            scene.fpk_angle = float(data[38])
        
        # Player Stats
        if len(data) > 44:
            scene.fpk_stamina = int(data[44])
        if len(data) > 45:
            scene.fpk_cleanliness = int(data[45])
        if len(data) > 46:
            scene.fpk_armor = int(data[46])
        if len(data) > 47:
            scene.fpk_gold = int(data[47])
        if len(data) > 48:
            scene.fpk_creampie = int(data[48])
        
        # Options and Toggles
        if len(data) > 50:
            scene.fpk_windowed = bool(int(data[50]))
        if len(data) > 51:
            resolution_index = int(data[51])
            enum_items = list(scene.bl_rna.properties['fpk_resolution'].enum_items.keys())
            if resolution_index < len(enum_items):
                scene.fpk_resolution = enum_items[resolution_index]
        
        if len(data) > 55:
            scene.fpk_pregnant = bool(int(data[55]))
        if len(data) > 56:
            scene.fpk_birthing = bool(int(data[56]))
        
        if len(data) > 57:
            scene.fpk_brightness = float(data[57])  # Assuming brightness is a float property
        
        if len(data) > 59:
            graphics_index = int(data[59])
            enum_items = list(scene.bl_rna.properties['fpk_graphics_quality'].enum_items.keys())
            if graphics_index < len(enum_items):
                scene.fpk_graphics_quality = enum_items[graphics_index]
        
        if len(data) > 60:
            scene.fpk_blizzard = bool(int(data[60]))
        if len(data) > 61:
            encounter_index = int(data[61])
            enum_items = list(scene.bl_rna.properties['fpk_encounter_rate'].enum_items.keys())
            if encounter_index < len(enum_items):
                scene.fpk_encounter_rate = enum_items[encounter_index]
        
        print("CSV data loaded into properties successfully.")
    
    except Exception as e:
        print(f"Error loading CSV data: {e}")
    
    # Refresh the UI to reflect the updated values
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            area.tag_redraw()
    
    # Refresh the UI to reflect the updated values
    bpy.context.view_layer.update()

# Function to write values from properties back to the CSV
def write_csv_values(scene):
    # Load existing CSV data
    data = read_csv(csv_path)
    
    # Flatten the data into a single list if necessary
    if len(data) > 0:
        data = data[0]
    else:
        data = ['0'] * 200  # Create a default list if CSV is empty
    
    # Update Experience and Stats fields (indices corrected by -1)
    data_length = len(data)
    
    # Ensure the data list is long enough
    if data_length < 200:
        data.extend(['0'] * (200 - data_length))
    
    try:
        # Experience and Stats fields
        data[7] = str(scene.fpk_sex)
        data[8] = str(scene.fpk_vaginal_ejac)
        data[9] = str(scene.fpk_oral_ejac)
        data[10] = str(scene.fpk_menstruation)
        data[11] = str(scene.fpk_ovulated)
        data[12] = str(scene.fpk_fertilized)
        data[13] = str(scene.fpk_implanted)
        data[14] = str(scene.fpk_childbirth)
        data[15] = str(scene.fpk_raped)
        data[16] = str(scene.fpk_prostitute)
        data[17] = str(scene.fpk_yobai)
        data[18] = str(scene.fpk_fellatio)
        data[19] = str(scene.fpk_cunnilingus)
        data[20] = str(scene.fpk_imprisonment)
        data[21] = str(scene.fpk_battle)
        data[22] = str(scene.fpk_pushed_down)
        data[23] = str(scene.fpk_defeat)
        
        # Position and Direction
        data[34] = str(scene.fpk_pos_x)
        data[35] = str(scene.fpk_pos_y)
        data[36] = str(scene.fpk_pos_z)
        data[38] = str(scene.fpk_angle)
        
        # Player Stats
        data[44] = str(scene.fpk_stamina)
        data[45] = str(scene.fpk_cleanliness)
        data[46] = str(scene.fpk_armor)
        data[47] = str(scene.fpk_gold)
        data[48] = str(scene.fpk_creampie)
        
        # Options and Toggles
        data[50] = '1' if scene.fpk_windowed else '0'
        data[51] = str(list(scene.bl_rna.properties['fpk_resolution'].enum_items.keys()).index(scene.fpk_resolution))
        
        data[55] = '1' if scene.fpk_pregnant else '0'
        data[56] = '1' if scene.fpk_birthing else '0'
        
        data[57] = str(scene.fpk_brightness)  # Assuming brightness is a float property
        
        data[59] = str(list(scene.bl_rna.properties['fpk_graphics_quality'].enum_items.keys()).index(scene.fpk_graphics_quality))
        
        data[60] = '1' if scene.fpk_blizzard else '0'
        data[61] = str(list(scene.bl_rna.properties['fpk_encounter_rate'].enum_items.keys()).index(scene.fpk_encounter_rate))
        
        # Write back the modified CSV data
        write_csv(csv_path, data)
        print("CSV data updated successfully.")
        
    except Exception as e:
        print(f"Error writing CSV data: {e}")

# Define Blender properties for the fields in the UI
def register_props():
    # Positions and Direction
    bpy.types.Scene.fpk_pos_x = bpy.props.FloatProperty(name="Position X")
    bpy.types.Scene.fpk_pos_y = bpy.props.FloatProperty(name="Position Y")
    bpy.types.Scene.fpk_pos_z = bpy.props.FloatProperty(name="Position Z")
    bpy.types.Scene.fpk_angle = bpy.props.FloatProperty(name="Direction", min=0.0, max=360.0)
    
    # Player Stats
    bpy.types.Scene.fpk_stamina = bpy.props.IntProperty(name="Stamina", min=0, max=100)
    bpy.types.Scene.fpk_armor = bpy.props.IntProperty(name="Armor", min=0, max=100)
    bpy.types.Scene.fpk_cleanliness = bpy.props.IntProperty(name="Cleanliness", min=0, max=100)
    bpy.types.Scene.fpk_creampie = bpy.props.IntProperty(name="Creampie", min=0, max=100)
    
    # Inventory
    bpy.types.Scene.fpk_gold = bpy.props.IntProperty(name="Gold", min=0, max=99999999)
    
    # Options and Toggles
    bpy.types.Scene.fpk_pregnant = bpy.props.BoolProperty(name="Enable Pregnancy")
    bpy.types.Scene.fpk_birthing = bpy.props.BoolProperty(name="Enable Child Birth")
    bpy.types.Scene.fpk_blizzard = bpy.props.BoolProperty(name="Blizzard Effects")
    bpy.types.Scene.fpk_windowed = bpy.props.BoolProperty(name="Windowed Mode")
    bpy.types.Scene.fpk_brightness = bpy.props.FloatProperty(name="Brightness", min=0.0, max=1.0)
    
    # Experience, Battle, etc.
    bpy.types.Scene.fpk_sex = bpy.props.IntProperty(name="Sex", min=0, max=99999999)
    bpy.types.Scene.fpk_vaginal_ejac = bpy.props.IntProperty(name="Vaginal Ejac", min=0, max=99999999)
    bpy.types.Scene.fpk_oral_ejac = bpy.props.IntProperty(name="Oral Ejac", min=0, max=99999999)
    bpy.types.Scene.fpk_menstruation = bpy.props.IntProperty(name="Menstruation", min=0, max=99999999)
    bpy.types.Scene.fpk_ovulated = bpy.props.IntProperty(name="Ovulated", min=0, max=99999999)
    bpy.types.Scene.fpk_fertilized = bpy.props.IntProperty(name="Fertilized", min=0, max=99999999)
    bpy.types.Scene.fpk_implanted = bpy.props.IntProperty(name="Implanted", min=0, max=99999999)
    bpy.types.Scene.fpk_childbirth = bpy.props.IntProperty(name="Childbirth", min=0, max=99999999)
    
    # More experience and event tracking
    bpy.types.Scene.fpk_raped = bpy.props.IntProperty(name="Raped", min=0, max=99999999)
    bpy.types.Scene.fpk_prostitute = bpy.props.IntProperty(name="Prostitute", min=0, max=99999999)
    bpy.types.Scene.fpk_yobai = bpy.props.IntProperty(name="Yobai", min=0, max=99999999)
    bpy.types.Scene.fpk_fellatio = bpy.props.IntProperty(name="Fellatio", min=0, max=99999999)
    bpy.types.Scene.fpk_cunnilingus = bpy.props.IntProperty(name="Cunnilingus", min=0, max=99999999)
    bpy.types.Scene.fpk_imprisonment = bpy.props.IntProperty(name="Imprisonment", min=0, max=99999999)
    bpy.types.Scene.fpk_battle = bpy.props.IntProperty(name="Battle", min=0, max=99999999)
    bpy.types.Scene.fpk_pushed_down = bpy.props.IntProperty(name="Pushed Down", min=0, max=99999999)
    bpy.types.Scene.fpk_defeat = bpy.props.IntProperty(name="Defeat", min=0, max=99999999)
    
    # Dropdown options
    bpy.types.Scene.fpk_location = bpy.props.EnumProperty(
        name="Waypoint",
        items=[
            ('GOBLIN_CAMP', 'Goblin Camp', ''),
            ('CHURCH', 'Church', ''),
            ('WELL', 'Well', ''),
            ('PALE_CAVE', 'Pale Cave', ''),
            ('INN', 'Inn', ''),
            ('BLACK_SMITH', 'Black Smith', ''),
            ('VILLAGE_ENTRANCE', 'Village Entrance', '')
            ],
        update=update_waypoint  # Call when waypoint changes
        )
    
    bpy.types.Scene.fpk_resolution = bpy.props.EnumProperty(
        name="Resolution",
        items=[
            ('1280x720', '1280 x 720', ''),
            ('1366x768', '1366 x 768', ''),
            ('1440x900', '1440 x 900', ''),
            ('1536x864', '1536 x 864', ''),
            ('1920x1080', '1920 x 1080', ''),
            ('2560x1440', '2560 x 1440', ''),
            ('3840x2160', '3840 x 2160', '')
            ]
        )
    
    bpy.types.Scene.fpk_graphics_quality = bpy.props.EnumProperty(
        name="Graphics Quality",
        items=[
            ('VERY_LOW', 'Very Low', ''),
            ('LOW', 'Low', ''),
            ('MEDIUM', 'Medium', ''),
            ('HIGH', 'High', ''),
            ('VERY_HIGH', 'Very High', ''),
            ('ULTRA', 'Ultra', '')
            ]
        )
    
    bpy.types.Scene.fpk_encounter_rate = bpy.props.EnumProperty(
        name="Encounter Rate",
        items=[
            ('0', 'None', ''),
            ('1', 'Low', ''),
            ('2', 'Medium', ''),
            ('3', 'High', '')
            ]
        )

# Define the panel UI in Blender with collapsible sections
class FPK_PT_Panel(bpy.types.Panel):
    bl_label = "Fallen Princess Knight CSV Editor"
    bl_idname = "FPK_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'FallenPrincessKnight'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        # Group: Location
        box = layout.box()
        box.prop(scene, "fpk_location", text="Waypoint")

        # Group: Position and Direction
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Position and Direction")
        col.prop(scene, "fpk_pos_x", text="Position X")
        col.prop(scene, "fpk_pos_y", text="Position Y")
        col.prop(scene, "fpk_pos_z", text="Position Z")
        col.prop(scene, "fpk_angle", text="Direction")
        
        # Group: Player Stats
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Player Stats")
        col.prop(scene, "fpk_stamina", text="Stamina")
        col.prop(scene, "fpk_armor", text="Armor")
        col.prop(scene, "fpk_cleanliness", text="Cleanliness")
        col.prop(scene, "fpk_creampie", text="Creampie")
        
        # Group: Inventory
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Inventory")
        col.prop(scene, "fpk_gold", text="Gold")
        
        # Group: Options
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Options")
        col.prop(scene, "fpk_pregnant", text="Enable Pregnancy")
        col.prop(scene, "fpk_birthing", text="Enable Child Birth")
        col.prop(scene, "fpk_blizzard", text="Blizzard Effects")
        col.prop(scene, "fpk_windowed", text="Windowed Mode")
        col.prop(scene, "fpk_brightness", text="Brightness")
        col.prop(scene, "fpk_resolution", text="Resolution")
        col.prop(scene, "fpk_graphics_quality", text="Graphics Quality")
        col.prop(scene, "fpk_encounter_rate", text="Encounter Rate")

        # Group: Experience and Stats
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Experience and Stats")
        col.prop(scene, "fpk_sex", text="Sex")
        col.prop(scene, "fpk_vaginal_ejac", text="Vaginal Ejac")
        col.prop(scene, "fpk_oral_ejac", text="Oral Ejac")
        col.prop(scene, "fpk_menstruation", text="Menstruation")
        col.prop(scene, "fpk_ovulated", text="Ovulated")
        col.prop(scene, "fpk_fertilized", text="Fertilized")
        col.prop(scene, "fpk_implanted", text="Implanted")
        col.prop(scene, "fpk_childbirth", text="Childbirth")
        col.prop(scene, "fpk_raped", text="Raped")
        col.prop(scene, "fpk_prostitute", text="Prostitute")
        col.prop(scene, "fpk_yobai", text="Yobai")
        col.prop(scene, "fpk_fellatio", text="Fellatio")
        col.prop(scene, "fpk_cunnilingus", text="Cunnilingus")
        col.prop(scene, "fpk_imprisonment", text="Imprisonment")
        col.prop(scene, "fpk_battle", text="Battle")
        col.prop(scene, "fpk_pushed_down", text="Pushed Down")
        col.prop(scene, "fpk_defeat", text="Defeat")
        
        # Load and Save buttons
        layout.operator("fpk.load_csv", text="Load CSV")
        layout.operator("fpk.save_csv", text="Save CSV")

# Operator to load data from the CSV
class FPK_OT_LoadCSV(bpy.types.Operator):
    bl_label = "Load CSV"
    bl_idname = "fpk.load_csv"
    
    def execute(self, context):
        load_csv_values(context.scene)
        self.report({'INFO'}, "CSV Loaded Successfully")
        return {'FINISHED'}

# Operator to save data to the CSV
class FPK_OT_SaveCSV(bpy.types.Operator):
    bl_label = "Save CSV"
    bl_idname = "fpk.save_csv"
    
    def execute(self, context):
        write_csv_values(context.scene)
        self.report({'INFO'}, "CSV Saved Successfully")
        return {'FINISHED'}

# Registration functions
def register():
    register_props()
    bpy.utils.register_class(FPK_PT_Panel)
    bpy.utils.register_class(FPK_OT_LoadCSV)
    bpy.utils.register_class(FPK_OT_SaveCSV)

def unregister():
    bpy.utils.unregister_class(FPK_PT_Panel)
    bpy.utils.unregister_class(FPK_OT_LoadCSV)
    bpy.utils.unregister_class(FPK_OT_SaveCSV)
    del bpy.types.Scene.fpk_pos_x
    del bpy.types.Scene.fpk_pos_y
    del bpy.types.Scene.fpk_pos_z
    del bpy.types.Scene.fpk_angle
    del bpy.types.Scene.fpk_stamina
    del bpy.types.Scene.fpk_armor
    del bpy.types.Scene.fpk_cleanliness
    del bpy.types.Scene.fpk_creampie
    del bpy.types.Scene.fpk_gold
    del bpy.types.Scene.fpk_pregnant
    del bpy.types.Scene.fpk_birthing
    del bpy.types.Scene.fpk_blizzard
    del bpy.types.Scene.fpk_windowed
    del bpy.types.Scene.fpk_brightness
    del bpy.types.Scene.fpk_sex
    del bpy.types.Scene.fpk_vaginal_ejac
    del bpy.types.Scene.fpk_oral_ejac
    del bpy.types.Scene.fpk_menstruation
    del bpy.types.Scene.fpk_ovulated
    del bpy.types.Scene.fpk_fertilized
    del bpy.types.Scene.fpk_implanted
    del bpy.types.Scene.fpk_childbirth
    del bpy.types.Scene.fpk_raped
    del bpy.types.Scene.fpk_prostitute
    del bpy.types.Scene.fpk_yobai
    del bpy.types.Scene.fpk_fellatio
    del bpy.types.Scene.fpk_cunnilingus
    del bpy.types.Scene.fpk_imprisonment
    del bpy.types.Scene.fpk_battle
    del bpy.types.Scene.fpk_pushed_down
    del bpy.types.Scene.fpk_defeat
    del bpy.types.Scene.fpk_location
    del bpy.types.Scene.fpk_resolution
    del bpy.types.Scene.fpk_graphics_quality
    del bpy.types.Scene.fpk_encounter_rate

if __name__ == "__main__":
    register()
