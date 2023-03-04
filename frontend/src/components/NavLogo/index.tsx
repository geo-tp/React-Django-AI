import RobotSmall from "../../assets/img/robot-small.png";

export const NavLogo = () => {
  return (
    <div className="nav-logo">
      <div className="nav-logo__icon">
        <img src={RobotSmall} alt="A robot's head" />
      </div>
      <h1>
        <span>Django</span>
        <span>AI</span>
      </h1>
    </div>
  );
};
