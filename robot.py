import wpilib


# noinspection PyAttributeOutsideInit
class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        self.robot_drive = wpilib.RobotDrive(0, 1, 3, 2)
        self.robot_drive.setExpiration(0.1)
        #self.stick = wpilib.XboxController(1)
        self.stick = wpilib.Joystick(1)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Check if we've completed 100 loops (approximately 2 seconds)
        if self.auto_loop_counter < 100:
            self.robot_drive.drive(-0.5, 0)  # Drive forwards at half speed
            self.auto_loop_counter += 1
        else:
            self.robot_drive.drive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
<<<<<<< HEAD
        left_stick = self.stick.getRawAxis(1)/2
        right_stick = self.stick.getRawAxis(5)/2
        #left_stick = self.stick.getY(wpilib.XboxController.Hand.kLeft)
        #right_stick = self.stick.getY(wpilib.XboxController.Hand.kRight)
=======
        # left_stick = self.stick.getRawAxis(1)/2
        # right_stick = self.stick.getRawAxis(5)/2
        left_stick = self.stick.getY(wpilib.XboxController.Hand.kLeft)
        right_stick = self.stick.getX(wpilib.XboxController.Hand.kRight)
>>>>>>> 702b4981f5dc826f94b85527b42de3a5cec6b39e
        self.robot_drive.tankDrive(left_stick, right_stick)

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()


if __name__ == "__main__":
    wpilib.run(MyRobot)
