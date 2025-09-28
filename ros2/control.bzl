""" Implements a macro for setting up a ROS 2 controller manager.
"""

load("@com_github_mvukov_rules_ros2//ros2:cc_defs.bzl", "ros2_cpp_binary")

def ros2_controller_manager(name, controller_plugins = None, **kwargs):
    ros2_cpp_binary(
        name = name,
        set_up_ament = True,
        srcs = ["@ros2_control//:controller_manager/src/ros2_control_node.cpp"],
        data = controller_plugins,
        deps = [
            "@ros2_control//:controller_manager",
            "@ros2_rclcpp//:rclcpp",
            "@ros2_realtime_tools//:realtime_tools",
        ],
    )
