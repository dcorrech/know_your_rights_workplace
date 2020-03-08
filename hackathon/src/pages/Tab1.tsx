import React, { useState } from 'react';
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar, IonItem, IonLabel, IonSelect, IonSelectOption, IonTextarea, IonButton, IonFooter, IonLoading } from '@ionic/react';
import './Tab1.css';
import { RouteComponentProps } from 'react-router-dom';

const Tab1: React.FC<RouteComponentProps> = (props) => {
  const [displayLoading, setDisplayLoading] = useState(false);
  const [whatHappened, setWhatHappened] = useState('');
  const [employer, setEmployer] = useState('');
  const [reasonWhy, setReasonWhy] = useState([]);
  const [whereHappened, setWhereHappened] = useState('');
  const [description, setDescription] = useState('');

  const getResolution = () => {
    setDisplayLoading(true);
    setTimeout(() => {
      setDisplayLoading(false);
      console.log(whatHappened,employer,reasonWhy,whereHappened,description);
      props.history.push('/tab3')
    }, 5000);
  }
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Complaint Form</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent>
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">Complaint Form</IonTitle>
          </IonToolbar>
        </IonHeader>
        <IonItem>
          <IonLabel>What Happened?</IonLabel>
          <IonSelect onIonChange={(e) => setWhatHappened(e.detail.value)} placeholder="Select One">
            <IonSelectOption value="fired">I was fired</IonSelectOption>
            <IonSelectOption value="demoted">I was demoted</IonSelectOption>
            <IonSelectOption value="not_promoted">I was not promoted</IonSelectOption>
            <IonSelectOption value="no_service">I did not receive a service</IonSelectOption>
            <IonSelectOption value="harassed">I was harassed</IonSelectOption>
            <IonSelectOption value="access_work">I had accessibility problems at work</IonSelectOption>
            <IonSelectOption value="access_serv">I had accessibility problems when receiving a service</IonSelectOption>
            <IonSelectOption value="accom_work">I was not accommodated at work</IonSelectOption>
            <IonSelectOption value="accom_serv">I was not accommodated when receiving a service</IonSelectOption>
            <IonSelectOption value="other">Other</IonSelectOption>
          </IonSelect>
        </IonItem>
        <IonItem>
          <IonLabel>Who is the employer?</IonLabel>
          <IonSelect onIonChange={(e) => setEmployer(e.detail.value)} placeholder="Select One">
            <IonSelectOption value="Provincial or territorial government department">Provincial or territorial government dept</IonSelectOption>
            <IonSelectOption value="Restaurant">Restaurant</IonSelectOption>
            <IonSelectOption value="Hospital">Hospital</IonSelectOption>
            <IonSelectOption value="School">School</IonSelectOption>
            <IonSelectOption value="Local Police">Local Police</IonSelectOption>
            <IonSelectOption value="Retail Store">Retail Store</IonSelectOption>
            <IonSelectOption value="Govt. of Canada Department">Govt. of Canada Department</IonSelectOption>
            <IonSelectOption value="Bank">Bank</IonSelectOption>
            <IonSelectOption value="Airport or Airline">Airport or Airline</IonSelectOption>
            <IonSelectOption value="Ships and Navigation">Ships and Navigation</IonSelectOption>
            <IonSelectOption value="Media">Media</IonSelectOption>
            <IonSelectOption value="Phone or Internet Provider">Phone or Internet Provider</IonSelectOption>
            <IonSelectOption value="Transportation and Logistics">Transportation and Logistics</IonSelectOption>
            <IonSelectOption value="First Nations Government or Band">First Nations Government or Band</IonSelectOption>
            <IonSelectOption value="RCMP">RCMP</IonSelectOption>
            <IonSelectOption value="Other">Other</IonSelectOption>
          </IonSelect>
        </IonItem>
        <IonItem>
          <IonLabel>Why do you think this happened?</IonLabel>
          <IonSelect onIonChange={(e) => setReasonWhy(e.detail.value)} multiple={true} cancelText="Cancel" okText="Confirm">
            <IonSelectOption value="race">My race</IonSelectOption>
            <IonSelectOption value="nationality">My national or ethnic region</IonSelectOption>
            <IonSelectOption value="colour">My colour</IonSelectOption>
            <IonSelectOption value="religion">My religion</IonSelectOption>
            <IonSelectOption value="age">My age</IonSelectOption>
            <IonSelectOption value="sex">My sex</IonSelectOption>
            <IonSelectOption value="orientation">My sexual orientation</IonSelectOption>
            <IonSelectOption value="marital">My marital status</IonSelectOption>
            <IonSelectOption value="family">My family status</IonSelectOption>
            <IonSelectOption value="disability">My disability</IonSelectOption>
            <IonSelectOption value="genetic">My genetic information</IonSelectOption>
            <IonSelectOption value="gender_identity">My gender identity or expression</IonSelectOption>
            <IonSelectOption value="pardon">A conviction for which I have received a pardon</IonSelectOption>
            <IonSelectOption value="other">Other</IonSelectOption>
          </IonSelect>
        </IonItem>
        <IonItem>
          <IonLabel>Location of Incident</IonLabel>
          <IonSelect onIonChange={(e) => setWhereHappened(e.detail.value)} placeholder="Select One">
            <IonSelectOption value="Alberta">Alberta</IonSelectOption>
            <IonSelectOption value="British Columbia">British Columbia</IonSelectOption>
            <IonSelectOption value="Manitoba">Manitoba</IonSelectOption>
            <IonSelectOption value="New Brunswick">New Brunswick</IonSelectOption>
            <IonSelectOption value="NewFoundland and Labrador">NewFoundland and Labrador</IonSelectOption>
            <IonSelectOption value="Northwest Territories">Northwest Territories</IonSelectOption>
            <IonSelectOption value="Nova Scotia">Nova Scotia</IonSelectOption>
            <IonSelectOption value="Nunavut">Nunavut</IonSelectOption>
            <IonSelectOption value="Ontario">Ontario</IonSelectOption>
            <IonSelectOption value="Prince Edward Island">Prince Edward Island</IonSelectOption>
            <IonSelectOption value="Quebec">Quebec</IonSelectOption>
            <IonSelectOption value="Saskatchewan">Saskatchewan</IonSelectOption>
            <IonSelectOption value="Yukon">Yukon</IonSelectOption>
            <IonSelectOption value="Outside of Canada">Outside of Canada</IonSelectOption>
          </IonSelect>
        </IonItem>
        <IonItem>
          <IonLabel position="floating">Description</IonLabel>
          <IonTextarea autoGrow={true} onIonChange={(e) => setDescription(e.detail.value!)}></IonTextarea>
        </IonItem>
        <IonLoading
          isOpen={displayLoading}
          message="Working on finding best resoluton..."
        />
      </IonContent>
      <IonFooter>
        <IonToolbar>
          <IonButton expand="block" onClick={getResolution}>Submit</IonButton>
        </IonToolbar>
      </IonFooter>
    </IonPage>
  );
};

export default Tab1;
