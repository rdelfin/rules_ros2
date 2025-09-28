import sys

import ros2cli.cli
import ros2controlcli.verb.list_controller_types
import ros2controlcli.verb.list_controllers
import ros2controlcli.verb.list_hardware_components
import ros2controlcli.verb.list_hardware_interfaces
import ros2controlcli.verb.load_controller
import ros2controlcli.verb.reload_controller_libraries
import ros2controlcli.verb.set_controller_state
import ros2controlcli.verb.set_hardware_component_state
import ros2controlcli.verb.switch_controllers
import ros2controlcli.verb.unload_controller

import ros2.ros2_cmd

COMMAND_EXTENSIONS = {
    'list_controller_types':
        ros2controlcli.verb.list_controller_types.ListControllerTypesVerb(),
    'list_hardware_interfaces':
        ros2controlcli.verb.list_hardware_interfaces.ListHardwareInterfacesVerb(
        ),
    'reload_controller_libraries':
        ros2controlcli.verb.reload_controller_libraries.
        ReloadControllerLibrariesVerb(),
    'set_hardware_component_state':
        ros2controlcli.verb.set_hardware_component_state.
        SetHardwareComponentStateVerb(),
    'unload_controller':
        ros2controlcli.verb.unload_controller.UnloadControllerVerb(),
    'list_controllers':
        ros2controlcli.verb.list_controllers.ListControllersVerb(),
    'list_hardware_components':
        ros2controlcli.verb.list_hardware_components.ListHardwareComponentsVerb(
        ),
    'load_controller':
        ros2controlcli.verb.load_controller.LoadControllerVerb(),
    'set_controller_state':
        ros2controlcli.verb.set_controller_state.SetControllerStateVerb(),
    'switch_controllers':
        ros2controlcli.verb.switch_controllers.SwitchControllersVerb(),
}

extension = ros2.ros2_cmd.Ros2CommandExtension(COMMAND_EXTENSIONS)
sys.exit(ros2cli.cli.main(argv=sys.argv[1:], extension=extension))
