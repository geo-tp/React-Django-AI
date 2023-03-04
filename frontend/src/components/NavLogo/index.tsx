import Robot from "../../assets/img/robot.svg";

export const NavLogo = () => {
  return (
    <div className="nav-logo">
      <div className="nav-logo__icon">
        <img src={Robot} alt="A robot's head" />
      </div>
      <h1>
        <span>Django</span>
        <span>AI</span>
      </h1>
    </div>
  );
};
