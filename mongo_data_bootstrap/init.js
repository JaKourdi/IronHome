var dbName = 'customermgmt';
var db = db.getSiblingDB(dbName);


db.user.insertMany([
  {
    username: 'dummy1',
    // "IRON552!$source" same for dummy2
    password: 'pbkdf2:sha256:600000$IwKYbuFdym0NI3aY$ddb6a08827e3307671d0eef2b85b559ac87a42449f196071139d475841c6f05d',
    active: true,
  },
  {
    username: 'dummy2',
    password: 'pbkdf2:sha256:600000$IwKYbuFdym0NI3aY$ddb6a08827e3307671d0eef2b85b559ac87a42449f196071139d475841c6f05d',
    active: true,
  },
]);

var dummyUsername1 = db.user.findOne({ username: 'dummy1' });
var dummyUsername2 = db.user.findOne({ username: 'dummy2' });

db.item.insertMany([
  {
    name: 'DummyItem1',
    description: "blabl",
    available: true,
    cost: 20,
  },
  {
    name: 'DummyItem2',
    description: "blabl",
    available: true,
    cost: 20,
  },
  {
    name: 'DummyItem3',
    description: "blabl",
    cost: 20,
  },
  {
    name: 'DummyItem4',
    description: "blabl",
    cost: 20,
  },
]);

var dummyItem1 = db.item.findOne({ name: 'DummyItem1' });
var dummyItem2 = db.item.findOne({ name: 'DummyItem2' });

db.order.insertMany([
  {
    name: 'Order1',
    description: 'Description 1',
    total: 11.99,
    items: [
      { itemId: dummyItem1._id },
    ],
    usernameId: dummyUsername1._id,
  },
  {
    name: 'Order2',
    description: 'Description 2',
    total: 12.99,
    items: [
      { itemId: dummyItem2._id },
    ],
    usernameId: dummyUsername1._id,
  },
  {
    name: 'Order3',
    description: 'Description 3',
    total: 13.99,
    items: [
      { itemId: dummyItem1._id },
      { itemId: dummyItem2._id },
    ],
    usernameId: dummyUsername2._id,
  },
]);
