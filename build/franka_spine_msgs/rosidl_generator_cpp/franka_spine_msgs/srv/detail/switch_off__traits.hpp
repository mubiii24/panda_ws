// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from franka_spine_msgs:srv/SwitchOff.idl
// generated code does not contain a copyright notice

#ifndef FRANKA_SPINE_MSGS__SRV__DETAIL__SWITCH_OFF__TRAITS_HPP_
#define FRANKA_SPINE_MSGS__SRV__DETAIL__SWITCH_OFF__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "franka_spine_msgs/srv/detail/switch_off__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace franka_spine_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SwitchOff_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SwitchOff_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SwitchOff_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace franka_spine_msgs

namespace rosidl_generator_traits
{

[[deprecated("use franka_spine_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const franka_spine_msgs::srv::SwitchOff_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  franka_spine_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use franka_spine_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const franka_spine_msgs::srv::SwitchOff_Request & msg)
{
  return franka_spine_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<franka_spine_msgs::srv::SwitchOff_Request>()
{
  return "franka_spine_msgs::srv::SwitchOff_Request";
}

template<>
inline const char * name<franka_spine_msgs::srv::SwitchOff_Request>()
{
  return "franka_spine_msgs/srv/SwitchOff_Request";
}

template<>
struct has_fixed_size<franka_spine_msgs::srv::SwitchOff_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<franka_spine_msgs::srv::SwitchOff_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<franka_spine_msgs::srv::SwitchOff_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace franka_spine_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SwitchOff_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: state
  {
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << ", ";
  }

  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: message
  {
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SwitchOff_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << "\n";
  }

  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }

  // member: message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SwitchOff_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace franka_spine_msgs

namespace rosidl_generator_traits
{

[[deprecated("use franka_spine_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const franka_spine_msgs::srv::SwitchOff_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  franka_spine_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use franka_spine_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const franka_spine_msgs::srv::SwitchOff_Response & msg)
{
  return franka_spine_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<franka_spine_msgs::srv::SwitchOff_Response>()
{
  return "franka_spine_msgs::srv::SwitchOff_Response";
}

template<>
inline const char * name<franka_spine_msgs::srv::SwitchOff_Response>()
{
  return "franka_spine_msgs/srv/SwitchOff_Response";
}

template<>
struct has_fixed_size<franka_spine_msgs::srv::SwitchOff_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<franka_spine_msgs::srv::SwitchOff_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<franka_spine_msgs::srv::SwitchOff_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<franka_spine_msgs::srv::SwitchOff>()
{
  return "franka_spine_msgs::srv::SwitchOff";
}

template<>
inline const char * name<franka_spine_msgs::srv::SwitchOff>()
{
  return "franka_spine_msgs/srv/SwitchOff";
}

template<>
struct has_fixed_size<franka_spine_msgs::srv::SwitchOff>
  : std::integral_constant<
    bool,
    has_fixed_size<franka_spine_msgs::srv::SwitchOff_Request>::value &&
    has_fixed_size<franka_spine_msgs::srv::SwitchOff_Response>::value
  >
{
};

template<>
struct has_bounded_size<franka_spine_msgs::srv::SwitchOff>
  : std::integral_constant<
    bool,
    has_bounded_size<franka_spine_msgs::srv::SwitchOff_Request>::value &&
    has_bounded_size<franka_spine_msgs::srv::SwitchOff_Response>::value
  >
{
};

template<>
struct is_service<franka_spine_msgs::srv::SwitchOff>
  : std::true_type
{
};

template<>
struct is_service_request<franka_spine_msgs::srv::SwitchOff_Request>
  : std::true_type
{
};

template<>
struct is_service_response<franka_spine_msgs::srv::SwitchOff_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // FRANKA_SPINE_MSGS__SRV__DETAIL__SWITCH_OFF__TRAITS_HPP_
