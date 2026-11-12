// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from franka_spine_msgs:srv/SwitchOn.idl
// generated code does not contain a copyright notice

#ifndef FRANKA_SPINE_MSGS__SRV__DETAIL__SWITCH_ON__BUILDER_HPP_
#define FRANKA_SPINE_MSGS__SRV__DETAIL__SWITCH_ON__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "franka_spine_msgs/srv/detail/switch_on__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace franka_spine_msgs
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::franka_spine_msgs::srv::SwitchOn_Request>()
{
  return ::franka_spine_msgs::srv::SwitchOn_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace franka_spine_msgs


namespace franka_spine_msgs
{

namespace srv
{

namespace builder
{

class Init_SwitchOn_Response_message
{
public:
  explicit Init_SwitchOn_Response_message(::franka_spine_msgs::srv::SwitchOn_Response & msg)
  : msg_(msg)
  {}
  ::franka_spine_msgs::srv::SwitchOn_Response message(::franka_spine_msgs::srv::SwitchOn_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::franka_spine_msgs::srv::SwitchOn_Response msg_;
};

class Init_SwitchOn_Response_success
{
public:
  explicit Init_SwitchOn_Response_success(::franka_spine_msgs::srv::SwitchOn_Response & msg)
  : msg_(msg)
  {}
  Init_SwitchOn_Response_message success(::franka_spine_msgs::srv::SwitchOn_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_SwitchOn_Response_message(msg_);
  }

private:
  ::franka_spine_msgs::srv::SwitchOn_Response msg_;
};

class Init_SwitchOn_Response_state
{
public:
  Init_SwitchOn_Response_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SwitchOn_Response_success state(::franka_spine_msgs::srv::SwitchOn_Response::_state_type arg)
  {
    msg_.state = std::move(arg);
    return Init_SwitchOn_Response_success(msg_);
  }

private:
  ::franka_spine_msgs::srv::SwitchOn_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::franka_spine_msgs::srv::SwitchOn_Response>()
{
  return franka_spine_msgs::srv::builder::Init_SwitchOn_Response_state();
}

}  // namespace franka_spine_msgs

#endif  // FRANKA_SPINE_MSGS__SRV__DETAIL__SWITCH_ON__BUILDER_HPP_
