// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from franka_spine_msgs:srv/GetSpineState.idl
// generated code does not contain a copyright notice

#ifndef FRANKA_SPINE_MSGS__SRV__DETAIL__GET_SPINE_STATE__TRAITS_HPP_
#define FRANKA_SPINE_MSGS__SRV__DETAIL__GET_SPINE_STATE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "franka_spine_msgs/srv/detail/get_spine_state__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace franka_spine_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetSpineState_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetSpineState_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetSpineState_Request & msg, bool use_flow_style = false)
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
  const franka_spine_msgs::srv::GetSpineState_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  franka_spine_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use franka_spine_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const franka_spine_msgs::srv::GetSpineState_Request & msg)
{
  return franka_spine_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<franka_spine_msgs::srv::GetSpineState_Request>()
{
  return "franka_spine_msgs::srv::GetSpineState_Request";
}

template<>
inline const char * name<franka_spine_msgs::srv::GetSpineState_Request>()
{
  return "franka_spine_msgs/srv/GetSpineState_Request";
}

template<>
struct has_fixed_size<franka_spine_msgs::srv::GetSpineState_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<franka_spine_msgs::srv::GetSpineState_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<franka_spine_msgs::srv::GetSpineState_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace franka_spine_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetSpineState_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: state
  {
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << ", ";
  }

  // member: error_code
  {
    out << "error_code: ";
    rosidl_generator_traits::value_to_yaml(msg.error_code, out);
    out << ", ";
  }

  // member: error_description
  {
    out << "error_description: ";
    rosidl_generator_traits::value_to_yaml(msg.error_description, out);
    out << ", ";
  }

  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetSpineState_Response & msg,
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

  // member: error_code
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "error_code: ";
    rosidl_generator_traits::value_to_yaml(msg.error_code, out);
    out << "\n";
  }

  // member: error_description
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "error_description: ";
    rosidl_generator_traits::value_to_yaml(msg.error_description, out);
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
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetSpineState_Response & msg, bool use_flow_style = false)
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
  const franka_spine_msgs::srv::GetSpineState_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  franka_spine_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use franka_spine_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const franka_spine_msgs::srv::GetSpineState_Response & msg)
{
  return franka_spine_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<franka_spine_msgs::srv::GetSpineState_Response>()
{
  return "franka_spine_msgs::srv::GetSpineState_Response";
}

template<>
inline const char * name<franka_spine_msgs::srv::GetSpineState_Response>()
{
  return "franka_spine_msgs/srv/GetSpineState_Response";
}

template<>
struct has_fixed_size<franka_spine_msgs::srv::GetSpineState_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<franka_spine_msgs::srv::GetSpineState_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<franka_spine_msgs::srv::GetSpineState_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<franka_spine_msgs::srv::GetSpineState>()
{
  return "franka_spine_msgs::srv::GetSpineState";
}

template<>
inline const char * name<franka_spine_msgs::srv::GetSpineState>()
{
  return "franka_spine_msgs/srv/GetSpineState";
}

template<>
struct has_fixed_size<franka_spine_msgs::srv::GetSpineState>
  : std::integral_constant<
    bool,
    has_fixed_size<franka_spine_msgs::srv::GetSpineState_Request>::value &&
    has_fixed_size<franka_spine_msgs::srv::GetSpineState_Response>::value
  >
{
};

template<>
struct has_bounded_size<franka_spine_msgs::srv::GetSpineState>
  : std::integral_constant<
    bool,
    has_bounded_size<franka_spine_msgs::srv::GetSpineState_Request>::value &&
    has_bounded_size<franka_spine_msgs::srv::GetSpineState_Response>::value
  >
{
};

template<>
struct is_service<franka_spine_msgs::srv::GetSpineState>
  : std::true_type
{
};

template<>
struct is_service_request<franka_spine_msgs::srv::GetSpineState_Request>
  : std::true_type
{
};

template<>
struct is_service_response<franka_spine_msgs::srv::GetSpineState_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // FRANKA_SPINE_MSGS__SRV__DETAIL__GET_SPINE_STATE__TRAITS_HPP_
