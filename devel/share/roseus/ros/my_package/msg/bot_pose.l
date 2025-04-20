;; Auto-generated. Do not edit!


(when (boundp 'my_package::bot_pose)
  (if (not (find-package "MY_PACKAGE"))
    (make-package "MY_PACKAGE"))
  (shadow 'bot_pose (find-package "MY_PACKAGE")))
(unless (find-package "MY_PACKAGE::BOT_POSE")
  (make-package "MY_PACKAGE::BOT_POSE"))

(in-package "ROS")
;;//! \htmlinclude bot_pose.msg.html


(defclass my_package::bot_pose
  :super ros::object
  :slots (_command _x _y _theta ))

(defmethod my_package::bot_pose
  (:init
   (&key
    ((:command __command) "")
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:theta __theta) 0.0)
    )
   (send-super :init)
   (setq _command (string __command))
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _theta (float __theta))
   self)
  (:command
   (&optional __command)
   (if __command (setq _command __command)) _command)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:theta
   (&optional __theta)
   (if __theta (setq _theta __theta)) _theta)
  (:serialization-length
   ()
   (+
    ;; string _command
    4 (length _command)
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _theta
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _command
       (write-long (length _command) s) (princ _command s)
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _theta
       (sys::poke _theta (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _command
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _command (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _theta
     (setq _theta (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get my_package::bot_pose :md5sum-) "73fdb5a9e2fcf473f35b1e1ab498b36d")
(setf (get my_package::bot_pose :datatype-) "my_package/bot_pose")
(setf (get my_package::bot_pose :definition-)
      "string command
float64 x
float64 y
float64 theta


")



(provide :my_package/bot_pose "73fdb5a9e2fcf473f35b1e1ab498b36d")


