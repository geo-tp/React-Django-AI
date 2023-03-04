import { InfoBanner } from "./components/InfoBanner";
import { Footer } from "./layouts/Footer";
import { Header } from "./layouts/Header";
import { HomePage } from "./pages/HomePage";

function App() {
  return (
    <div className="App">
      <Header />
      <InfoBanner content="Various Deep learning models deployed with a Django API, using Tensorflow, Keras and Pytorch. Try it below." />
      <HomePage />
      <Footer />
    </div>
  );
}

export default App;
