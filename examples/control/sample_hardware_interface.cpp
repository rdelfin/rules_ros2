#include "sample_hardware_interface.hpp"

namespace control_examples {

hardware_interface::CallbackReturn SampleHardwareInterface::on_init(
    const hardware_interface::HardwareComponentInterfaceParams& params)
    override {
  if (hardware_interface::SystemInterface::on_init(params) !=
      hardware_interface::CallbackReturn::SUCCESS) {
    return hardware_interface::CallbackReturn::ERROR;
  }

  RCLCPP_INFO(get_logger(), "I am configuring a sample hardware");
  return hardware_interface::CallbackReturn::SUCCESS;
}

hardware_interface::CallbackReturn SampleHardwareInterface::on_configure(
    const rclcpp_lifecycle::State& previous_state) override {
  RCLCPP_INFO(get_logger(), "Configuring sample hardware");
  return hardware_interface::CallbackReturn::SUCCESS;
}

hardware_interface::CallbackReturn SampleHardwareInterface::on_activate(
    const rclcpp_lifecycle::State& previous_state) override {
  return hardware_interface::CallbackReturn::SUCCESS;
}

hardware_interface::CallbackReturn SampleHardwareInterface::on_deactivate(
    const rclcpp_lifecycle::State& previous_state) override {
  return hardware_interface::CallbackReturn::SUCCESS;
}

hardware_interface::return_type SampleHardwareInterface::read(
    const rclcpp::Time& time, const rclcpp::Duration& period) override {
  return hardware_interface::return_type::OK;
}

hardware_interface::return_type SampleHardwareInterface::write(
    const rclcpp::Time& time, const rclcpp::Duration& period) override {
  return hardware_interface::return_type::OK;
}

}  // namespace control_examples

#include "pluginlib/class_list_macros.hpp"
PLUGINLIB_EXPORT_CLASS(control_examples::SampleHardwareInterface,
                       hardware_interface::SystemInterface)
